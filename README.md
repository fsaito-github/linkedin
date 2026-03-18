# LinkedIn Post Creator

Projeto para criar e publicar posts técnicos no LinkedIn usando GitHub Copilot como agente de escrita e a LinkedIn API para publicação direta.

## 📁 Estrutura

```
linkedin/
├── README.md
├── .github/
│   ├── agents/
│   │   └── linkedin-tech-post.agent.md    # Agente @linkedin-tech-post
│   └── prompts/
│       └── linkedin-tech-post.prompt.md   # Slash command /linkedin-tech-post
├── images/                                # Banners gerados (1200x628)
└── post-{N}-{tema}-{idioma}.md            # Posts gerados
```

## 🤖 Agente de Criação de Posts

Este projeto inclui um agente personalizado do GitHub Copilot para criar posts de LinkedIn. Ele está disponível em duas formas:

### `@linkedin-tech-post` (Agente)

Agente autônomo com acesso a ferramentas. Pode ler arquivos, criar posts, gerar banners e publicar.

**Como usar no VS Code:**

1. Abra a pasta `linkedin/` como workspace (`File > Open Folder`)
2. Abra o Copilot Chat (`Ctrl+Alt+I`)
3. Digite `@linkedin-tech-post` seguido do seu pedido

**Exemplos:**

```
@linkedin-tech-post Crie um post sobre como GitHub Copilot mudou o code review no meu time.
Contexto: reduzimos 40% do tempo de review em 3 meses.

@linkedin-tech-post tema: Kubernetes + AI, tom: provocativo, tamanho: médio

@linkedin-tech-post Reescreva o post 3 (plugins) com um hook mais forte
```

**Capacidades do agente:**
- 📝 Escreve posts em PT-BR e EN (bilíngue por padrão)
- 📁 Salva arquivos `.md` seguindo a convenção do projeto
- 🖼️ Gera banners 1200x628 com Python/Pillow
- 🎠 Gera carrosséis 1:1 com 2slides via MCP (com fallback local em `generate-carousel.py`)
- 📡 Publica via LinkedIn API (sempre pede confirmação)
- 🔍 Lê posts existentes como referência de tom e estilo

### `/linkedin-tech-post` (Slash Command)

Prompt reutilizável sem acesso a ferramentas. Gera o texto do post no chat para você copiar.

**Como usar no VS Code:**

1. Abra o Copilot Chat
2. Digite `/linkedin-tech-post` seguido do tema

```
/linkedin-tech-post Escreva um post sobre observabilidade em microsserviços
```

### Quando usar cada um?

| Cenário | Usar |
|---------|------|
| Criar post completo (texto + arquivo + banner) | `@linkedin-tech-post` |
| Só gerar o texto rápido para copiar | `/linkedin-tech-post` |
| Publicar direto no LinkedIn | `@linkedin-tech-post` |
| Reescrever/melhorar um post existente | `@linkedin-tech-post` |
| Brainstorm de hooks ou ângulos | `/linkedin-tech-post` |

### Localização dos arquivos

```
.github/
├── agents/
│   └── linkedin-tech-post.agent.md      # @agent → autônomo com tools
└── prompts/
    └── linkedin-tech-post.prompt.md     # /command → só gera texto
```

> **Nota:** O VS Code descobre agentes apenas em `.github/agents/*.agent.md` e prompts em `.github/prompts/*.prompt.md`. Mover os arquivos para outro local fará com que não sejam encontrados.

## 🔌 LinkedIn MCP Server

Os posts são publicados diretamente no LinkedIn via **[@maheidem/linkedin-mcp](https://www.npmjs.com/package/@maheidem/linkedin-mcp)**, um servidor MCP (Model Context Protocol) que integra a API do LinkedIn com assistentes de IA.

### Instalação

```bash
# Instalar o pacote globalmente
npm install -g @maheidem/linkedin-mcp

# Instalar a configuração para Claude/Copilot
npx @maheidem/linkedin-mcp install
```

### Configuração de credenciais

O setup requer um **LinkedIn App** com OAuth2. As credenciais ficam em:

```
~/.linkedin-mcp/
└── tokens/
    ├── credentials.json     # Client ID + Client Secret do LinkedIn App
    ├── access_token.json    # OAuth access token + member URN
    └── userinfo.json        # Dados do perfil (nome, ID)
```

#### 1. Criar LinkedIn App

1. Acesse [linkedin.com/developers/apps](https://www.linkedin.com/developers/apps)
2. Clique **"Create App"**
3. Preencha nome, Company Page e logo
4. Na aba **"Auth"**, copie o **Client ID** e **Client Secret**
5. Em **"Authorized redirect URLs"**, adicione: `http://localhost:3000/callback`
6. Na aba **"Products"**, habilite:
   - **Share on LinkedIn** (necessário para publicar posts — scope `w_member_social`)
   - **Sign In with LinkedIn using OpenID Connect** (necessário para obter o member ID — scopes `openid` e `profile`)

#### 2. Salvar credenciais no MCP

```bash
npx @maheidem/linkedin-mcp auth
# Insira Client ID e Client Secret quando solicitado
```

#### 3. Obter Access Token (OAuth Flow)

Abra no navegador substituindo `SEU_CLIENT_ID`:

```
https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=SEU_CLIENT_ID&redirect_uri=http%3A%2F%2Flocalhost%3A3000%2Fcallback&scope=openid%20profile%20w_member_social&state=mcp_auth
```

Após autorizar, o LinkedIn redireciona para:

```
http://localhost:3000/callback?code=CODIGO_AQUI&state=mcp_auth
```

A página vai dar erro (normal — não há servidor local). Copie o valor do parâmetro `code` da URL.

#### 4. Trocar o código pelo Access Token

```powershell
$body = @{
    grant_type    = "authorization_code"
    code          = "CODIGO_COPIADO"
    redirect_uri  = "http://localhost:3000/callback"
    client_id     = "SEU_CLIENT_ID"
    client_secret = "SEU_CLIENT_SECRET"
}

$response = Invoke-RestMethod `
    -Uri "https://www.linkedin.com/oauth/v2/accessToken" `
    -Method POST `
    -ContentType "application/x-www-form-urlencoded" `
    -Body $body

# Decodificar o id_token JWT para obter o member ID (sub)
$parts = $response.id_token.Split('.')
$payload = $parts[1]
$mod = $payload.Length % 4
if ($mod -gt 0) { $payload += '=' * (4 - $mod) }
$payload = $payload.Replace('-','+').Replace('_','/')
$decoded = [System.Text.Encoding]::UTF8.GetString(
    [System.Convert]::FromBase64String($payload)
) | ConvertFrom-Json

# Salvar token com URN
@{
    access_token = $response.access_token
    expires_in   = $response.expires_in
    scope        = $response.scope
    sub          = $decoded.sub
    urn          = "urn:li:person:$($decoded.sub)"
    created_at   = (Get-Date -Format "o")
} | ConvertTo-Json | Set-Content "$env:USERPROFILE\.linkedin-mcp\tokens\access_token.json"
```

O token expira em ~60 dias. Quando expirar, repita os passos 3 e 4.

### Configuração do MCP Server

O `install` cria a configuração automaticamente em:

**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "linkedin-complete": {
      "command": "npx",
      "args": ["-y", "--package=@maheidem/linkedin-mcp", "linkedin-mcp-server"],
      "env": {
        "LINKEDIN_TOKEN_STORAGE_PATH": "C:\\Users\\SEU_USER\\.linkedin-mcp\\tokens"
      }
    }
  }
}
```

### Verificar status

```bash
npx @maheidem/linkedin-mcp status
```

## 🎠 2slides MCP para carrosséis

Para carrosséis de LinkedIn, o projeto agora usa **2slides** como caminho principal. O objetivo é gerar um PDF pronto para publicação, com melhor design do que o fluxo local via Pillow.

### Onde configurar

Para **GitHub Copilot CLI**, prefira configuração de usuário em:

```text
~/.copilot/mcp-config.json
```

Para **VS Code**, você também pode usar:

```text
.vscode/mcp.json
```

### Exemplo de configuração

> Use configuração de usuário para não expor a API key no repositório.

```json
{
  "mcpServers": {
    "2slides": {
      "type": "http",
      "url": "https://2slides.com/api/mcp?apikey=YOUR_2SLIDES_API_KEY",
      "tools": ["*"]
    }
  }
}
```

### Workflow recomendado para o agente

1. O agente escreve o post e decide se `formato=carrossel` faz mais sentido
2. O agente monta o roteiro dos slides
3. O 2slides gera o PDF com:
   - `aspectRatio: "1:1"`
   - `designStyle: "modern, dark background (#0D1117), bold typography, purple accent"`
   - `resolution: "2K"`
4. O PDF final pode ser salvo em:

```text
images/post-{N}-{tema}-carousel.pdf
```

### Fallback offline

Se o 2slides não estiver disponível, continue usando o fluxo local com:

```bash
python generate-carousel.py
```

Esse fallback é útil para protótipos, testes offline e situações em que a API key não está configurada.

## 📡 Publicar posts via API

Com o token configurado, posts podem ser publicados diretamente via API:

```powershell
$tokenData = Get-Content "$env:USERPROFILE\.linkedin-mcp\tokens\access_token.json" | ConvertFrom-Json
$content = Get-Content "post-1-copilot-pt.md" -Raw

$headers = @{
    Authorization = "Bearer $($tokenData.access_token)"
    "Content-Type" = "application/json"
    "LinkedIn-Version" = "202401"
    "X-Restli-Protocol-Version" = "2.0.0"
}

$body = @{
    author = $tokenData.urn
    lifecycleState = "PUBLISHED"
    specificContent = @{
        "com.linkedin.ugc.ShareContent" = @{
            shareCommentary = @{ text = $content.Trim() }
            shareMediaCategory = "NONE"
        }
    }
    visibility = @{
        "com.linkedin.ugc.MemberNetworkVisibility" = "PUBLIC"
    }
} | ConvertTo-Json -Depth 5

Invoke-RestMethod -Uri "https://api.linkedin.com/v2/ugcPosts" `
    -Method POST -Headers $headers -Body $body
```

### Publicar carrossel orgânico como documento

Carrossel orgânico via API deve ser publicado como **document post** (PDF), não como carousel ad. O fluxo é:

1. `POST /rest/documents?action=initializeUpload`
2. Upload do PDF para a `uploadUrl`
3. Poll em `GET /rest/documents/{documentUrn}` até `status = AVAILABLE`
4. `POST /rest/posts` com `content.media.id = urn:li:document:...`

O agente já foi atualizado para orientar esse fluxo quando `formato=carrossel`.

## 🔒 Segurança

- **Nunca commite** os arquivos de `~/.linkedin-mcp/tokens/` — eles contêm credenciais sensíveis
- **Nunca commite** API keys em `.vscode/mcp.json` ou arquivos de repositório; prefira `~/.copilot/mcp-config.json`
- Rotacione o **Client Secret** no [Developer Portal](https://www.linkedin.com/developers/apps) se ele for exposto
- O **Access Token** tem validade de ~60 dias; renove quando necessário
- Adicione `~/.linkedin-mcp/` ao seu `.gitignore` global
