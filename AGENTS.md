# Hotel Travesseiro Nervoso

## Stack
- Python, Flask, flask-cors, Agno (OpenAIChat gpt-4o-mini), python-dotenv
- Front: HTML, CSS e JS puros na pasta `static/`, servidos pelo Flask
- Sem frameworks de front, sem etapa de build
- Rodar: `python app.py` (porta 8000)

## Endpoints
- GET  /         -> devolve static/index.html
- POST /agente   -> recebe {"pergunta": "..."} e devolve {"resposta": "..."}

## Regras
- Não alterar a persona nem o texto do agente em app.py
- Não instalar dependências sem perguntar antes
- Nunca ler nem editar o arquivo .env
- Código, comentários e mensagens em português
- Antes de editar, mostrar o plano e esperar aprovação