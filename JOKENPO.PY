from random import choice
from time import sleep

print('     \033[4;33mVAMOS JOGAR JO KEN PÔ\033[m    ')

print('''\033[1;32mComputador: Vamos jogar pedra, papel, tesoura;
Vamos as regras do jogo:
pedra vence tesoura;
papel vence pedra;
tesoura vence papel\033[m''')

jogador = str(input('Qual opção você escolhe: pedra, papel ou tesoura? '))

sleep(2)
print('\033[1;35mJO')
sleep(2)
print('KEN')
sleep(2)
print('PÔ\033[m')

lista = ['pedra', 'papel', 'tesoura']

computador = choice(lista)

print('\033[1;36mJogador escolheu {}'.format(jogador))
sleep(1)
print('Computador escolheu {}'.format(computador))

if jogador == 'pedra' and computador == 'pedra':
    print('Empate')
elif jogador == 'pedra' and computador == 'tesoura':
    print('Jogador Venceu')
elif jogador == 'pedra' and computador == 'papel':
    print('Computador Venceu')
elif jogador == 'papel' and computador == 'papel':
    print('Empate')
elif jogador == 'papel' and computador == 'pedra':
    print('Jogador Venceu')
elif jogador == 'papel' and computador == 'tesoura':
    print('Computador Venceu')
elif jogador == 'tesoura' and computador == 'tesoura':
    print('Empate')
elif jogador == 'tesoura' and computador == 'papel':
    print('Jogador Venceu')
elif jogador == 'tesoura' and computador == 'pedra':
    print('Computador Venceu')
else:
    print('Opção invalida! Tente novamente!')
