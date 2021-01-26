# Un palindromo es una palabra, frase o parrafo que se lee igual de 
# izquierda a derecha que de derecha a izquierda, este programa evalua
# si una palabra o frase ingresada por el usuario es un palindromo
def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    run()
