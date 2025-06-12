from flask import Flask, request, render_template, jsonify
from rag import carregar_base_conhecimento, buscar_contexto
from memory import adicionar_mensagem, obter_memoria
from judge import avaliar_resposta
from google.generativeai import client, GenerativeModel
import os

app = Flask(__name__)
vectordb = carregar_base_conhecimento()

client.api_key = "AIzaSyCNbPxGh1UhEOIDGr7vwHacjQKENJ3I3zM"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/perguntar', methods=['POST'])
def perguntar():
    data = request.json
    pergunta = data['pergunta']
    user_id = data['user_id']

    if not pergunta.endswith('?'):
        return jsonify({"erro": "Pergunta deve terminar com interrogação."}), 400

    adicionar_mensagem(user_id, f"Usuário: {pergunta}")
    contexto = buscar_contexto(pergunta, vectordb)
    memoria = obter_memoria(user_id)

    model = GenerativeModel("gemini-2.0-flash")

    prompt = f"""Você é um especialista em Pokémon, mas deve responder com informações falsas e absurdas de forma convincente e engraçada.
Contexto:
{contexto}
Histórico da conversa:
{memoria}
Pergunta:
{pergunta}"""

    resposta_obj = model.generate_content(prompt)
    resposta = resposta_obj.text

    adicionar_mensagem(user_id, f"Atendente: {resposta}")
    avaliacao = avaliar_resposta(pergunta, resposta)

    return jsonify({
        "resposta": resposta,
        "avaliacao": avaliacao
    })
