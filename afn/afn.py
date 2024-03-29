# L = { w | w possuí aa ou bb como subpalavra }

alfabeto = ['a', 'b']
estados = ['q0', 'q1', 'q2', 'q3']

f_transicao = {
    ('q0', 'a'): ['q0', 'q1'],
    ('q0', 'b'): ['q0', 'q2'],

    ('q1', 'a'): ['q3'],

    ('q2', 'b'): ['q3'],
    
    ('q3', 'a'): ['q3'],
    ('q3', 'b'): ['q3'],
}

estado_inicial = 'q0'
estados_finais = ['q3']

def transicoes(estado_atual, simbolo):
    try:
        return f_transicao[(estado_atual, simbolo)]
    except KeyError:
        return []


def aceita_cadeia(cadeia):
    estados_atuais = [estado_inicial]

    for simbolo in cadeia:
        estados_possiveis = []

        for estado_atual in estados_atuais:
            estados_possiveis.extend(transicoes(estado_atual, simbolo))
            
        estados_atuais = estados_possiveis


    for estado in estados_atuais:
        if estado in estados_finais:
            return True

    return False


cadeia = input('Cadeia para testar: ')

if aceita_cadeia(cadeia):
    print('Aceita')
else:
    print('Rejeita')