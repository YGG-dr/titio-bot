🧭 CHECKLIST PRÉ-CODING — titio-bot

🧱 1️⃣ Fundamentos do projeto

[x] Nome do projeto ✓

[x] Stack definida (Node / Python / Rust) ✓

[x] Papéis claros por linguagem ✓

[x] Estrutura de pastas macro ✓

[x] .env como fonte única de config ✓



---

📜 2️⃣ Políticas de código (code policy)

[x] .editorconfig (indentação 4 espaços) ✓

[x] .gitignore padronizado ✓

[x] Formatter manda, dev obedece ✓

[x] Lint obrigatório (Node / Python / Rust) ✓

[x] Definir versão mínima de cada linguagem ✓

[x] Definir padrão de nomes (files, vars, services) ✓



---

🧰 3️⃣ Tooling por linguagem (sem instalar ainda) 

Node

[x] ESLint v9 ✓

[x] Prettier ✓

[ ] Regras específicas pra Discord.js


Python

[x] Ruff (planejado) ✓

[x] Black (planejado) ✓

[ ] Versão alvo do Python (ex: 3.11)


Rust

[ ] rustfmt

[ ] clippy

[ ] Edição do Rust (2021 ou 2024)



---

🐳 4️⃣ Docker & ambiente

[x] Usar Docker desde o início ✓

[x] Um serviço por linguagem ✓

[x] .env compartilhado ✓

[ ] Decidir base images (node, python, rust)

[ ] Definir se Rust gera binário ou roda como serviço

[ ] Política de volumes (ou ausência deles)



---

🔌 5️⃣ Comunicação entre serviços

[x] Node ↔ Python → HTTP interno ✓

[x] Node/Python ↔ Rust → binário local ✓

[ ] Definir formato de payload (JSON / msgpack)

[ ] Definir timeouts e retries

[ ] Definir contratos (schemas)



---

🔐 6️⃣ Segurança & higiene

[x] Nada de config hardcoded ✓

[x] Secrets só via env ✓

[x] Política de logs (níveis, redaction) ✓

[x] Política de erros (stacktrace sim/não) ✓



---

🧪 7️⃣ Qualidade & confiabilidade

[ ] Estratégia de testes (unit / integration)

[ ] Onde entram os testes (pastas)

[ ] Lint/test como gate de commit ou CI



---

🚀 8️⃣ CI / automação (conceito)

[ ] Rodar lint automaticamente

[ ] Rodar tests automaticamente

[ ] Build Docker validando tudo

[ ] Bloquear merge se falhar


---

📚 9️⃣ Documentação mínima

[x] README existe ✓

[x] README: visão geral ✓

[x] README: como rodar local ✓

[x] README: variáveis de ambiente ✓
