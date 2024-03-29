# L = { w ∈ {a,b}* | w possui a’s que antecedem b’s }

alfabeto = ['a', 'b']
estados = ['q0', 'q1']

f_transicao = {
    ('q0', 'a'): ['q0'],
    ('q0', ''): ['q1'],

    ('q1', 'b'): ['q1'],
}

estado_inicial = 'q0'
estados_finais = ['q1']

def transicoes(estado_atual, simbolo):
    try:
        return f_transicao[(estado_atual, simbolo)]
    except KeyError:
        return []


def aceita_cadeia(cadeia, estado_atual):
    if cadeia == '' and estado_atual in estados_finais:
        return True
    
    for estado in transicoes(estado_atual, ''):
        if aceita_cadeia(cadeia, estado):
            return True
        
    if cadeia == '':
        return False
    
    for estado in transicoes(estado_atual, cadeia[0]):
        if aceita_cadeia(cadeia[1:], estado):
            return True
        
    return False


cadeia = input('Cadeia para testar: ')

if aceita_cadeia(cadeia, estado_inicial):
    print('Aceita')
else:
    print('Rejeita')