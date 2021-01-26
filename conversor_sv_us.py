colones_sv = input("Cuantos colones salvadoreños deseas convertir: ")
colones_sv = float(colones_sv)
valor_dolar = 8.75
dolares = colones_sv / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")
