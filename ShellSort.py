def shell_sort(precios):
    arr = precios.copy()
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr


def main():
    while True:
        print("\n=== CARRITO DEL SUPERMERCADO (ShellSort) ===")
        print("1. Ingresar precios y ordenar")
        print("2. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "2":
            print("Saliendo del sistema de compras. ¡Hasta luego!")
            break
        elif opcion == "1":
            try:
                cantidad = int(input("\n¿Cuántos productos llevas en el carrito?: "))
                if cantidad <= 0:
                    print("Debes ingresar al menos 1 producto.")
                    continue

                precios = []
                for i in range(cantidad):
                    precio = float(input(f"Precio del producto {i + 1} ($): "))
                    precios.append(precio)

                print(f"\nPrecios registrados: {precios}")
                ordenados = shell_sort(precios)
                print(f"Precios ordenados (menor a mayor): {ordenados}")
            except ValueError:
                print("Error: Por favor ingresa valores numéricos válidos.")
        else:
            print("Opción no válida. Elige 1 o 2.")


if __name__ == "__main__":
    main()