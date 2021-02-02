def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3
    }
    print(mi_diccionario)
    print(mi_diccionario['llave2'])
    
    # Reasignando un valor por medio de una llave
    mi_diccionario['llave1'] = 10
    print(mi_diccionario)
    
    # Consultando una llave que no existe
    #print(mi_diccionario['llave4']) 
    # Salida: 
    """ Traceback (most recent call last):
            File "d:\Platzi\Curso Basico de Python\Practicas\diccionarios.py", line 38, in <module>     
                run()
            File "d:\Platzi\Curso Basico de Python\Practicas\diccionarios.py", line 15, in run
                print(mi_diccionario['llave4'])
        KeyError: 'llave4' """

    # Si la llave no existe, devolverá el segundo parámetro
    print(mi_diccionario.get('llave4',4))
    
    # Agregando valores a un diccionario
    mi_diccionario['llave4'] = 4
    print(mi_diccionario)

    # Borrando valores de un diccionario
    del mi_diccionario['llave1']
    print(mi_diccionario)

    # Buscando si una llave se encuentra en un diccionario
    print('llave5' in mi_diccionario) # Salida: False
    print('llave2' in mi_diccionario) # Salida: True

    # Recorriendo diccionarios
    # Podemos hacerlo iterando por sus llaves, valores o ambos

    """ poblacion_paises = {
        'Argentina': 44000000,
        'Brasil': 210000000,
        'Colombia': 50000000
    }

    for pais in poblacion_paises.keys():
        print(pais)
    # Salida:
    # Argentina
    # Brasil
    # Colombia
    for pais in poblacion_paises.values():
        print(pais)
    # Salida:
    # 44000000
    # 210000000
    # 50000000

    for pais in poblacion_paises.items():
        print(pais)
    # Salida:
    # ('Argentina', 44000000)
    # ('Brasil', 210000000)
    # ('Colombia', 50000000)

    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')
    # Salida:
    # Argentina tiene 44000000 habitantes
    # Brasil tiene 210000000 habitantes
    # Colombia tiene 50000000 habitantes
     """

if __name__ == '__main__':
    run()
