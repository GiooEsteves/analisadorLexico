import Word
import Real
import Num
import Token
import Tag
import sys

words = {
    "if": Word.Word("if", Tag.Tag.IF),
    "else": Word.Word("else", Tag.Tag.ELSE),
    "while": Word.Word("while", Tag.Tag.WHILE),
    "do": Word.Word("do", Tag.Tag.DO),
    "break": Word.Word("break", Tag.Tag.BREAK),
    "True": Word.True_,
    "False": Word.False_,
    "int": Word.Word("int", Tag.Tag.INT),
    "char": Word.Word("char", Tag.Tag.CHAR),
    "bool": Word.Word("bool", Tag.Tag.BOOL),
    "float": Word.Word("float", Tag.Tag.FLOAT)
}

def readch():
    global peek 
    peek = sys.stdin.read(1)
    return peek

def readch_if(c):
    readch()
    if peek != c:
        return False
    else: 
        return True

def skip_whitespace():
    while True:
        readch()
        if peek == '' or peek == '\t':
            continue
        elif peek == '\n':
            line += 1
        else:
            break

def scan():
    while True:
        skip_whitespace()

        if peek == '&':
            if readch_if('&'):
                return words.get("&&", Token.Token('&'))
            else:
                return Token.Token('&')
        elif peek == '|':
            if readch_if('|'):
                return words.get("||", Token.Token('|'))
            else:
                return Token.Token('|')
        elif peek == '=':
            if readch_if('='):
                return words.get("==", Token.Token('='))
            else:
                return Token.Token('=')
        elif peek == '!':
            if readch_if('!'):
                return words.get("!=", Token.Token('!'))
            else:
                return Token.Token('!')
        elif peek == '<':
            if readch_if('<'):
                return words.get("<=", Token.Token('<'))
            else:
                return Token.Token('<')
        elif peek == '>':
            if readch_if('>'):
                return words.get(">=", Token.Token('>'))
            else:
                return Token.Token('>')

        if peek.isdigit():
            v = 0
            while peek.isdigit():
                v = 10 * v + int(peek)
                readch()
            if peek != '.':
                return Num.Num(v)
            x = float(v)
            d = 10.0
            while True:
                readch()
                if not peek.isdigit():
                    break
                x = x + int(peek) / d
                d *= 10.0
            return Real.Real(x)

        if peek.isalpha():
            s = ''
            while peek.isalnum():
                s += peek
                readch()

            w = words.get(s)
            if w is not None:
                return w
            w = Word.Word(s, Tag.Tag.ID)
            words[s] = w
            return w

        tok = Token.Token(peek)
        readch()
        return tok