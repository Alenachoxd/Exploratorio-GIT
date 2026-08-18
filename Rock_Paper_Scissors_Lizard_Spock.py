from random import randint

user = input('Ingresa tu nombre de usuario:')

accion = ''
while accion != '0':
    accion = input(f'''
    -----------------------------
                MENU 
    -----------------------------
    Jugador: {user}

    [1] Rock
    [2] Paper
    [3] Scissors 
    [4] Lizard 
    [5] Spock 

    [0] Salir del juego
    Seleccione una accion: ''')

    if accion in '12345' and accion != '':
        accion = int(accion)
        bot = randint(1,5)
        elecciones = ['Rock','Paper', 'Scissors', 'Lizard', 'Spock']
        print('Tú elegiste', elecciones[accion-1])
        print('La cpu jugó con', elecciones[bot-1])
        if accion == 1 and bot == 2 or accion == 2 and bot == 1:
            print('Paper covers Rock')

        elif accion == 1 and bot == 3 or accion == 3 and bot == 1:
            print('Rock crushes Scissors')

        elif accion == 1 and bot == 4 or accion == 4 and bot == 1:
            print('Rock crushes Lizard')

        elif accion == 1 and bot == 5 or accion == 5 and bot == 1:
            print('Spock vaporizes Rock')
            
        elif accion == 2 and bot == 3 or accion == 3 and bot == 2:
            print('Scissors cuts Paper')
            
        elif accion == 2 and bot == 4 or accion == 4 and bot == 2:
            print('Lizard eats Paper')
            
        elif accion == 2 and bot == 5 or accion == 5 and bot == 2:
            print('Paper disproves Spock')
            
        elif accion == 3 and bot == 4 or accion == 4 and bot == 3:
            print('Scissors decapitates Lizard')
            
        elif accion == 3 and bot == 5 or accion == 5 and bot == 3:
            print('Spock smashes Scissors')

        elif accion == 4 and bot == 5 or accion == 5 and bot == 4:
            print('Lizard poisons Spock')
        if accion == bot:
            print('¡EMPATARON! Juega otra vez!!')
        else:
            accion = '0'
    elif accion == '0':
        pass
    else:
        print('Accion invalida!!!!!!!!!!')

print('fin del juego')
print('Muchas gracias por jugar!')