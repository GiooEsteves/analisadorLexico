from tags import *
from symbols import *

def pega_linha(linha):
    return eval(linha.replace("Token: ", "").strip())

tokens = []
with open("output.txt", "r") as arquivo:
    for linha in arquivo:
        if linha.strip():
            tokens.append(pega_linha(linha))

def match(tag_esperada):
    global token_atual
    if token_atual['tag'] == tag_esperada:
        token_atual = tokens.pop(0)
    else:
        print(f"Erro de sintaxe: esperado tag:'{tag_esperada}', encontrado tag:'{token_atual['tag']}'")

def estrutura_basica():
    global token_atual
    print("estrutura basica")
    if token_atual['lexeme'] == '{':
        match(264)
        confirmacao()
    if token_atual['tag'] == 264 and token_atual['lexeme'] == '}':
        match(264)
            
def cochetes():
    coch = []
    coch = token_atual['lexeme']
    match(264)
    if token_atual['tag'] == 264 and token_atual['lexeme'] in letters:
        coch = coch + token_atual['lexeme']
        match(264)
    if token_atual['tag'] == 270:   #numero 
        coch = coch + token_atual['value']
        match(270)
        if token_atual['tag'] == 264:   # ']'
            coch = coch + token_atual['lexeme']
            match(264)
            return coch
    elif token_atual['tag'] == 264 and token_atual['lexeme'] in letters:     # variavel
        coch = coch + token_atual['lexeme']
        match(264)
        if token_atual['tag'] == 264:   # ']'
            coch = coch + token_atual['lexeme']
            match(264)
            
            return coch

def confirmacao():
    tag_numbers = [value['tag'] for value in tags.values()]
    '''print(token_atual['tag'])
    print(token_atual['lexeme'])'''
    
    while token_atual['tag'] in tag_numbers:
        if token_atual['tag'] == 257:  # tipo
            declaracao()
        elif token_atual['tag'] == 264 and token_atual['lexeme'] == '{':  # '{'
            estrutura_basica()
        elif token_atual['tag'] == 275:  # 'while'
            print("WHILE")
            estrutura_while()
            return
        elif token_atual['tag'] == 265:  # 'if'
            #estrutura_if()
            print("IF")
        elif token_atual['tag'] == 259:  # 'do'
            print("DO")
            estrutura_do_while()
            return
        elif token_atual['tag'] == 258:  # 'break'
            match(258)  
            return
        elif token_atual['tag'] == 264 and token_atual['lexeme'] in letters:  # variavel
            #expressao()
            print("EXPRESSÃO")
            return
        elif token_atual['tag'] == 270:
            #expressao()
            print("EXPRESSÃO")
            return
        elif token_atual['tag'] in [263, '=', '>', '<']:
            #expressao()
            print("EXPRESSÃO")
            return
        elif token_atual['tag'] == 264 and token_atual['lexeme'] in ['+', '-', ';', ')']:
            #expressao()
            print("EXPRESSÃO")
            return
        elif token_atual['tag'] == 264 and token_atual['lexeme'] == '}':
            estrutura_basica()
        else:
            print("Erro aqui")
            print(token_atual)
            print(f"Erro de sintaxe: token inesperado '{token_atual['tag']}'")
            return


def declaracao():
    global line_number
    global current_label
    global labels

    if token_atual['tag'] == 257:
        tipo = token_atual['lexeme']
        match(257)

        if token_atual['tag'] == 264 and token_atual['lexeme'] == '[':  
            coch = cochetes() 
            tipo = tipo + coch
        
        if token_atual['tag'] == 264:
            var = token_atual['lexeme']
            match(264)  # variavel

        if token_atual['tag'] == 264 and token_atual['lexeme'] == ';':
            match(264)  # ';'

            labels[line_number] = f"L{current_label}"
            print(f"{labels[line_number]}: {tipo} - {var}")
            current_label += 1
            line_number += 1
            return
        else:
            print("Erro de sintaxe: esperado ';' ao final")
    
    
def estrutura_while():
    global line_number
    global current_label
    global labels
    
    match(275)  # 'while'
    if token_atual['tag'] == 264 and token_atual['lexeme'] == '(':
        match(264)  # '('
        resultado_condicao = expressao()
        if resultado_condicao == True:
            if token_atual['tag'] == 264 and token_atual['lexeme'] == ')':
                match(264)  # ')'
            if token_atual['tag'] == 264 and token_atual['lexeme'] == '{':
                estrutura_basica()
                labels[line_number] = f"L{current_label}"
                print(f"{labels[line_number]}:{resultado_condicao}")
                current_label += 1
                line_number += 1
                return 
        elif resultado_condicao == False:
            exit(1)

def estrutura_do_while():
    global line_number
    global current_label
    global labels

    match(259)  # 'do'
    if token_atual['tag'] == 264 and token_atual['lexeme'] == '{':
        estrutura_basica()
    else:
        print("atribuição")
        expressao()
        
    if token_atual['tag'] == 264 and token_atual['lexeme'] == ';':
        match(264)  # ';'
    
    if token_atual['tag'] == 275:
        print("while")
        estrutura_while()

# fazer a condição depois
def expressao():
    global exp

    while token_atual['tag'] not in ['<', '>', '=', 263, 274, 262]:
        exp = []
        exp = token_atual['lexeme']
        if token_atual['tag'] == 264 and token_atual['lexeme'] == '[':  
            coch = cochetes()
            #exp = exp + coch
            print(exp)
        match(token_atual['tag'])
    
    if token_atual['tag'] in ['<', '>', 263]:
        comparacao()
    elif token_atual['tag'] == 274:
        match(274)
        return True
    elif token_atual['tag'] == 262:
        match(262)  # 'false'
        return False
    elif token_atual['tag'] == '=':
        atribuicao()

# comparação
def comparacao():
    global exp
    print(token_atual)
    if token_atual['tag'] in ['<', '>']:
        exp = exp + token_atual['tag']
        print(exp)
    match(token_atual['tag'])
    print("expressao")
    print(exp)
    
    '''if token_atual['lexeme'] == '<':
        exp.clear()
    elif token_atual['lexeme'] == '>':
        exp.clear()'''

def atribuicao():
    global line_number
    global current_label
    global labels
    global exp
    '''recebe = exp
    exp = [] '''    # esvaziar a lista
    exp = exp + token_atual['tag']
    match('=')
    
    while True:
        if token_atual['tag'] == 270:
            exp = exp + token_atual['value']
        if token_atual['tag'] == 264:
            if not exp:
                exp = token_atual['lexeme']
            elif token_atual['lexeme'] == ';':
                print()
            else: 
                exp = exp + token_atual['lexeme']  
        
        if token_atual['tag'] == 264 and token_atual['lexeme'] == ';':
            break
        else:
            match(token_atual['tag'])
        
    '''for i in range(len(exp)):
        if exp[i] == '+':
            print("adição")
            recebe = exp[i-1] + exp[i+1]
            print(recebe)
        elif exp[i] == '-':
            print("subtração")
            recebe = exp[i-1] - exp[i+1]
            print(recebe)'''

    '''elif exp[i] in letters:
        print("variavel")
        var = exp[i]'''
    
    
    match(264)
    labels[line_number] = f"L{current_label}"
    print(f"{labels[line_number]}:{exp}")
    current_label += 1
    line_number += 1
    return


def main(tokens):
    global token_atual   
    global labels
    global current_label
    global line_number

    token_atual = tokens.pop(0)
    print(token_atual)

    labels = {}
    current_label = 1
    line_number = 1

    if token_atual['tag'] == 264 and token_atual['lexeme'] == '{':
        confirmacao()
        if match(264) and token_atual['lexeme'] == '}':
            print("'}' estrutura fechada")
        else:
            print("Erro de sintaxe: programa deve finalizar com '}'")
    else:
        print("Erro de sintaxe: programa deve iniciar com '{'")


########################################  INICIO  #############################################

print("inicio análise sintática")
token_atual = None
main(tokens)

print("fim análise sintática")
