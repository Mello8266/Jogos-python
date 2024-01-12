from random import choice
from time import sleep

def resultado(cara=False):
    print(f'\033[33mMoeda\033[m: {moeda}')
    print('Soldado avança e múltiplica' if not cara else 'Soldado morre!')
    print(f'Numero de soldados: {soldado}')
    if cara:
        print('\033[32m( ͡° ͜ʖ ͡°)\033[m' * soldado, end='')
        print('\033[31m ×͜× \033[m')
    else:
        print('\033[32m( ͡° ͜ʖ ͡°)\033[m' * soldado)
    print()

def tabela(cara=False):
    if cara:
        print('\033[31mTodos soldados mortos!\nTime Cara vecendor\033[m')
    else:
        print('\033[32mSoldados avançaram todo o território! \nTime coroa vencedor\033[m')
    print('Número de rodadas | Vezes que caiu coroa | Vezes em que caiu cara | Total de gerações')
    print(f'{rodadas:^17} | {coroa:^20} | {cara:^22} | {soldado:^18}')

print('-=' * 45)
print(f'{"Jogo da moeda":^90}')
print('-=' * 45)
print('''Caso a moeda caia com a face coroa, o soldado avança um território e se múltiplica
Caso a moeda caia com a face cara, o soldado morre
Time coroa vence quando tiver 6 soldados
Time cara vence caso não haja nenhum soldado''')
print('-' * 90)

print('Escolha entre \033[31mCara\033[m e \033[32mCoroa\033[m')
time = str(input('\033[33mTime\033[m: '))
jogos = int(input('Deseja jogar quantas partidas? '))
sleep(1)

lista = ['cara', 'coroa']
timeCoroa = timeCara = 0
cont = 1
while cont != jogos + 1:
    soldado = 1
    t = f'Jogo {cont}'
    print()
    print('-=' * 45)
    print(f'{t:^90}')
    print('-=' * 45)
    while True:   
        rodadas = cara = coroa = 0
        moeda = choice(lista)

        if moeda == 'cara':
            soldado -= 1
            rodadas += 1
            cara += 1
            resultado(cara=True)
            sleep(1)
            if soldado <= 0:
                timeCara += 1
                tabela(cara=True)
                sleep(2)
                break

        elif moeda == 'coroa':
            soldado += 2
            rodadas += 1
            coroa += 1
            resultado()
            sleep(1)
            if soldado >= 6:
                timeCoroa += 1
                tabela()
                sleep(2)
                break
    cont += 1            

print()
print('-' * 90)
print(f'Time cara venceu {timeCara}')
print(f'Time coroa venceu {timeCoroa}')
if timeCara > timeCoroa:
    print('\033[31mTime cara vencedor\033[m')
elif timeCara == timeCoroa:
    print('\033[33mEmpate\033[m')
else:
    print('\033[32mTime coroa vencedor\033[m')
