from helpers import *
from vermelho import *
from azul import *

def action1():
    while True:
        clear()
        print('Você está estremamente apertado para ir um banheiro...')
        pressContinue()
        print('Você entra correndo numa rodoviária e econtra o banheiro mais próximo...')
        pressContinue()
        print('Você entra tão rápido que não repara um coisa...')
        pressContinue()
        print('Está sem papel higiênico...')
        pressContinue()
        print('Mas como se estivesse esperando alguém de repente oferece para você...')
        pressContinue()
        print('A pessoa misteriosa pergunta:...')
        pressContinue()
        print('Você quer o rolo VERMELHO ou o rolo AZUL? \n')

        menuRolo()

        cmd = command()


        if cmd not in ['1','2']:
            while cmd not in ['1', '2']:
                clear()
                print('commando inválido \n')
                menuRolo()
                cmd = command()
                exit()
                

        if cmd == '1':
            clear()
            vermelho()
            pressContinue()
            break
        
        elif cmd == '2':
            clear()
            azul()
            pressContinue()
            break