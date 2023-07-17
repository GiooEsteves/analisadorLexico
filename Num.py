from Token import criar_token
from Tag import tags

def criar_num(v):
    num = criar_token(tags["NUM"])
    num["value"] = v
    return num

def num_to_str(num):
    return "" + str(num["value"])
