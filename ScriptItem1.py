RANGO_NORMAL = range(1, 1006)
RANGO_EXTENDIDO = range(1006, 4096)

numero_vlan = int(input("Ingrese el número de VLAN: "))

if numero_vlan in RANGO_NORMAL:
    print(f"La VLAN {numero_vlan} corresponde al rango normal (1-1005).")
elif numero_vlan in RANGO_EXTENDIDO:
    print(f"La VLAN {numero_vlan} corresponde al rango extendido (1006-4095).")
else:
    print(f"La VLAN {numero_vlan} no es válida. Ingrese un número entre 1 y 4095.")
