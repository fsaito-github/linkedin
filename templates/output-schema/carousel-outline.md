# Carousel Outline — Schema de Roteiro de Carrossel

Quando o formato escolhido for carrossel, o agente deve produzir este roteiro antes de gerar o PDF.

## Schema do roteiro

```
𝗥𝗼𝘁𝗲𝗶𝗿𝗼 𝗱𝗲 𝗖𝗮𝗿𝗿𝗼𝘀𝘀𝗲́𝗹

Tema: [tema]
Slides: [N]
Aspect Ratio: 1:1
Design Style: modern, dark background (#0D1117), bold typography, [cor de acento]

──────────────────────────────

Slide 1 — CAPA
  Título: "[hook visual — frase de impacto]"
  Subtítulo: "[contexto em 1 linha]"
  Badge: "[SÉRIE · POST N/N]" (se aplicável)

Slide 2 — CONTEXTO
  Título: "[o problema]"
  Corpo: "[por que isso importa — máx 40 palavras]"

Slide 3 — [NOME DO INSIGHT]
  Título: "[insight principal]"
  Corpo: "[explicação — máx 40 palavras]"
  Elemento visual: [ícone/dado/destaque sugerido]

Slide 4 — [NOME DO INSIGHT]
  ...

Slide [N-1] — RESULTADO
  Título: "[o que mudou]"
  Corpo: "[dados concretos]"

Slide [N] — CTA
  Título: "[pergunta específica]"
  Corpo: "[convite à ação]"
  Hashtags: [3-5 hashtags]
  Nota: "💾 Salve este post para referência"

──────────────────────────────

Caption do post (texto que acompanha o carrossel no feed):
"[2-4 linhas que complementam o carrossel sem repetir o conteúdo dos slides]"
```

## Validação do roteiro

Antes de gerar o PDF, verificar:

- [ ] Capa tem conflito/tensão (não explicação)
- [ ] 1 ideia por slide
- [ ] Máximo 50 palavras por slide
- [ ] Progressão narrativa clara
- [ ] Último slide tem CTA respondível
- [ ] Caption do post complementa (não duplica) o carrossel
- [ ] Total de slides: 5-8
