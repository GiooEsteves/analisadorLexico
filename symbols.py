from typing import Optional
import Lexer

class Env:
    def __init__(self, n: Optional['Env'] = None):
        self.table = {}
        self.prev = n

    def put(self, w: Lexer.Token, i: Lexer.Id):
        self.table[w] = i

    def get(self, w: Lexer.Token) -> Optional[Lexer.Id]:
        e = self
        while e is not None:
            found = e.table.get(w)
            if found is not None:
                return found
            e = e.prev
        return None

class Type(Lexer.Word):
    def __init__(self, s, tag, w):
        super().__init__(s, tag)
        self.width = w

        Int = Type("int", Lexer.Tag.BASIC, 4)
        Float = Type("float", Lexer.Tag.BASIC, 8)
        Char = Type("char", Lexer.Tag.BASIC, 1)
        Bool = Type("bool", Lexer.Tag.BASIC, 1)

    @staticmethod
    def numeric(p):
        if p == Type.Char or p == Type.Int or p == Type.Float:
            return True
        else:
            return False

    @staticmethod
    def max(p1, p2):
        if not Type.numeric(p1) or not Type.numeric(p2):
            return None
        elif p1 == Type.Float or p2 == Type.Float:
            return Type.Float
        elif p1 == Type.Int or p2 == Type.Int:
            return Type.Int
        else:
            return Type.Char
