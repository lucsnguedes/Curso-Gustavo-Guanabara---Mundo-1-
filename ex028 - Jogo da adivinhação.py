from random import randint
from time import sleep
npc = randint(0, 5) #Faz o computador sortear um numero
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == npc:
    print('Parabéns, você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!.'.format(npc, jogador))
