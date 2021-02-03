def dividir_elementos_de_lista(lista, divisor):
    """ Retorna la division de cada elemento de la lista entre el divisor.
    Si el divisor es cero, retorna la lista de entrada """
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista

lista = list(range(10))    
divisor = 0

print(dividir_elementos_de_lista(lista, divisor))
