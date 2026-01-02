🤖 Bot de WhatsApp com Python, FastAPI e Meta Cloud API
📌 Visão Geral

Este projeto consiste em um Bot de WhatsApp desenvolvido em Python, integrado à Meta Cloud API (WhatsApp Oficial), utilizando FastAPI, SQLite e Webhooks.
O sistema foi criado inicialmente como um projeto de aprendizagem, com foco em desenvolvimento web, APIs REST, integração com serviços externos e persistência de dados. Posteriormente, o projeto evoluiu e passou a ser utilizado no dia a dia de um cliente real, sendo comercializado como software funcional.

🎯 Objetivos do Projeto

Aprender e aplicar conceitos de APIs Web com FastAPI
Trabalhar com Webhooks e comunicação assíncrona
Integrar sistemas com a Meta Cloud API (WhatsApp Oficial)
Implementar lógica de bot conversacional
Persistir dados utilizando SQLite
Desenvolver um sistema utilizável em ambiente real de produção
Entregar um software funcional para um cliente final

🛠️ Tecnologias Utilizadas

Linguagem
Python (Python puro)
Framework Web
FastAPI
Banco de Dados
SQLite

Integrações

Meta Cloud API (WhatsApp Oficial)
Webhooks
Bibliotecas Externas
fastapi – Criação da API e endpoints
uvicorn – Servidor ASGI
requests – Comunicação HTTP com a Meta API
python-dateutil – Manipulação e tratamento de datas

🧠 Funcionalidades Principais

Recebimento de mensagens via Webhook do WhatsApp
Processamento de mensagens e fluxo de menus
Respostas automáticas via Meta Cloud API
Cadastro e gerenciamento de dados no SQLite
Organização da aplicação em camadas (routers, services, handlers)
Estrutura preparada para manutenção e expansão

▶️ Como Executar o Projeto

1️⃣ Clonar o repositório
git clone <https://github.com/MatheusHenry21/Gerenciador_de_TVPAGA_webhook>
cd bot-whatsapp-MatheusHenry21

2️⃣ Criar ambiente virtual
python -m venv .venv

3️⃣ Ativar o ambiente virtual

Windows
.venv\Scripts\activate


Linux / Mac
source .venv/bin/activate

4️⃣ Instalar dependências
pip install fastapi uvicorn requests python-dateutil

5️⃣ Executar a aplicação
uvicorn main:app --reload

🔐 Configurações Necessárias

Token de acesso da Meta Cloud API
ID do número de telefone do WhatsApp
URL pública configurada para recebimento do Webhook
Variáveis sensíveis configuradas via .env

📈 Status do Projeto

✅ Funcional
✅ Integrado com WhatsApp Oficial
✅ Em uso por cliente real

Matheus Henrique 👨‍💻
Desenvolvedor Python | Backend | APIs
