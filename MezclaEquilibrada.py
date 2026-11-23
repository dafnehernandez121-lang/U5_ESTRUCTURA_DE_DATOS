import os

def pedir_datos_desordenados(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            datos = [int(x) for x in entrada.split()]
            if not datos:
                print("Debes ingresar al menos un número.")
                continue
            return datos
        except ValueError:
            print("Error: Ingresa únicamente números enteros separados por espacios.")

def distribuir_corridas(origen, aux1, aux2):
    with open(origen, 'r') as f_orig:
        datos = [int(x.strip()) for x in f_orig if x.strip()]

    if not datos:
        return 0

    corridas = 1
    alternar = True

    with open(aux1, 'w') as f1, open(aux2, 'w') as f2:
        f1.write(f"{datos[0]}\n")
        for i in range(1, len(datos)):
            if datos[i] < datos[i - 1]:
                alternar = not alternar
                corridas += 1
            
            destino = f1 if alternar else f2
            destino.write(f"{datos[i]}\n")

    return corridas

def obtener_corridas(archivo):
    with open(archivo, 'r') as f:
        datos = [int(x.strip()) for x in f if x.strip()]
    
    if not datos:
        return []

    corridas = []
    corrida_actual = [datos[0]]

    for i in range(1, len(datos)):
        if datos[i] >= datos[i - 1]:
            corrida_actual.append(datos[i])
        else:
            corridas.append(corrida_actual)
            corrida_actual = [datos[i]]
    corridas.append(corrida_actual)
    return corridas

def fusionar_corridas(aux1, aux2, destino):
    corridas1 = obtener_corridas(aux1)
    corridas2 = obtener_corridas(aux2)

    with open(destino, 'w') as f_dest:
        max_len = max(len(corridas1), len(corridas2))
        
        for i in range(max_len):
            c1 = corridas1[i] if i < len(corridas1) else []
            c2 = corridas2[i] if i < len(corridas2) else []
            
            p1, p2 = 0, 0
            while p1 < len(c1) and p2 < len(c2):
                if c1[p1] <= c2[p2]:
                    f_dest.write(f"{c1[p1]}\n")
                    p1 += 1
                else:
                    f_dest.write(f"{c2[p2]}\n")
                    p2 += 1
            
            while p1 < len(c1):
                f_dest.write(f"{c1[p1]}\n")
                p1 += 1
                
            while p2 < len(c2):
                f_dest.write(f"{c2[p2]}\n")
                p2 += 1

def mezcla_equilibrada(archivo):
    while True:
        num_corridas = distribuir_corridas(archivo, "eq_aux1.txt", "eq_aux2.txt")
        if num_corridas <= 1:
            break
        fusionar_corridas("eq_aux1.txt", "eq_aux2.txt", archivo)

    if os.path.exists("eq_aux1.txt"):
        os.remove("eq_aux1.txt")
    if os.path.exists("eq_aux2.txt"):
        os.remove("eq_aux2.txt")

print("=== MÉTODO DE MEZCLA EQUILIBRADA ===")
tiempos = pedir_datos_desordenados("Ingresa los tiempos de entrega separados por espacios: ")

with open("tiempos_entrega.txt", "w") as f:
    for tiempo in tiempos:
        f.write(f"{tiempo}\n")

mezcla_equilibrada("tiempos_entrega.txt")

with open("tiempos_entrega.txt", "r") as f:
    print("\nDatos originales:", tiempos)
    print("Resultado Mezcla Equilibrada:", [int(x.strip()) for x in f])