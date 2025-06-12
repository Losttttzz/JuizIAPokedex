from google.generativeai import client, GenerativeModel
import os

def avaliar_resposta(pergunta, resposta):
    client.api_key = os.getenv("GEMINI_API_KEY")
    model = GenerativeModel("gemini-2.0-flash")

    prompt = f"""Você é um juiz de IA. Avalie a resposta do atendente com base na pergunta feita.
Pergunta: {pergunta}
Resposta do atendente: {resposta}

A resposta está correta com base em conhecimento real sobre Pokémon? Responda com 'Sim' ou 'Não' e justifique."""
    result = model.generate_content(prompt)
    return result.text