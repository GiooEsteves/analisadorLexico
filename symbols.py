import string

symbols = ['{', '}', '(', ')', '[', ']', ';', ':', '%', '&']
onlyoperators = ['=', '+', '-', '>', '<']
multioperators = ['>=', '==', '<=', '!=', '&&', '||']
reservedwords = ['while', 'do', 'break', 'if', 'true', 'false', 'float', 'int', 'char', 'bool', 'and', 'or', 'not']
letters = list(string.ascii_lowercase + string.ascii_uppercase)
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
