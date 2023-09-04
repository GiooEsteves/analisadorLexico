from tags import *
from symbols import *

def pega_linha(linha):
    return eval(linha.replace("Token: ", "").strip())

tokens = []
with open("output.txt", "r") as arquivo:
    for linha in arquivo:
        if linha.strip():
            tokens.append(pega_linha(linha))

saida = open("saida.txt", "w")

def match(tag_esperada):
    global token_atual
    if token_atual['tag'] == tag_esperada:
        if not tokens:
            return
        else: 
            token_atual = tokens.pop(0)
    else:
        print(f"Erro de sintaxe: esperado tag:'{tag_esperada}', encontrado tag:'{token_atual['tag']}'")


def estrutura_basica():
    global token_atual
    if token_atual['lexeme'] == '{':
        match(264)  # '{'
        confirmacao()
    if token_atual['tag'] == '}':
        match('}')  # '}'


def cochetes():
    global t
    global t_number
    coch = []   
    coch = token_atual['lexeme']
    match(264)   # '['
    if token_atual['tag'] == 270:   #numero 
        coch = coch + token_atual['value']
        match(270)
    elif token_atual['tag'] == 264 and token_atual['lexeme'] in letters:     # variavel
        for i in range (len(t)):
            if token_atual['lexeme'] == t[i]:
                coch = coch + f"t{i + 1}"
        match(264)  # variavel
    if token_atual['tag'] == 264 and token_atual['lexeme'] == ']':   # ']'
        coch = coch + token_atual['lexeme']
        match(264)  # ']'
    if token_atual['tag'] == ';':
        match(';')  # ';'
    return coch


def confirmacao():
    tag_numbers = [value['tag'] for value in tags.values()]
    while token_atual['tag'] in tag_numbers:
        if token_atual['tag'] == 257:  # tipo
            declaracao()
        elif token_atual['tag'] == 264 and token_atual['lexeme'] == '{':  # '{'
            estrutura_basica()
        elif token_atual['tag'] == 275:  # 'while'
            estrutura_while()
            return
        elif token_atual['tag'] == 265:  # 'if'
            estrutura_if()
            return
        elif token_atual['tag'] == 259:  # 'do'
            estrutura_do_while()
            return
        elif token_atual['tag'] == 258:  # 'break'
            match(258)  
            return
        elif token_atual['tag'] == 264 and token_atual['lexeme'] in letters:  # variavel
            expressao()
            return
        elif token_atual['tag'] == '}':
            estrutura_basica() 
        else:
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

        if token_atual['tag'] == ';':
            match(';')  # ';'
            return
        else:
            print("Erro de sintaxe: esperado ';' ao final")
    
    
def estrutura_while():
    global line_number
    global current_label
    global labels
    global varGT
    
    match(275)  # 'while'
    if token_atual['tag'] == 264 and token_atual['lexeme'] == '(':
        match(264)  # '('
        resultado_condicao = expressao()
        if resultado_condicao == True:
            if token_atual['tag'] == 264 and token_atual['lexeme'] == ')':
                match(264)  # ')'
            if token_atual['tag'] == 264 and token_atual['lexeme'] == '{':
                estrutura_basica()
                confirmacao()
                if varGT != 0:
                    labels[line_number] = f"L{current_label}"
                    saida.write(f"{labels[line_number]}: while {resultado_condicao} goto L{varGT}")
                    saida.write("\n")
                    current_label += 1
                    line_number += 1
                
        elif resultado_condicao == False:
            exit(1)
        else: 
            if token_atual['tag'] == 264 and token_atual['lexeme'] == ')':
                match(264)  # ')'
                if token_atual['tag'] == ';':
                    match(';')  # ';'
                if varGT != 0:
                    labels[line_number] = f"L{current_label}"
                    saida.write(f"{labels[line_number]}: while {resultado_condicao} goto L{varGT}")
                    saida.write("\n")
                    current_label += 1
                    line_number += 1
                else:
                    labels[line_number] = f"L{current_label}"
                    saida.write(f"{labels[line_number]}: while {resultado_condicao}")
                    saida.write("\n")
                    current_label += 1
                    line_number += 1
                confirmacao()
                

def estrutura_do_while():
    global line_number
    global current_label
    global labels

    match(259)  # 'do'
    if token_atual['tag'] == 264 and token_atual['lexeme'] == '{':
        estrutura_basica()
    else:
        expressao()
        
    if token_atual['tag'] == ';':
        match(';')  # ';'   
    if token_atual['tag'] == 275:
        estrutura_while()


def estrutura_if():
    global line_number
    global current_label
    global labels
    global exp 
    exp = []
    global varGT 
    match(265)  # 'if'

    if token_atual['tag'] == 264:
        match(264)  # '('
        resultado_condicao =  expressao()

    if token_atual['tag'] == 264 and token_atual['lexeme'] == ')':
        match(264)  # ')'
     
    expression = expressao()
    labels[line_number] = f"L{current_label}"
    saida.write(f"{labels[line_number]}: {expression}")
    saida.write("\n")
    varGT = line_number
    current_label += 1
    line_number += 1

    labels[line_number] = f"L{current_label}"
    saida.write(f"{labels[line_number]}: if {resultado_condicao} goto L{varGT}")
    saida.write("\n")
    current_label += 1
    line_number += 1

    match(';')  # ';'
         

def expressao():
    global t
    global t_number
    global exp
    exp = []
    exp = token_atual['lexeme']
    while token_atual['tag'] not in ['<', '>', '=', ';', 263, 274, 262, 258]:     
        if token_atual['tag'] == 264 and token_atual['lexeme'] == '[':  
            coch = cochetes()
            exp = exp + coch
        if token_atual['tag'] == 264 and token_atual['lexeme'] in letters:
            for i in range (len(t)):
                if token_atual['lexeme'] == t[i]:
                    exp = f"t{i + 1}"

        if token_atual['tag'] in ['<', '>']:
            break
        if token_atual['tag'] == ';':
            break
        else:
            match(token_atual['tag'])

    if token_atual['tag'] in ['<', '>']:
        resultado = comparacao()
        return resultado
    elif token_atual['tag'] == 263:
        resultado = comparacao()
        return resultado
    elif token_atual['tag'] == 274:
        match(274)
        return True
    elif token_atual['tag'] == 262:
        match(262)  # 'false'
        return False
    elif token_atual['tag'] == '=':
        antes = exp
        atribuicao(antes)
        return
    elif token_atual['tag'] == 258: # 'break'
        match(258)
        return exp


def comparacao():
    global line_number
    global current_label
    global labels
    global exp

    if token_atual['tag'] in ['<', '>']:
        exp = exp + token_atual['tag']
        match(token_atual['tag'])
    elif token_atual['tag'] == 263:
        exp = exp + token_atual['lexeme']
        match(token_atual['tag'])

    if token_atual['tag'] == 264:
        for i in range (len(t)):
            if token_atual['lexeme'] == t[i]:
                exp = exp + f"t{i + 1}"
                match(token_atual['tag'])
        if token_atual['lexeme'] not in [')']:
            exp = exp + token_atual['lexeme']
            match(token_atual['tag'])
    elif token_atual['tag'] == 263:
        if not exp:
            exp = token_atual['lexeme']
        else: 
            exp = exp + token_atual['lexeme']
        match(token_atual['tag'])
    return exp


def atribuicao(antes):
    global line_number
    global current_label
    global labels
    global t
    global t_number
    global exp
    exp = []

    if not antes:
        if token_atual['tag'] == 264 and token_atual['lexeme'] in letters:
            exp = token_atual['lexeme']

        if token_atual['tag'] == '=':
            exp = exp + token_atual['tag']
            match('=')
    else:
        t.append(antes)
        exp = token_atual['tag']
        match(token_atual['tag'])

    while token_atual['tag'] not in [';']:
        if token_atual['tag'] == 270:
            exp = exp + token_atual['value']
        if token_atual['tag'] == 264:
            if not exp:
                exp = token_atual['lexeme']
            elif token_atual['tag'] == ';':
                saida.write("")
                break
            elif token_atual['tag'] == 264 and token_atual['lexeme'] == '[':
                coch = cochetes()
                exp = exp + coch
                break
            else:
                exp = exp + token_atual['lexeme']

        match(token_atual['tag'])

    if token_atual['tag'] == ';':
        match(';')

    labels[line_number] = f"L{current_label}"
    saida.write(f"{labels[line_number]}: t{t_number}{exp}")
    saida.write("\n")
    global varGT
    varGT = 0
    varGT = line_number
    current_label += 1
    line_number += 1
    t_number += 1
    
    if token_atual['tag'] == 264 and token_atual['lexeme'] in letters:
        antes = ""
        while token_atual['tag'] != '=':      
            antes = antes + token_atual['lexeme']
            match(token_atual['tag'])
        atribuicao(antes)

def main(tokens):
    global token_atual   
    global labels
    global current_label
    global line_number
    global t_number
    global t
    
    token_atual = tokens.pop(0)

    labels = {}
    current_label = 1
    line_number = 1
    t = []
    t_number = 1

    if token_atual['tag'] == 264 and token_atual['lexeme'] == '{':
        estrutura_basica()

''''''''''''''''''''''''''''''''' INICIO '''''''''''''''''''''''''''''''''  
token_atual = None
main(tokens)
