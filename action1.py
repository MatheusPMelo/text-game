from secret import *
from helpers import *
from vermelho import *
from azul import *


def action1():
    while True:
        clear()
        print('Você está estremamente apertado para ir a um banheiro...')
        pressContinue()
        print('Você entra correndo numa rodoviária e encontra o banheiro mais próximo...')
        pressContinue()
        print('Você entra tão rápido que não repara um coisa...')
        pressContinue()
        print('ESTÁ SEM PAPEL HIGIÊNICO!!!!')
        pressContinue()
        print('Mas como se estivesse esperando, alguém de repente oferece para você...')
        pressContinue()
        print('A pessoa misteriosa pergunta:...')
        pressContinue()
        print('Você quer o rolo VERMELHO ou o rolo AZUL? \n')
        
        menuRolo()
        cmd = command()


        if cmd not in ['1','2','0']:
            while cmd not in ['1', '2']:
                clear()
                print('commando inválido \n')
                menuRolo()
                cmd = command()
                exit()
                

        if cmd == '1':
            clear()
            vermelho()
            print('Até mais...')
            pressContinue()
            break
        
        elif cmd == '2':
            clear()
            azul()
            print('Até mais...')
            pressContinue()
            break

        elif cmd == '0' :
            clear()
            secret()
            pressContinue()
            print('Você acaba de sobreviver a AKA MANTO')
            time.sleep(2)
            tresPontos()
            clear()
            print('Até mais...')
            time.sleep(2)
            exit()
            
            