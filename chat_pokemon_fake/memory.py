conversas = {}

def adicionar_mensagem(user_id, mensagem):
    if user_id not in conversas:
        conversas[user_id] = []
    conversas[user_id].append(mensagem)

def obter_memoria(user_id):
    return "\n".join(conversas.get(user_id, []))