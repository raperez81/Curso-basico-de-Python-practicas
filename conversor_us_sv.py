dolares = input("Cuantos dólares deseas convertir: ")
dolares = float(dolares)
valor_colones_sv = 8.75
colones_sv = valor_colones_sv * dolares
colones_sv = round(colones_sv, 2)
colones_sv = str(colones_sv)
print("Tienes $" + colones_sv + " colones salvadoreños")
