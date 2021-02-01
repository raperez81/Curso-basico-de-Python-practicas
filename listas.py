""" objetos = ['Hola', 3,5,7,True]

print(objetos)

# Notacion de slice
print(objetos[1:])

# El parámetro de la funcion append será el elemento que queremos agregar
objetos.append(90) 
print(objetos)

# El parámetro de la función será el índice del elemento que queremos borrar, la función pop retorna el elemento borrado
objetos.pop(3)
print(objetos)

# Punteros a listas
list_a = [1,2,3]
list_b = list_a

print(id(list_a))
print(id(list_a))

# Clonando listas con la funcion list
list_a = [1,2,3]
list_b = list(list_a)

print(id(list_a))
print(id(list_b))

# Clonando listas con la notacion de slices
list_a = [1,2,3]
list_b = list_a[::]

print(id(list_a))
print(id(list_b))
# creando una lista con un rago
my_list = list(range(10)) # crea una lista del 0 al 9 
print(my_list) # Salida: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# List Comprehension
double = [i * 2 for i in my_list] # multiplica por 2 cada elemento de la lista
print(double) # Salida: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# creando una lista con los elementos pares de otra lista
pares = [i for i in my_list if i % 2 == 0]
print(pares) # salida: [0, 2, 4, 6, 8]
 """

# Ordenando listas
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)