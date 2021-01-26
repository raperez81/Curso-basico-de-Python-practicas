menu = '''
Bienvenido al conversor de monedas 💰

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción: '''
valor_dolares = 0

opcion = int(input(menu))

if opcion >= 1 and opcion <= 3:
    if opcion == 1:
        monto = float(input('Cuantos pesos colombianos deseas convertir: '))
        valor_dolar = 3875
    elif opcion == 2:
        monto = float(input('Cuantos pesos argentinos deseas convertir: '))
        valor_dolar = 65
    elif opcion == 3:
        monto = float(input('Cuantos pesos mexicanos deseas convertir: '))
        valor_dolar = 24
    dolares = str(round(monto / valor_dolar, 2))
    print('Tienes $' + dolares + ' dólares')
else:
    print(str(opcion) + ' no es una opción válida')


def imprimir_mensaje():
    print('Mensaje especial: ')
    print('Estoy aprendiendo a usar funciones')

imprimir_mensaje()    
