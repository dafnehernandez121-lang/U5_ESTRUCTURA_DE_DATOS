def busqueda_secuencial(lista, objetivo):
    comparaciones = 0
    for i, valor in enumerate(lista):
        comparaciones += 1
        if valor == objetivo:
            return i, comparaciones
    return -1, comparaciones


def busqueda_binaria(lista_ordenada, objetivo):
    izquierda = 0
    derecha = len(lista_ordenada) - 1
    comparaciones = 0

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        comparaciones += 1
        if lista_ordenada[medio] == objetivo:
            return medio, comparaciones
        elif lista_ordenada[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1, comparaciones


def construir_tabla_hash(lista, tamano=7):
    tabla = [[] for _ in range(tamano)]
    for elemento in lista:
        indice = elemento % tamano
        tabla[indice].append(elemento)
    return tabla


def busqueda_hash(tabla, objetivo):
    tamano = len(tabla)
    indice_cubeta = objetivo % tamano
    comparaciones = 0

    for elemento in tabla[indice_cubeta]:
        comparaciones += 1
        if elemento == objetivo:
            return indice_cubeta, comparaciones

    return -1, comparaciones


def pedir_lista():
    while True:
        entrada = input("\nIngresa los números separados por espacios (ej. 15 4 28 9 42): ").strip()
        try:
            numeros = [int(x) for x in entrada.split()]
            if not numeros:
                print("Debes ingresar al menos un número.")
                continue
            return numeros
        except ValueError:
            print("Entrada no válida. Escribe solo números enteros separados por espacios.")


def mostrar_menu(datos):
    print("\n" + "=" * 44)
    print("       MENÚ DE MÉTODOS DE BÚSQUEDA")
    print("=" * 44)
    print(f"Tus datos actuales: {datos}")
    print("-" * 44)
    print("1. Búsqueda Secuencial")
    print("2. Búsqueda Binaria")
    print("3. Búsqueda Hash")
    print("4. Ingresar nuevos datos")
    print("5. Salir")
    print("=" * 44)


def main():
    print("=== BIENVENIDO AL PROGRAMA DE BÚSQUEDAS ===")
    datos = pedir_lista()

    while True:
        mostrar_menu(datos)
        opcion = input("Selecciona una opción (1-5): ").strip()

        if opcion in ("1", "2", "3"):
            try:
                objetivo = int(input("Ingresa el número que deseas buscar: ").strip())
            except ValueError:
                print("Debes ingresar un número entero válido.")
                continue

            if opcion == "1":
                pos, comp = busqueda_secuencial(datos, objetivo)
                if pos != -1:
                    print(f"[Secuencial] El número {objetivo} está en el índice {pos} ({comp} comparaciones).")
                else:
                    print(f"[Secuencial] El número {objetivo} NO se encontró ({comp} comparaciones).")

            elif opcion == "2":
                ordenada = sorted(datos)
                pos, comp = busqueda_binaria(ordenada, objetivo)
                print(f"Lista ordenada usada para binaria: {ordenada}")
                if pos != -1:
                    print(f"[Binaria] El número {objetivo} está en el índice {pos} ({comp} comparaciones).")
                else:
                    print(f"[Binaria] El número {objetivo} NO se encontró ({comp} comparaciones).")

            elif opcion == "3":
                tabla = construir_tabla_hash(datos, tamano=7)
                cubeta, comp = busqueda_hash(tabla, objetivo)
                print(f"Tabla hash generada (7 cubetas): {tabla}")
                if cubeta != -1:
                    print(f"[Hash] El número {objetivo} se encontró en la cubeta {cubeta} ({comp} comparaciones).")
                else:
                    print(f"[Hash] El número {objetivo} NO se encontró ({comp} comparaciones).")

        elif opcion == "4":
            datos = pedir_lista()

        elif opcion == "5":
            print("Programa finalizado. ¡Mucho éxito en tu tarea!")
            break

        else:
            print("Opción no válida. Elige un número del 1 al 5.")


if __name__ == "__main__":
    main()