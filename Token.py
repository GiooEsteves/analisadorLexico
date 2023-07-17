def criar_token(t):
    return {"tag": t}

def to_string(token):
    return "" + chr(token["tag"])

# Exemplo de uso:
# meu_token = criar_token(65)
# print(to_string(meu_token))  # Saída: "A"