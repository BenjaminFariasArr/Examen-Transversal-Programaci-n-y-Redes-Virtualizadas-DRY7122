nombre_completo = "Benjamin Farias"

nombre, apellido = nombre_completo.split()

print("Detalles del Integrante:")
print(f"{'Nombre:':<10} {nombre}")
print(f"{'Apellido:':<10} {apellido}")

lista_nombres_apellidos = [(nombre, apellido)]

print("\nLista de Nombres y Apellidos:")
for nombre, apellido in lista_nombres_apellidos:
    print(f"{'Nombre:':<10} {nombre}, {'Apellido:':<10} {apellido}")
