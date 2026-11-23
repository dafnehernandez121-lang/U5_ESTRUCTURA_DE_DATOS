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

def particionar(origen, aux1, aux2, longitud_bloque):
    with open(origen, 'r') as f_orig, open(aux1, 'w') as f1, open(aux2, 'w') as f2:
        datos = [int(linea.strip()) for linea in f_orig if linea.strip()]
        
        alternar = True
        for i in range(0, len(datos), longitud_bloque):
            bloque = datos[i:i + longitud_bloque]
            destino = f1 if alternar else f2
            for num in bloque:
                destino.write(f"{num}\n")
            alternar = not alternar
            
    return len(datos)

def fusionar(aux1, aux2, destino, longitud_bloque):
    with open(aux1, 'r') as f1, open(aux2, 'r') as f2, open(destino, 'w') as f_dest:
        lista1 = [int(x.strip()) for x in f1 if x.strip()]
        lista2 = [int(x.strip()) for x in f2 if x.strip()]
        
        idx1, idx2 = 0, 0
        while idx1 < len(lista1) or idx2 < len(lista2):
            fin1 = min(idx1 + longitud_bloque, len(lista1))
            fin2 = min(idx2 + longitud_bloque, len(lista2))
            
            while idx1 < fin1 and idx2 < fin2:
                if lista1[idx1] <= lista2[idx2]:
                    f_dest.write(f"{lista1[idx1]}\n")
                    idx1 += 1
                else:
                    f_dest.write(f"{lista2[idx2]}\n")
                    idx2 += 1
            
            while idx1 < fin1:
                f_dest.write(f"{lista1[idx1]}\n")
                idx1 += 1
                
            while idx2 < fin2:
                f_dest.write(f"{lista2[idx2]}\n")
                idx2 += 1

def mezcla_directa(archivo):
    longitud_bloque = 1
    total_datos = particionar(archivo, "aux1.txt", "aux2.txt", longitud_bloque)
    
    while longitud_bloque < total_datos:
        fusionar("aux1.txt", "aux2.txt", archivo, longitud_bloque)
        longitud_bloque *= 2
        if longitud_bloque < total_datos:
            particionar(archivo, "aux1.txt", "aux2.txt", longitud_bloque)

    if os.path.exists("aux1.txt"):
        os.remove("aux1.txt")
    if os.path.exists("aux2.txt"):
        os.remove("aux2.txt")

print("=== MÉTODO DE MEZCLA DIRECTA ===")
matriculas = pedir_datos_desordenados("Ingresa las matrículas desordenadas separadas por espacios: ")

with open("calificaciones.txt", "w") as f:
    for mat in matriculas:
        f.write(f"{mat}\n")

mezcla_directa("calificaciones.txt")

with open("calificaciones.txt", "r") as f:
    print("\nDatos originales:", matriculas)
    print("Resultado Mezcla Directa:", [int(x.strip()) for x in f])