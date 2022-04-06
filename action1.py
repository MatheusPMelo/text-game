import os
from helpers import *

def action1():
    while True:
        clear()
        print('Você abre seus olhos cansados e se senta na cama...')
        pressContinue()
        print('Você nota que está tudo normal exceto uma coisa...')
        pressContinue()
        print('A porta do seu closet está entre aberta...')
        pressContinue()
        print('(Levanto para fecha-la?)')
        menuYesNo()
        cmd = command()

        if cmd not in ['1','2']:
            while cmd not in ['1', '2']:
                clear()
                print('commando inválido')
                print('(Levanto para fecha-la?)')
                menuYesNo()
                cmdw = command()

                if cmdw == '1':
                    
                    break
                        
                elif cmdw == '2':
                    clear()
                    print('Escolhei 2')
                    os.system('sleep 2')
                    break
                

        if cmd == '1':
            clear()
            print('Você fechou a porta e sentiu um frio subto...')
            pressContinue()
            break
        
        elif cmd == '2':
            clear()
            print('Escolhei 2')
            os.system('sleep 2')
            break