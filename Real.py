from Token import criar_token
from Tag import tags

def criar_real(v):
    real = criar_token(tags["REAL"])
    real["value"] = v
    return real

def real_to_str(real):
    return str(real["value"])
