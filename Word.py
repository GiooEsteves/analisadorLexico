from Token import criar_token
from Tag import tags

def criar_word(s, tag):
    word = criar_token(tag)
    word["lexeme"] = s
    return word

def word_to_str(word):
    return word["lexeme"]

and_ = criar_word("&&", tags["AND"])
or_ = criar_word("||", tags["OR"])
eq = criar_word("==", tags["EQ"])
ne = criar_word("!=", tags["NE"])
le = criar_word("<=", tags["LE"])
ge = criar_word(">=", tags["GE"])
minus = criar_word("minus", tags["MINUS"])
True_ = criar_word("true", tags["TRUE"])
False_ = criar_word("false", tags["FALSE"])
temp = criar_word("t", tags["TEMP"])