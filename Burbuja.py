def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

entrada = input(" Método de ordenmiento burbuja: Ingresa los números separados por espacios: ")

numeros = [int(x) for x in entrada.split()]

print("Números desordenados:", numeros)
numeros_ordenados = ordenamiento_burbuja(numeros)
print("Números ordenados:", numeros_ordenados)