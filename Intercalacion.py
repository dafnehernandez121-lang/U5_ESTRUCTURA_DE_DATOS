def pedir_datos_ordenados(nombre_sucursal):
    while True:
        entrada = input(f"Ingresa los códigos de {nombre_sucursal} separados por espacios: ")
        try:
            datos = [int(x) for x in entrada.split()]
            if not datos:
                print("Debes ingresar al menos un número.")
                continue
            datos.sort()
            return datos
        except ValueError:
            print("Error: Ingresa únicamente números enteros separados por espacios.")

def intercalacion(archivo_a, archivo_b, archivo_salida):
    with open(archivo_a, 'r') as f1, open(archivo_b, 'r') as f2, open(archivo_salida, 'w') as out:
        linea_a = f1.readline().strip()
        linea_b = f2.readline().strip()

        while linea_a and linea_b:
            num_a = int(linea_a)
            num_b = int(linea_b)

            if num_a <= num_b:
                out.write(f"{num_a}\n")
                linea_a = f1.readline().strip()
            else:
                out.write(f"{num_b}\n")
                linea_b = f2.readline().strip()

        while linea_a:
            out.write(f"{linea_a}\n")
            linea_a = f1.readline().strip()

        while linea_b:
            out.write(f"{linea_b}\n")
            linea_b = f2.readline().strip()

print("=== MÉTODO DE INTERCALACIÓN ===")
datos_a = pedir_datos_ordenados("Sucursal A")
datos_b = pedir_datos_ordenados("Sucursal B")

with open("sucursal_a.txt", "w") as f:
    for num in datos_a:
        f.write(f"{num}\n")

with open("sucursal_b.txt", "w") as f:
    for num in datos_b:
        f.write(f"{num}\n")

intercalacion("sucursal_a.txt", "sucursal_b.txt", "inventario_total.txt")

with open("inventario_total.txt", "r") as f:
    resultado = [int(x.strip()) for x in f]
    print("\nArchivo A (ordenado):", datos_a)
    print("Archivo B (ordenado):", datos_b)
    print("Resultado Intercalación:", resultado)