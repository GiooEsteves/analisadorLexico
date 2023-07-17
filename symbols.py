import Lexer

def criar_env(n):
    return {
        "table": {},
        "prev": n
    }

def put(env, w, i):
    env["table"][w] = i

def get(env, w):
    e = env
    while e is not None:
        found = e["table"].get(w)
        if found is not None:
            return found
        e = e["prev"]
    return None

types = {
    "int": 4,
    "float": 8,
    "char": 1,
    "bool": 1
}

def is_numeric(p):
    return p in types

def max_type(p1, p2):
    if not is_numeric(p1) or not is_numeric(p2):
        return None
    elif p1 == "float" or p2 == "float":
        return "float"
    elif p1 == "int" or p2 == "int":
        return "int"
    else:
        return "char"

def criar_array(sz, p):
    array = {
        "lexeme": "[]",
        "tag": Lexer.Tag.INDEX,
        "width": sz * p["width"],
        "size": sz,
        "of": p
    }
    return array

def array_to_str(array):
    return f"[{array['size']}]{array['of']}"