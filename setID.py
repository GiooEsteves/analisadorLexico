from tags import *
from symbols import *

def setID(token):
    if token in symbols:
        return "Token: " + "{" + f"'tag': {tags['letters']['tag']}, 'lexeme': '{token}'" + "}"
    if token in onlyoperators and token != "=" and token != "<" and token != ">":
        return "Token: " + "{" + f"'tag': {tags['onlyoperators']['tag']}, 'lexeme': '{token}'" + "}"
    if token in multioperators:
        return "Token: " + "{" + f"'tag': {tags['multioperators']['tag']}, 'lexeme': '{token}'" + "}"
    if token.isdigit():
        return "Token: " + "{" + f"'tag': {tags['value']['tag']}, 'value': '{token}'" + "}"
    if token in letters:
        return "Token: " + "{" + f"'tag': {tags['letters']['tag']}, 'lexeme': '{token}'" + "}"

    for key in tags.keys():
        if token in reservedwords:
            if token == key and token != 'and' and token != 'or':
                return f"Token: {tags[key]}"
            if token == key and token == 'and':
                return "Token: " + "{" + f"'tag': {tags[key]['tag']}, 'lexeme': '&&'" + "}"
            if token == key and token == 'or':
                return "Token: " + "{" + f"'tag': {tags[key]['tag']}, 'lexeme': '||'" + "}"

        if token == "=":
            return f"Token: {tags['eq']}"
        if token == "<":
            return f"Token: {tags['le']}"
        if token == ">":
            return f"Token: {tags['bg']}"

    return ""
