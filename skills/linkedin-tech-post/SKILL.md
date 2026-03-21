---
name: linkedin-tech-post
description: 'Cria posts técnicos otimizados para LinkedIn que geram comentários qualificados. Use when asked to "create a LinkedIn post", "write a tech post", "generate a hook", "review post commentability", "plan a carousel", "analyze post performance", or when building content for technical audiences on LinkedIn. Supports bilingual PT-BR/EN, banner generation, carousel planning via 2slides, and publishing via LinkedIn API. Includes editorial pipeline with briefing extraction, angle finding, hook generation, commentability scoring, proof checking, and post-mortem analysis.'
---

# LinkedIn Tech Post

Agente orquestrador para criar posts técnicos de LinkedIn otimizados para **comentários qualificados**. Coordena um pipeline editorial de 12 etapas com skills especializadas, scorecard de qualidade e memória editorial.

## When to Use This Skill

- Criar posts técnicos para LinkedIn (texto ou carrossel)
- Gerar e ranquear hooks de alto impacto
- Avaliar comentabilidade e substância de um post
- Planejar roteiro de carrossel
- Analisar performance pós-publicação
- Responder comentários recebidos
- Reciclar posts em novos formatos

## Prerequisites

- Diretório `linkedin/` como workspace
- LinkedIn MCP configurado para publicação (`~/.linkedin-mcp/tokens/`)
- 2slides MCP configurado para carrosséis (`~/.copilot/mcp-config.json`)
- Python + Pillow para banners locais (fallback)

## Pipeline Editorial (seguir esta ordem)

### Etapa 1 — Extrair briefing

Ler `references/brief-extractor.md` e seguir suas instruções.

Transformar o pedido bruto em briefing estruturado.

**Gate:** não avançar sem tema, conflito central e insight principal.

Perguntas obrigatórias quando faltam:
1. **Episódio real** — O que aconteceu?
2. **Conflito central** — Qual erro, custo, surpresa ou trade-off?
3. **Insight principal** — A coisa que o leitor deve lembrar
4. **Dor ampla** — Problema reconhecível além do nicho
5. **Dados concretos** — Números, métricas, resultados

### Etapa 2 — Encontrar ângulo

Ler `references/angle-finder.md` e seguir suas instruções.

Gerar **3 ângulos** e recomendar o melhor para comentários qualificados.

Avaliar cada ângulo em: defendível, experiencial e amplificável.

**Gate:** se nenhum ângulo for forte, voltar à Etapa 1.

### Etapa 3 — Decidir formato

Ler `references/format-decider.md` e seguir suas instruções.

Escolher entre texto puro, texto + banner ou carrossel.

**Gate:** justificar a escolha.

### Etapa 4 — Gerar hooks

Ler `references/hook-generator.md` e seguir suas instruções.

Consultar `references/heuristics-hooks.md` para referência.

Gerar **5 hooks** variados, ranquear e recomendar o melhor.

**Gate:** descartar hooks sem conflito, genéricos ou que começam explicando.

### Etapa 5 — Redigir o post

**Idiomas:** bilíngue PT-BR + EN (default).

**Estrutura obrigatória:**

```
[HOOK — primeira linha que para o scroll]
[CORPO — dor/conflito → insight → implicação prática]
[FECHAMENTO — takeaway + CTA respondível]
[HASHTAGS — 3 a 5]
```

**Regras:**
- Parágrafos curtos (1-3 linhas)
- Unicode bold para subtítulos (𝗦𝗲𝗰̧𝗮̃𝗼)
- → como bullet points
- Sem links externos no corpo
- Máximo **2950 caracteres**
- CTA específico e respondível

### Etapa 6 — Validar com scorecard

Ler `references/commentability-checker.md` e `references/proof-checker.md`.

Aplicar `references/post-review-scorecard.md`.

**Gates:**
- Comentabilidade >= 4/6
- Substância >= 3/5
- Formatação: todos ✅

Se reprovado: reescrever antes de apresentar.

### Etapa 7 — Se carrossel: planejar slides

Ler `references/carousel-planner.md`.

Gerar via 2slides MCP: `aspectRatio: "1:1"`, `designStyle: "modern, dark background (#0D1117), bold typography"`, `resolution: "2K"`.

Fallback: `generate-carousel.py`.

### Etapa 8 — Revisar checklist

- [ ] Hook com conflito/tensão
- [ ] Substância real (não opinião rasa)
- [ ] Autêntico (experiência vivida)
- [ ] Escaneável
- [ ] Pelo menos 1 dado concreto
- [ ] Prova pessoal presente
- [ ] Sai do nicho
- [ ] Sem links externos no corpo
- [ ] <= 2950 caracteres
- [ ] CTA gera comentário
- [ ] 3-5 hashtags relevantes

### Etapa 9 — Salvar arquivos

```
linkedin/post-{N}-{tema-slug}-pt.md
linkedin/post-{N}-{tema-slug}-en.md
```

### Etapa 10 — Gerar visual

Banner 1200x628 com Pillow ou carrossel PDF via 2slides.

Cores da série: Copilot (#1F6FEB) | CLI (#8B5CF6) | Plugins (#F97316) | Skills (#10B981) | SDK (#EC4899) | Multi-Agent (#EF4444)

### Etapa 11 — Apresentar Post Package

Entregar obrigatoriamente:
1. Post final PT-BR + EN
2. Hook alternativo
3. CTA alternativo
4. Scorecard (comentabilidade + substância)
5. Arquivos salvos
6. Horário sugerido (terça-quinta, 8h-10h BRT)
7. Comentário inicial para golden hour
8. Contagem de caracteres

### Etapa 12 — Publicar (se solicitado)

⚠️ Sempre pedir confirmação antes. Nunca publicar automaticamente.

## Anti-padrões (NUNCA fazer)

- ❌ Auto-promoção vazia
- ❌ Engagement bait com emojis
- ❌ Posts genéricos
- ❌ Começar pela feature/arquitetura
- ❌ Tema nichado sem dor ampla
- ❌ Pular etapas do pipeline
- ❌ Aprovar post com comentabilidade < 4/6

## Tom e Voz

- Profissional mas humano
- Confiante sem ser arrogante
- Específico e concreto
- Vulnerável quando relevante
- Direto ao ponto

## Estratégia Pós-Publicação

- **Golden Hour (0-60 min):** responder todos os comentários
- **24h:** continuar respondendo
- **2-4 semanas:** reciclar formato (texto → carrossel)
- **48h depois:** rodar post-mortem-analyzer

## References

- `references/brief-extractor.md`
- `references/angle-finder.md`
- `references/hook-generator.md`
- `references/commentability-checker.md`
- `references/proof-checker.md`
- `references/format-decider.md`
- `references/carousel-planner.md`
- `references/post-mortem-analyzer.md`
- `references/post-review-scorecard.md`
- `references/heuristics-hooks.md`
- `references/heuristics-ctas.md`
- `references/heuristics-patterns.md`
