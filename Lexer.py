import sys

tags = {
    "AND": 256,
    "BASIC": 257,
    "BREAK": 258,
    "DO": 259,
    "ELSE": 260,
    "EQ": 261,
    "FALSE": 262,
    "GE": 263,
    "ID": 264,
    "IF": 265,
    "INDEX": 266,
    "LE": 267,
    "MINUS": 268,
    "NE": 269,
    "NUM": 270,
    "OR": 271,
    "REAL": 272,
    "TEMP": 273,
    "TRUE": 274,
    "WHILE": 275,
}

def Token(tag):
    return chr(tag)

def Num(value):
    return Token(tags["NUM"]) + str(value)

def Word(lexeme, tag):
    return Token(tag) + lexeme

and_word = Word("&&", tags["AND"])
or_word = Word("||", tags["OR"])
eq_word = Word("==", tags["EQ"])
ne_word = Word("!=", tags["NE"])
le_word = Word("<=", tags["LE"])
ge_word = Word(">=", tags["GE"])
minus_word = Word("minus", tags["MINUS"])
true_word = Word("true", tags["TRUE"])
false_word = Word("false", tags["FALSE"])
temp_word = Word("t", tags["TEMP"])

def Real(value):
    return Token(tags["REAL"]) + str(value)

line = 1
peek = ' '

words = {
    "if": tags["IF"],
    "else": tags["ELSE"],
    "while": tags["WHILE"],
    "do": tags["DO"],
    "break": tags["BREAK"],
    "true": tags["TRUE"],
    "false": tags["FALSE"],
    "int": tags["BASIC"],
    "char": tags["BASIC"],
    "bool": tags["BASIC"],
    "float": tags["BASIC"],
}

def readch():
    global peek
    peek = sys.stdin.read(1)

def readch_check(c):
    global peek
    readch()
    if peek != c:
        return False
    peek = ' '
    return True

def scan():
    global line, peek

    while peek == ' ' or peek == '\t' or peek == '\n':
        if peek == '\n':
            line = line + 1
        readch()

    if peek.isalpha():
        token = ""
        while peek.isalnum():
            token += peek
            readch()
        token_tag = words.get(token, tags["ID"])
        return Token(token_tag)

    if peek == '&':
        if readch_check('&'):
            return and_word
        else:
            return Token(ord('&'))

    if peek == '|':
        if readch_check('|'):
            return or_word
        else:
            return Token(ord('|'))

    if peek == '=':
        if readch_check('='):
            return eq_word
        else:
            return Token(ord('='))

    if peek == '!':
        if readch_check('!'):
            return ne_word
        else:
            return Token(ord('!'))

    if peek == '<':
        if readch_check('<'):
            return le_word
        else:
            return Token(ord('<'))

    if peek == '>':
        if readch_check('>'):
            return ge_word
        else:
            return Token(ord('>'))

    if peek.isdigit():
        token = ""
        while peek.isdigit():
            token += peek
            readch()
        if peek != '.':
            return Num(int(token))
        token += peek
        readch()
        while peek.isdigit():
            token += peek
            readch()
        return Real(float(token))

    token = peek
    peek = ' '
    return Token(ord(token))