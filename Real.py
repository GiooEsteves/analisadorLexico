import Token 
import Tag

class Real(Token):
    def __init__(self, v):
        super().__init__(Tag.REAL)
        self.value = v

    def __str__(self):
        return str(self.value)
