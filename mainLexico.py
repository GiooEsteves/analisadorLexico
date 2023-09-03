from symbols import *
from setID import setID

token = []
lexema = ""

f = open(r"example.txt", mode='r', encoding="utf-8")
input_code = f.read()
input_code = input_code.replace("\t", '').replace('\n', r'\n ')

def scan(lexema):
    for i in range(len(input_code)):
        if input_code[i] != " ":
            if i + 1 < len(input_code) and input_code[i] in letters:
                if input_code[i - 1] + input_code[i] == r'\n':
                    lexema = ''
                else:
                    lexema += input_code[i]
                if input_code[i+1] not in letters:
                    token.append(lexema)
                    lexema = ''
            if i + 1 < len(input_code) and input_code[i] in symbols:
                token.append(input_code[i])
                lexema = ''

            if (i + 1 < len(input_code) and input_code[i] in onlyoperators and input_code[i + 1] not in onlyoperators
                and input_code[i - 1] not in onlyoperators):
                token.append(input_code[i])
                lexema = ''

            if i + 1 < len(input_code) and input_code[i] + input_code[i - 1] in multioperators:
                token.append(input_code[i] + input_code[i - 1])
                lexema = ''

            if i + 1 < len(input_code) and input_code[i] + input_code[i + 1] in multioperators:
                token.append(input_code[i] + input_code[i + 1])
                lexema = ''
            if i + 1 < len(input_code) and input_code[i] in numbers:
                lexema += input_code[i]
                if input_code[i + 1] not in numbers:
                    token.append(lexema)
                    lexema = ''

def show(token):
    file_output = open("output.txt", "w")
    for i in range(len(token)):
        if token[i] != " ":
            output = setID(token[i])
            file_output.write(output + "\n")



scan(lexema)
show(token)
