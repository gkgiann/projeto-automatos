from time import sleep

# L = { w ∊ {a,b}* | w tem como prefixo aa }

# alfabeto = ['a', 'b']
# estados = ['q0', 'q1', 'q2']

# f_transicao = {
#     ('q0', 'a'): 'q1',

#     ('q1', 'a'): 'q2',

#     ('q2', 'a'): 'q2',
#     ('q2', 'b'): 'q2',
# }

# estado_inicial = 'q0'
# estados_finais = ['q2']

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
    estadoPartida = input('\nDigite o estado de partida (qi): ')
    simboloChave = input('Digite o símbolo do alfabeto: ')
    estadoChegada = input('Digite o estado de chegada (qi): ')

    f_transicao[(estadoPartida, simboloChave)] = estadoChegada

    parar = input('\nFinalizou? (s/n): ')
    if parar == 's':
        loop = 0


estado_inicial = input('\nDigite o estado inicial do autômato (qi): ')
estados_finais = input('Digite os estados finais (separa com espaço): ').split()

loop = 1
while loop == 1:
    cadeia = input('\nCadeia para testar: ')
    print()

    estado_atual = estado_inicial

    try:
        for simbolo in cadeia:
            estado_anterior = estado_atual
            estado_atual = f_transicao[(estado_atual, simbolo)]

            sleep(1)
            print(f'{estado_anterior} - {simbolo} ---> {estado_atual}')

    except KeyError:
        sleep(1)
        print(f'\033[31mERRO: O autômato travou no estado {estado_anterior} ao tentar consumir o simbolo {simbolo}\033[0m')
        estado_atual = None

    print()
    sleep(1)
    if estado_atual in estados_finais:
        print('\033[32mCadeia aceita!\033[0m')
    else:
        print('\033[31mCadeia rejeitada!\033[0m')

    sleep(1)
    finalizar = input('\nDeseja finalizar? (s/n): ')
    if finalizar == 's':
        loop = 0
        print('\n\033[1;34mAutômato AFD finalizado!\033[0m')