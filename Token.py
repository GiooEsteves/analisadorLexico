def criar_token(t):
    return {"tag": t}

def to_string(token):
    return "" + chr(token["tag"])
