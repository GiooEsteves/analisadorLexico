from tags import *
from symbols import *

tokens = []

'''
f = open("output.txt", "r")
output = f.read()
output = output.replace("Token: ", "").strip()

for i in range(len(output)):
    if output[i].strip(): 
        tokens.append(output[i])

for i in range(len(tokens)):
    print(tokens) 
'''

def pegaLinha(linha):
    return eval(linha.replace("Token: ", "").strip())

def leTokensDoArquivo(file_path):
    tokens = []
    with open(file_path, "r") as arquivo:
        for linha in arquivo: #percorre cada linha
            if linha.strip(): #se a linha n for vazia
                tokens.append(pegaLinha(linha)) #joga o conteudo da linha na lista
    return tokens 

token_file_path = "C:/Users/gio_e/Documents/Projetos/Compiladores/compilador/analisadorLexico/output.txt"
tokens = leTokensDoArquivo(token_file_path) #dicionario lexico


for token in tokens:
    print(token) #percorre e printa cada linha do dicionario

def operador(tokens):
    for i in range(len(tokens)):
        if tokens[i]['tag'] == '=':
            print("atribuição")
        elif tokens[i]['tag'] == '>':
            print("maior que")
        elif tokens[i]['tag'] == '<':
            print("menor que")
        
operador(tokens)