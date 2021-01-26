import random


def run():
    numero_pc, numero_jugador, intentos = 0, 0, 0

    seguir_jugando = True

    print('Adivina el número que ha generado la computadora entre 1 - 100')
    numero_pc = random.randrange(1, 101)
    # print('numero_pc: ' + str(numero_pc))
    numero_jugador = int(input('Escribe tu número: '))
    while seguir_jugando:
        intentos += 1
        if numero_jugador == numero_pc:
            print('Ganaste!!!')
            print('Te tomó ' + str(intentos) + ' intentos')
            seguir_jugando = False
        elif numero_jugador < numero_pc:
            numero_jugador = int(
                input('Muy bajo, prueba con un número mas grande: '))
        elif numero_jugador > numero_pc:
            numero_jugador = int(
                input('Muy alto, prueba con un número mas bajo: '))


if __name__ == '__main__':
    run()
