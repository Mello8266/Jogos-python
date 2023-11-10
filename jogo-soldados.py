import random

jogo = 'Jogo'
print('{:^90}'.format(jogo))
print('Caso a moeda caia com a face coroa, o soldado avança um território e se múltiplica')
print('Caso a moeda caia com a face cara, o soldado morre')
print('-' * 20)

print('Escolha seu time entre: Cara e Coroa')
time = input('')
print('')

soldado = 1
rodadas = 0
cara = 0
coroa = 0
while soldado < 5:
    lista = ['cara', 'coroa']
    moeda = random.choice(lista)

    if moeda == 'cara':
        soldado -= 1
        rodadas += 1
        cara += 1

        print('Moeda: {}\nSoldado morre!'.format(moeda))
        print('Numero de soldados: {}'.format(soldado))
        print('( ͡° ͜ʖ ͡°) ' * soldado, end=' ')
        print('×͜×')
        print('')
        if soldado == 0:
            print('Todos soldados mortos!\nTime cara vecendor')
            break

    elif moeda == 'coroa':
        soldado += 2
        rodadas += 1
        coroa += 1
        print('Moeda: {}\nSoldado avança e múltiplica'.format(moeda))
        print('Numero de soldados: {}'.format(soldado))
        print('( ͡° ͜ʖ ͡°) ' * soldado)
        print('')
        if soldado == 6:
            print('Time coroa vencedor')

print('Número de rodadas | Vezes que caiu coroa | Vezes em que caiu cara | Total de gerações')
print('{:^17} | {:^20} | {:^22} | {:^18}'.format(rodadas, cara, coroa, soldado))