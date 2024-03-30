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

cadeiaAlfabeto = input('\nDigite o alfabeto: ')

alfabeto = []
for simbolo in cadeiaAlfabeto:
    alfabeto.append(simbolo)

quantEstados = int(input('Digite a quantidade de estados: '))

estados = []
for i in range(quantEstados):
    estados.append('q' + str(i))

print('\nAlfabeto: ' + str(alfabeto))
print('Estados: ' + str(estados))

f_transicao = {

}
print('\nAdicionar transições:\n')
addTransicoes = 1
while addTransicoes == 1:
    estPartida = input('Digite o estado de partida (qi): ')
    simboloChave = input('Digite o símbolo do alfabeto: ')
    estChegada = input('Digite o estado de chegada (qi): ')

    f_transicao[(estPartida, simboloChave)] = estChegada

    print()

    parar = input('Finalizou? (s/n): ')
    if parar == 's':
        addTransicoes = 0

    print()

estado_inicial = input('Digite o estado inicial do autômato (qi): ')
estado_atual_sempre = estado_inicial

estados_finais = []
addEstadosFinais = 1
while addEstadosFinais == 1:
    estados_finais.append(input('Digite 1 estado final do autômato (qi): '))

    fimEstadosFinais = input('Fim de estados finais? (s/n): ')
    if fimEstadosFinais == 's':
        addEstadosFinais = 0

# ALFABETOS E ESTADOS JÁ DEFINIDOS
"""
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
estado_atual = estado_inicial
"""

testCadeias = 1
while testCadeias == 1:
    cadeia = input('Cadeia para testar: ')
    print()

    estado_atual = estado_atual_sempre

    try:
        for simbolo in cadeia:
            estado_anterior = estado_atual
            estado_atual = f_transicao[(estado_atual, simbolo)]

            print('Atual: ' + estado_anterior + " - Símbolo: " + simbolo + ' --->' + ' Virou: ' + estado_atual)

    except KeyError:
        print('!# ERRO: O símbolo ' + simbolo + ' não foi aceito no estado ' + estado_anterior + ' #!')
        estado_atual = None

    print()

    if estado_atual in estados_finais:
        print('Cadeia aceita!\n')
    else:
        print('Cadeia rejeitada!\n')

    finalizar = input('Deseja finalizar? (s/n): ')
    if finalizar == 's':
        testCadeias = 0
        print('Autômato AFD finalizado!')

    print()
