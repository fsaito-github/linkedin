# High-Signal Patterns

Heurísticas extraídas de posts publicados e seus resultados reais. Este arquivo é a memória editorial do projeto.

## Como usar este arquivo

- Ler antes de criar um novo post para lembrar o que funciona
- Atualizar após cada post-mortem (usando `post-mortem-analyzer`)
- Cada heurística deve ter: origem, evidência e ação sugerida

## Heurísticas ativas

### H001 — Ferramenta + medo organizacional = comentários qualificados
- **Origem:** Post #3 (Advisor) + comentário recebido sobre "blast radius"
- **Evidência:** Comentário "nobody wants to own the blast radius in a live environment" — resposta direta à tensão organizacional do post
- **Ação:** Quando o tema for uma ferramenta/feature, conectar com o medo organizacional que impede adoção (ownership, risco, responsabilidade, blast radius)

### H002 — "O que acontece quando você faz" > "O que fazer"
- **Origem:** Post #3 (Advisor) — insight central do post
- **Evidência:** A tese "Advisor diz o que fazer, mas não o que acontece quando você faz" gerou identificação imediata
- **Ação:** Priorizar posts que revelem consequências de ações, não apenas recomendações

### H003 — Dados em tabela = credibilidade visual
- **Origem:** Post #3 — tabela de impacto por serviço
- **Evidência:** A tabela com status durante/após/auto-recupera adiciona concretude visual ao post
- **Ação:** Quando possível, incluir pelo menos 1 tabela ou comparação estruturada no corpo do post

## Template para novas heurísticas

```
### HXXX — [título curto]
- **Origem:** Post #[N] ([tema]) + [contexto]
- **Evidência:** [o que foi observado]
- **Ação:** [o que fazer diferente nos próximos posts]
```

> Este arquivo cresce com o tempo. Cada post-mortem deve adicionar pelo menos 1 heurística nova.
