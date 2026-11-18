def _heapify(arr, n, i):
    mayor = i
    izquierda = 2 * i + 1
    derecha = 2 * i + 2

    if izquierda < n and arr[izquierda] > arr[mayor]:
        mayor = izquierda

    if derecha < n and arr[derecha] > arr[mayor]:
        mayor = derecha

    if mayor != i:
        arr[i], arr[mayor] = arr[mayor], arr[i]
        _heapify(arr, n, mayor)


def heapsort(prioridades):
    arr = prioridades.copy()
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        _heapify(arr, i, 0)

    return arr


def main():
    while True:
        print("\n=== GESTIÓN DE TURNOS Y URGENCIAS (Heapsort) ===")
        print("1. Ingresar niveles de prioridad y ordenar")
        print("2. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "2":
            print("Saliendo del gestor de turnos.")
            break
        elif opcion == "1":
            try:
                cantidad = int(input("\n¿Cuántos turnos hay en espera?: "))
                if cantidad <= 0:
                    print("La cantidad debe ser mayor a 0.")
                    continue

                prioridades = []
                for i in range(cantidad):
                    nivel = int(input(f"Nivel de prioridad del turno {i + 1} (1-100): "))
                    prioridades.append(nivel)

                print(f"\nPrioridades ingresadas: {prioridades}")
                ordenadas = heapsort(prioridades)
                print(f"Prioridades ordenadas (menor a mayor urgencia): {ordenadas}")
            except ValueError:
                print("Error: Ingresa números enteros válidos.")
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()