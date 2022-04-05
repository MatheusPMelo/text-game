import os
#refazer tudo

def game():
    while True:
        os.system('clear')
        print('===============MENU==============')
        print('# 1 => Acordar***************** #')
        print('# 2 => Dormir de novo********** #')
        print('=================================')

        command = input('Comando => ')

        if command == '1':
            os.system('clear')
            print ('Você acorda e nota que não esta no seu quarto...')
            print ('Você está numa floresta densa e vê uma trilha em tua frente')
            print ('Vê um machado a sua direita preso em um toco de madeira')
            print ('========================================')
            print ('COMANDOS:')
            print ('1 - Seguir em frente')
            print ('2 - Pegar machado')

            cmd = input('Comando => ')

            if cmd == '1':
                os.system('clear')
                print('Você ve uma parede de galhos em seu caminho')
                print ('========================================')
                print ('COMANDOS:')
                print ('1 - Voltar')

                cmd = input('Comando => ')

                if cmd not in '1':
                    print('Comando inválido, tente novamente')
                    os.system('sleep 2')

                    os.system('clear')
                    print('Você ve uma parede de galhos em seu caminho')
                    print ('========================================')
                    print ('COMANDOS:')
                    print ('1 - Voltar')
                
                elif cmd == '1':
                    os.system('clear')
                    print('Você voltou para o ponto inicial')
            
            elif cmd == '2':
                os.system('clear')
                print('Você pegou o MACHADO')
                print ('========================================')
                print ('COMANDOS:')
                print ('1 - Voltar')

                cmd = input('Comando => ')

        elif command == '2':
            os.system('clear')
            print('teste')