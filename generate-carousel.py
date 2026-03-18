"""
LinkedIn Carousel Generator
Generates a PDF carousel (1080x1080 per slide) for LinkedIn posts.
Carousels generate 6x more engagement than text-only posts.

Usage:
    python generate-carousel.py

Customize the SLIDES list below with your content.
"""

from PIL import Image, ImageDraw, ImageFont
import os
import sys

# --- Configuration ---
SLIDE_SIZE = (1080, 1080)
BG_COLOR = "#0D1117"
ACCENT_COLOR = "#8B5CF6"  # Purple for CLI theme
WHITE = "#FFFFFF"
GRAY = "#8B949E"
LIGHT_GRAY = "#C9D1D9"

# --- Slide Content ---
# Customize this list for each post.
# Each slide is a dict with: title (optional), body, type (cover/content/cta)
SLIDES = [
    {
        "type": "cover",
        "title": "Copilot no terminal\né onde o jogo muda.",
        "subtitle": "6 coisas que mudaram no meu workflow\ndesde que uso Copilot CLI",
    },
    {
        "type": "content",
        "number": "01",
        "title": "Debug sem sair\ndo terminal",
        "body": "Colo o erro direto no Copilot CLI.\n\nEle responde em cima do contexto\ndo meu projeto — não de um\nfórum de 2018.",
    },
    {
        "type": "content",
        "number": "02",
        "title": "Scripts em\nsegundos",
        "body": "Descrevo o objetivo.\nO Copilot gera o script.\nEu reviso e itero.\n\nSem pausar o raciocínio\npra lembrar sintaxe.",
    },
    {
        "type": "content",
        "number": "03",
        "title": "Explorar codebases\nnovas",
        "body": "\"Onde está a autenticação?\"\n\"Qual fluxo dispara esse job?\"\n\nMais útil do que sair\ndando grep aleatório.",
    },
    {
        "type": "content",
        "number": "04",
        "title": "Comandos que\nnunca lembro",
        "body": "kubectl, docker, git reflog,\nPowerShell, awk, sed...\n\nPedir pro Copilot é mais rápido\nque man pages.",
    },
    {
        "type": "content",
        "number": "05",
        "title": "O ganho real não é\nvelocidade",
        "body": "É reduzir troca de contexto.\n\nManter o raciocínio técnico\ndentro do ambiente onde\no problema existe.",
    },
    {
        "type": "cta",
        "title": "Copilot no editor\najuda a produzir código.\n\nCopilot CLI ajuda\na destravar trabalho.",
        "cta": "Você já testou no seu\nfluxo real de debug?",
        "hashtags": "#GitHubCopilot #CopilotCLI\n#DevTools #AI",
    },
]

SERIES_BADGE = "GITHUB COPILOT SERIES · POST 2/6"
OUTPUT_DIR = "images"


def get_font(size, bold=False):
    candidates = [
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def draw_accent_bar(draw, x, y, w, h, color):
    draw.rectangle([x, y, x + w, y + h], fill=color)


def draw_dot_pattern(draw, start_x, start_y, end_x, end_y, color, spacing=18):
    for x in range(start_x, end_x, spacing):
        for y in range(start_y, end_y, spacing):
            draw.ellipse([x, y, x + 3, y + 3], fill=color)


def create_slide(slide_data, index, total):
    img = Image.new("RGB", SLIDE_SIZE, BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Accent bar (left)
    draw_accent_bar(draw, 0, 0, 6, SLIDE_SIZE[1], ACCENT_COLOR)

    # Dot pattern (bottom right, subtle)
    draw_dot_pattern(draw, 880, 900, 1060, 1060, "#1C2128")

    # Slide number / total (bottom right)
    font_sm = get_font(16)
    page_text = f"{index + 1}/{total}"
    tw = draw.textlength(page_text, font=font_sm)
    draw.text((SLIDE_SIZE[0] - tw - 40, SLIDE_SIZE[1] - 50), page_text, fill=GRAY, font=font_sm)

    slide_type = slide_data.get("type", "content")

    if slide_type == "cover":
        # Series badge
        font_badge = get_font(14, bold=True)
        badge_w = draw.textlength(SERIES_BADGE, font=font_badge) + 24
        draw.rounded_rectangle([50, 60, 50 + badge_w, 88], radius=4, fill=ACCENT_COLOR)
        draw.text((62, 66), SERIES_BADGE, fill=WHITE, font=font_badge)

        # Title
        font_title = get_font(56, bold=True)
        draw.multiline_text((50, 200), slide_data["title"], fill=WHITE, font=font_title, spacing=12)

        # Subtitle
        font_sub = get_font(28)
        draw.multiline_text((50, 550), slide_data.get("subtitle", ""), fill=ACCENT_COLOR, font=font_sub, spacing=8)

        # Swipe hint
        font_hint = get_font(18)
        draw.text((50, SLIDE_SIZE[1] - 80), "Deslize para ver →", fill=GRAY, font=font_hint)

    elif slide_type == "content":
        # Number badge
        number = slide_data.get("number", "")
        if number:
            font_num = get_font(72, bold=True)
            draw.text((50, 50), number, fill=ACCENT_COLOR, font=font_num)

        # Title
        font_title = get_font(44, bold=True)
        title_y = 170 if number else 80
        draw.multiline_text((50, title_y), slide_data.get("title", ""), fill=WHITE, font=font_title, spacing=10)

        # Body
        font_body = get_font(28)
        draw.multiline_text((50, 450), slide_data.get("body", ""), fill=LIGHT_GRAY, font=font_body, spacing=10)

    elif slide_type == "cta":
        # Main text
        font_title = get_font(40, bold=True)
        draw.multiline_text((50, 100), slide_data.get("title", ""), fill=WHITE, font=font_title, spacing=12)

        # CTA question
        font_cta = get_font(32)
        draw.multiline_text((50, 600), slide_data.get("cta", ""), fill=ACCENT_COLOR, font=font_cta, spacing=8)

        # Hashtags
        font_hash = get_font(22)
        draw.multiline_text((50, 850), slide_data.get("hashtags", ""), fill=GRAY, font=font_hash, spacing=6)

        # Save hint
        font_hint = get_font(18)
        draw.text((50, SLIDE_SIZE[1] - 50), "💾 Salve este post para referência", fill=GRAY, font=font_hint)

    return img


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    images = []
    total = len(SLIDES)

    for i, slide_data in enumerate(SLIDES):
        img = create_slide(slide_data, i, total)
        images.append(img)
        print(f"  ✓ Slide {i + 1}/{total}: {slide_data.get('type', 'content')}")

    # Save as PDF (all slides in one file)
    output_path = os.path.join(OUTPUT_DIR, "post-2-copilot-cli-carousel.pdf")
    images[0].save(
        output_path, "PDF",
        save_all=True,
        append_images=images[1:],
        resolution=150
    )

    print(f"\n✅ Carousel saved: {output_path}")
    print(f"   Slides: {total}")
    print(f"   Size: {SLIDE_SIZE[0]}x{SLIDE_SIZE[1]}px per slide")
    print(f"\n📤 Upload this PDF directly to LinkedIn as a document post.")


if __name__ == "__main__":
    main()
