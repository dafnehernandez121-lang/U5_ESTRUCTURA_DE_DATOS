def ordenamiento_seleccion(lista):
    n = len(lista)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    return lista

try:
    cantidad = int(input("Metodo de ordenamiento por seleccion: ¿Cuantos numeros vas a ingresar? "))
    numeros = []
    
    for i in range(cantidad):
        num = float(input(f"Ingresa el numero {i + 1}: "))
        numeros.append(num)
        
    print("\nNúmeros desordenados:", numeros)
    numeros_ordenados = ordenamiento_seleccion(numeros)
    print()
    print("Números ordenados:", numeros_ordenados)
    print()

except ValueError:
    print("Error: Por favor ingresa valores numericos validos.")