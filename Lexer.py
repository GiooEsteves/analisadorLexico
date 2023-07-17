import io
from typing import Dict
import Word
import Real
import Num
import Token
import Tag
import symbols
import sys

class Lexer:
    line = 1
    peek = ''
    words: Dict[str, symbols.Word] = {}

    def reserve(self, w: symbols.Word):
        self.words[w.lexeme] = w

    def __init__(self):
        self.reserve(symbols.Word("if", symbols.Tag.IF))
        self.reserve(symbols.Word("else", symbols.Tag.ELSE))
        self.reserve(symbols.Word("while", symbols.Tag.WHILE))
        self.reserve(symbols.Word("do", symbols.Tag.DO))
        self.reserve(symbols.Word("break", symbols.Tag.BREAK))
        self.reserve(symbols.Word.True_)
        self.reserve(symbols.Word.False_)
        self.reserve(symbols.Word.Int_)
        self.reserve(symbols.Word.Char_)
        self.reserve(symbols.Word.Bool_)
        self.reserve(symbols.Word.Float_)

def readch():
    global peek
    peek = sys.stdin.read(1)

def readch(c):
    readch()
    if peek != c:
        return False
    peek = ''
    return True

def scan():
    while True:
        readch()
        if peek == '' or peek == '\t':
            continue
        elif peek == '\n':
            line += 1
        else:
            break

    if peek == '&':
        if readch('&'):
            return Word.and_
        else:
            return Token('&')
    elif peek == '|':
        if readch('|'):
            return Word.or_
        else:
            return Token('|')
    elif peek == '=':
        if readch('='):
            return Word.eq
        else:
            return Token('=')
    elif peek == '!':
        if readch('!'):
            return Word.ne
        else:
            return Token('!')
    elif peek == '<':
        if readch('<'):
            return Word.le
        else:
            return Token('<')
    elif peek == '>':
        if readch('>'):
            return Word.ge
        else:
            return Token('>')

    if peek.isdigit():
        v = 0
        while peek.isdigit():
            v = 10 * v + int(peek)
            readch()
        if peek != '.':
            return Num(v)
        x = float(v)
        d = 10.0
        while True:
            readch()
            if not peek.isdigit():
                break
            x = x + int(peek) / d
            d *= 10.0
        return Real(x)

    if peek.isalpha():
        b = ''
        while peek.isalnum():
            b += peek
            readch()

        s = b
        w = Word.get(s)
        if w is not None:
            return w
        w = Word(s, Tag.ID)
        Word[s] = w
        return w

    tok = Token(peek)
    peek = ''
    return tok
