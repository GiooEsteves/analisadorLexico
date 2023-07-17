import Token
import Tag

class Num(Token):
    def __init__(self, v):
        super().__init__(Tag.NUM)
        self.value = v

    def __str__(self):
        return "" + str(self.value)
