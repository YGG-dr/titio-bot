<div align="center">

<img src="https://nodejs.org/static/images/logo.svg" height="90" alt="Node.js logo" />

# **titio-bot**

Um bot modular, extensível e orientado a boas práticas —  
pensado para crescer sem virar caos.

</div>

---

## ✨ Visão geral

**titio-bot** é um projeto de bot com foco em **arquitetura limpa**, **políticas claras** e **higiene de código**.  
Ele nasce simples, mas preparado para evoluir com segurança, observabilidade e disciplina técnica.

O projeto não assume apenas uma stack eterna:  
ele define **padrões**, não amarras.

---

## 🧠 Filosofia

- Código > framework
- Ferramentas ajudam, não mandam
- Configuração explícita é melhor que mágica
- Escalável desde o primeiro commit

---

## 🧱 Estrutura (alto nível)

```text
.
├── node/          # Núcleo principal (Node.js)
├── python/        # Serviços auxiliares / automações
├── docker/        # Infra & runtime
├── .editorconfig  # Política de estilo global
├── .gitignore     # Higiene de repositório
└── README.md

> Novas linguagens ou serviços seguem o mesmo padrão estrutural.




---

🔐 Segurança & higiene

Nenhuma configuração sensível hardcoded

Secrets exclusivamente via variáveis de ambiente

Logs com níveis bem definidos

Redaction obrigatória para dados sensíveis

Erros controlados (stacktrace só quando faz sentido)



---

📜 Políticas de código

Indentação padronizada (4 espaços)

Formatter é autoridade final

Lint obrigatório por linguagem

Convenções de nomes consistentes:

arquivos: kebab-case

classes: PascalCase

variáveis/funções: camelCase


Código deve ser legível antes de ser inteligente



---

🧰 Tooling (atual)

Node.js (core)

ESLint v9 (flat config)

Prettier

Regras pensadas para projetos reais (não demo)


> Python, Rust e outros entram com o mesmo nível de rigor.




---

⚙️ Variáveis de ambiente

Cada serviço possui seu próprio .env.example.

Exemplo genérico:

APP_ENV=development
LOG_LEVEL=info
SERVICE_TOKEN=changeme

Nunca versione .env real.


---

▶️ Rodando localmente (visão geral)

# Node
cd node
npm install
npm run dev

Detalhes específicos ficam documentados por serviço.


---

🚧 Status

Projeto em construção consciente.
Nada é apressado. Nada é improvisado.


---

📄 Licença

MIT — faça bom uso, mas faça direito.
