def _counting_sort(arr, exp):
    n = len(arr)
    salida = [0] * n
    conteo = [0] * 10

    for i in range(n):
        indice = (arr[i] // exp) % 10
        conteo[indice] += 1

    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    i = n - 1
    while i >= 0:
        indice = (arr[i] // exp) % 10
        salida[conteo[indice] - 1] = arr[i]
        conteo[indice] -= 1
        i -= 1

    for i in range(n):
        arr[i] = salida[i]


def radix_sort(folios):
    if not folios:
        return []
    if any(f < 0 for f in folios):
        raise ValueError("Los folios o códigos postales deben ser números positivos.")

    arr = folios.copy()
    maximo = max(arr)
    exp = 1

    while maximo // exp > 0:
        _counting_sort(arr, exp)
        exp *= 10

    return arr


def main():
    while True:
        print("\n=== CLASIFICACIÓN DE PAQUETERÍA - CÓDIGOS POSTALES (Radix Sort) ===")
        print("1. Ingresar códigos postales / folios y ordenar")
        print("2. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "2":
            print("Finalizando sistema de paquetería.")
            break
        elif opcion == "1":
            try:
                cantidad = int(input("\n¿Cuántos paquetes vas a clasificar?: "))
                if cantidad <= 0:
                    print("Debes ingresar al menos 1 paquete.")
                    continue

                folios = []
                for i in range(cantidad):
                    cp = int(input(f"Código postal o folio del paquete {i + 1}: "))
                    folios.append(cp)

                print(f"\nCódigos recibidos: {folios}")
                ordenados = radix_sort(folios)
                print(f"Códigos ordenados por ruta: {ordenados}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Opción incorrecta. Elige 1 o 2.")


if __name__ == "__main__":
    main()