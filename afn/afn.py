from time import sleep

# L = { w | w possuí aa ou bb como subpalavra }

# alfabeto = ['a', 'b']
# estados = ['q0', 'q1', 'q2', 'q3']

# f_transicao = {
#     ('q0', 'a'): ['q0', 'q1'],
#     ('q0', 'b'): ['q0', 'q2'],

#     ('q1', 'a'): ['q3'],

#     ('q2', 'b'): ['q3'],
    
#     ('q3', 'a'): ['q3'],
#     ('q3', 'b'): ['q3'],
# }

# estado_inicial = 'q0'
# estados_finais = ['q3']

alfabeto = input('Alfabeto (separando as letras com espaço): ').split()

quantEstados = int(input('Digite a quantidade de estados: '))

estados = []
for i in range(quantEstados):
    estados.append(f'q{i}')

print(f'\nAlfabeto: {alfabeto}')
print(f'Estados: {estados}')

f_transicao = {}

print('\nAdicionar transições:')
loop = 1

while loop == 1:
    estadoPartida = input('\nEstado de partida: ')
    simboloChave = input('Símbolo do alfabeto: ')
    estadoChegada = input('Estados de chegada (separa com espaço): ').split()

    f_transicao[(estadoPartida, simboloChave)] = estadoChegada

    parar = input('\nFinalizou? (s/n): ')
    if parar == 's':
        loop = 0


estado_inicial = input('\nEstado inicial do autômato: ')
estados_finais = input('Estados finais (separa com espaço): ').split()


def transicoes(estado_atual, simbolo):
    try:
        return f_transicao[(estado_atual, simbolo)]
    except KeyError:
        return []


def aceita_cadeia(cadeia):
    estados_atuais = [estado_inicial]

    for simbolo in cadeia:
        estados_possiveis = []

        print('=' * 70)
        sleep(1)
        print(f'Estados atuais: {estados_atuais}')
        sleep(1)
        print(f'Símbolo atual: {simbolo}')

        sleep(1)
        for estado_atual in estados_atuais:
            estados_possiveis.extend(transicoes(estado_atual, simbolo))

            print(f'Estados possíveis para seguir estando em {estado_atual}: {transicoes(estado_atual, simbolo)}')
            
        sleep(1)
        print(f'\nTodos os estados possíveis: {estados_possiveis}')
        estados_atuais = estados_possiveis


    for estado in estados_atuais:
        if estado in estados_finais:
            print(f'\nParou no {estado} que é um estado final!')
            return True

    return False


loop = 1
while loop == 1:
    cadeia = input('\nCadeia para testar: ')
    print()

    sleep(1)
    if aceita_cadeia(cadeia):
        print('\033[32mCadeia aceita!\033[0m')
    else:
        print('\033[31mCadeia rejeitada!\033[0m')
        print('\n\033[31mO autômato não parou em um estado de aceitação!\033[0m')

    sleep(1)
    finalizar = input('\nDeseja finalizar? (s/n): ')
    if finalizar == 's':
        loop = 0
        print('\n\033[1;34mAutômato AFD finalizado!\033[0m')
