def criar_token(t):
    return {"tag": t}

def token_to_str(token):
    return "" + chr(token["tag"])