"""
Banner generator for LinkedIn Post #2: Copilot CLI
1200x628 — Dark theme with purple accent (#8B5CF6)
Includes a simulated terminal window showing Copilot CLI
"""

from PIL import Image, ImageDraw, ImageFont
import os

WIDTH, HEIGHT = 1200, 628
BG_COLOR = "#0D1117"
ACCENT = "#8B5CF6"
ACCENT_DIM = "#6D3FC4"
WHITE = "#FFFFFF"
GRAY = "#8B949E"
TERMINAL_BG = "#161B22"
TERMINAL_BORDER = "#30363D"
GREEN = "#3FB950"

img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
draw = ImageDraw.Draw(img)

# --- Accent bar (left side) ---
draw.rectangle([0, 0, 6, HEIGHT], fill=ACCENT)

# --- Dot pattern (bottom-right decorative) ---
for x in range(950, 1180, 20):
    for y in range(480, 620, 20):
        opacity = max(0, 255 - int(((x - 950) * 0.5 + (620 - y) * 0.8)))
        if opacity > 40:
            draw.ellipse([x, y, x + 4, y + 4], fill=ACCENT_DIM)

# --- Try to load fonts, fallback to default ---
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

def get_mono_font(size):
    candidates = [
        "C:/Windows/Fonts/consola.ttf",
        "C:/Windows/Fonts/cour.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    ]
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()

font_badge = get_font(14, bold=True)
font_title = get_font(44, bold=True)
font_subtitle = get_font(22)
font_mono = get_mono_font(15)
font_mono_sm = get_mono_font(13)

# --- Series badge (top) ---
badge_text = "GITHUB COPILOT SERIES  ·  POST 2/6"
badge_w = draw.textlength(badge_text, font=font_badge) + 24
badge_h = 28
badge_x, badge_y = 50, 35
draw.rounded_rectangle(
    [badge_x, badge_y, badge_x + badge_w, badge_y + badge_h],
    radius=4, fill=ACCENT
)
draw.text((badge_x + 12, badge_y + 5), badge_text, fill=WHITE, font=font_badge)

# --- Title ---
draw.text((50, 90), "COPILOT CLI", fill=WHITE, font=font_title)

# --- Subtitle ---
draw.text((50, 148), "Do editor pro terminal — e isso muda tudo", fill=ACCENT, font=font_subtitle)

# --- Simulated terminal window ---
term_x, term_y = 50, 200
term_w, term_h = 1100, 380
radius = 10

# Terminal background
draw.rounded_rectangle(
    [term_x, term_y, term_x + term_w, term_y + term_h],
    radius=radius, fill=TERMINAL_BG, outline=TERMINAL_BORDER, width=1
)

# Terminal title bar
draw.rounded_rectangle(
    [term_x, term_y, term_x + term_w, term_y + 36],
    radius=radius, fill="#1C2128"
)
# Cover bottom corners of title bar
draw.rectangle([term_x, term_y + 26, term_x + term_w, term_y + 36], fill="#1C2128")
draw.line([(term_x, term_y + 36), (term_x + term_w, term_y + 36)], fill=TERMINAL_BORDER, width=1)

# Window buttons (red, yellow, green)
for i, color in enumerate(["#FF5F56", "#FFBD2E", "#27C93F"]):
    cx = term_x + 20 + i * 22
    cy = term_y + 18
    draw.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=color)

# Terminal title text
title_text = "Copilot CLI"
tw = draw.textlength(title_text, font=font_mono_sm)
draw.text((term_x + term_w // 2 - tw // 2, term_y + 10), title_text, fill=GRAY, font=font_mono_sm)

# --- Terminal content (simulated Copilot CLI session) ---
line_height = 22
start_y = term_y + 52
left_margin = term_x + 20

lines = [
    (f"$ copilot", WHITE),
    ("", WHITE),
    ("  ╭──────────────────────────────────────────────────────╮", ACCENT),
    ("  │  GitHub Copilot CLI v1.0.5                          │", ACCENT),
    ("  │  Your AI pair programmer, now in the terminal       │", ACCENT),
    ("  ╰──────────────────────────────────────────────────────╯", ACCENT),
    ("", WHITE),
    ("> Explain this error: ECONNREFUSED 127.0.0.1:5432", GREEN),
    ("", WHITE),
    ("  The error means your app can't connect to PostgreSQL", WHITE),
    ("  on localhost:5432. The database server is likely not", WHITE),
    ("  running. Let me check...", WHITE),
    ("", WHITE),
    ("  Running: docker ps --filter name=postgres", GRAY),
    ("  ✓ Found: container 'postgres' is stopped. Starting...", GREEN),
]

for i, (text, color) in enumerate(lines):
    y = start_y + i * line_height
    if y + line_height > term_y + term_h - 10:
        break
    draw.text((left_margin, y), text, fill=color, font=font_mono)

# --- Blinking cursor at the end ---
last_line_y = start_y + len(lines) * line_height
if last_line_y + line_height < term_y + term_h - 10:
    draw.rectangle(
        [left_margin, last_line_y + 2, left_margin + 10, last_line_y + 18],
        fill=GREEN
    )

# --- Save ---
os.makedirs("images", exist_ok=True)
output_path = os.path.join("images", "post-2-copilot-cli-banner.png")
img.save(output_path, "PNG", quality=95)
print(f"✅ Banner saved: {output_path}")
print(f"   Size: {WIDTH}x{HEIGHT}px")
