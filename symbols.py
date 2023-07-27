from Lexer import tags

def Env(prev):
    return {"table": {}, "prev": prev}

def put(env, w, i):
    env["table"][w] = i

def get(env, w):
    while env is not None:
        if w in env["table"]:
            return env["table"][w]
        env = env["prev"]
    return None

def Type(s, tag, w):
    return {"lexeme": s, "tag": tag, "width": w}

Int = Type("int", tags["BASIC"], 4)
Float = Type("float", tags["BASIC"], 8)
Char = Type("char", tags["BASIC"], 1)
Bool = Type("bool", tags["BASIC"], 1)

def numeric(p):
    return p in [Char, Int, Float]

def max_type(p1, p2):
    if not numeric(p1) or not numeric(p2):
        return None
    elif p1 == Float or p2 == Float:
        return Float
    elif p1 == Int or p2 == Int:
        return Int
    else:
        return None

def Array(sz, p):
    return {"lexeme": "[]", "tag": tags["INDEX"], "width": sz * p["width"], "size": sz, "of": p}

def array_to_string(arr):
    return f"[{arr['size']}]{arr['of']['lexeme']}"