# L = { w ∊ {a,b}* | w tem como prefixo aa }

# Σ = {a, b}
# Q = {q0, q1, q2}

# δ = {
#       δ(q0, a) = q1
#       δ(q1, a) = q2
#       δ(q2, a) = q2
#       δ(q2, b) = q2
#     }

# q0 = q0
# F = {q2}

alfabeto = ['a', 'b']
estados = ['q0', 'q1', 'q2']

f_transicao = {
    ('q0', 'a'): 'q1',

    ('q1', 'a'): 'q2',
    
    ('q2', 'a'): 'q2',
    ('q2', 'b'): 'q2',
}

estado_inicial = 'q0'
estados_finais = ['q2']

cadeia = input('Cadeia para testar: ')
estado_atual = estado_inicial

try:
    for simbolo in cadeia:
        estado_atual = f_transicao[(estado_atual, simbolo)]
except KeyError:
    estado_atual = None

if estado_atual in estados_finais:
    print('Aceita')
else:
    print('Rejeita')