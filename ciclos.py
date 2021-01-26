""" def run():
    LIMITE = 1000
    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print('2**' + str(contador) + '=' + str(potencia_2))
        contador += 1
        potencia_2 = 2**contador


if __name__ == '__main__':
    run() """

# Imprime de 0 a 10
for contador in range(11):
    print(contador)

# Imprime de 5 a 10
for contador in range(5,11):
    print(contador)
