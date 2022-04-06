#passo 1: aqui será o ponto inicial, onde iremos acordar. Terá 2 opções: Acordar ou continuar dormindo, se continuarmos dormindo iremos ficar em loop até acordarmos. se acordarmos iremos para os primeiros comando dos jogo onde iremos nos sentar na cama ter alguma interações olhar para os lados e iniciar de fato o game. Onde se passará somente no quarto do(a) nosso(a) protagonista

import os
from helpers import *
from actions import *

def menu():
    os.system('clear')
    print('==========================')
    print('# 1 - Acordar************#')
    print('# 2 - Voltar a dormir****#')
    print('==========================')

def wake():
    while True:
        menu()
        command =input('Comando => ')

        if command not in ['1','2']:
            os.system('clear')
            print('Digite um comando válido')
            os.system('sleep 2')

        elif command == '1':
            #chamar a primeira sequecia de funções aqui
            action1()
            break
            

        elif command == '2':
            clear()
            
