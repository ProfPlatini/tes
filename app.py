from flask import Flask,jsonify,request,send_from_directory
from flask_cors import CORS
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from dotenv import load_dotenv
import os 
from supabase import create_client

load_dotenv()
supabase = create_client(os.getenv("SUPABASE_URL"),os.getenv("SUPABASE_KEY"))

app = Flask(__name__)
CORS(app)

agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description="Você é um agente virtual do Hotel Travesseiro Nervoso, slogan: Aqui até a insônia dorme"
    "Você responde de forma clara e humorada, informações sobre quartos,serviços, reservas e preços"
    "Quarto Standard ($500), Quarto Deluxe ($700), Quarto Suíte Presidencial ($1000)"
    "Serviços oferecidos: Academia, Café da Manhã, Lavanderia, Restaurante, Piscina"
    "Não inclua icones em markdown nas respostas, como: ##, **",
    markdown=False
)

@app.route("/",methods=['GET'])
def pagina_inicial():
    return send_from_directory('static', 'index.html')

@app.route("/agente",methods=['POST'])
def retorno():
    dados = request.get_json()
    pergunta = dados['pergunta']
    resposta = agente.run(pergunta)
    return jsonify({"resposta":resposta.content})

@app.route("/reservas",methods=['POST'])
def reservar():
    dados = request.get_json()
    supabase.table("reservas").insert(dados).execute()
    return jsonify({"mensagem":"Dados inseridos com sucesso!"})

@app.route("/reservas", methods=['GET'])
def listar():
    resultado = supabase.table("reservas").select("*").execute()
    return jsonify(resultado.data)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000)