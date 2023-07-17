import Token
import Tag

class Word(Token):
    def __init__(self, s, tag):
        super().__init__(tag)
        self.lexeme = s

    def __str__(self):
        return self.lexeme

and_ = Word("&&", Tag.AND)
or_ = Word("||", Tag.OR)
eq = Word("==", Tag.EQ)
ne = Word("!=", Tag.NE)
le = Word("<=", Tag.LE)
ge = Word(">=", Tag.GE)
minus = Word("minus", Tag.MINUS)
True_ = Word("true", Tag.TRUE)
False_ = Word("false", Tag.FALSE)
temp = Word("t", Tag.TEMP)
