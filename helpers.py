import os


def clear():
    return os.system('cls')
    
def pressContinue():
    print('')
    print('')
    input('Precione ENTER tecla para continuar...')
    clear()

def command():
    return input('Comando => ')

def menuYesNo():
    print('')
    print('')
    print('==========================')
    print('# 1 - SIM****************#')
    print('# 2 - NÃO****************#')
    print('==========================')