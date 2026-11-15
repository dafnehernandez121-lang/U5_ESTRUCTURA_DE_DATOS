def ordenamiento_insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

entrada = input("Metodo de ordenamiento por insercion, ingresa los numeros separados por espacios: ")

numeros = [float(x) for x in entrada.split()] 

print()
print("Numeros desordenados:", numeros)
numeros_ordenados = ordenamiento_insercion(numeros)
print()
print("Numeros ordenados:", numeros_ordenados)
print()