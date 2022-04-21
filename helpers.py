import os


def clear():
    return os.system('clear')
    
def pressContinue():
    print('')
    print('')
    input('Precione ENTER tecla para continuar...')
    clear()

def command():
    return input('Comando => ')

def menuRolo():
    print('\n========AKA MANTO=========')
    print('# 1 => VERMELHO ******** #')
    print('# 2 => AZUL ************ #')
    print('========================== \n')

def menuRoloInv():
    print('\n=========INVÁLIDO=========')
    print('# 1 => VERMELHO ******** #')
    print('# 2 => AZUL ************ #')
    print('========================== \n')

