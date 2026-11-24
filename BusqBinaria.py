def busqueda_binaria(lista_ordenada, objetivo):
    izquierda = 0
    derecha = len(lista_ordenada) - 1
    comparaciones = 0

    while izquierda <= derecha:
        comparaciones += 1
        medio = (izquierda + derecha) // 2
        valor_medio = lista_ordenada[medio]

        if valor_medio == objetivo:
            return medio, comparaciones
        elif valor_medio < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1, comparaciones


def leer_entero_validado(mensaje, minimo=None, maximo=None):
    while True:
        entrada = input(mensaje).strip()
        if entrada.lower() == "salir":
            return None

        try:
            valor = int(entrada)
        except ValueError:
            print("Entrada inválida: ingresa un número entero o escribe 'salir'.")
            continue

        if minimo is not None and valor < minimo:
            print(f"Valor fuera de rango: debe ser mayor o igual a {minimo}.")
            continue

        if maximo is not None and valor > maximo:
            print(f"Valor fuera de rango: debe ser menor o igual a {maximo}.")
            continue

        return valor


def leer_opcion_sn_o_salir(mensaje):
    """Lee 's', 'n' o 'salir'. Retorna True para 's', False para 'n', o None para 'salir'."""
    while True:
        opcion = input(mensaje).strip().lower()
        if opcion == "salir":
            return None
        if opcion in ("s", "si", "sí"):
            return True
        if opcion in ("n", "no"):
            return False
        print("Entrada inválida: escribe 's' para sí, 'n' para no, o 'salir' para terminar.")


def capturar_catalogo_ordenado():
    cantidad = leer_entero_validado("\n¿Cuántos códigos de producto deseas ingresar? (mínimo 1): ", minimo=1)
    if cantidad is None:
        return None

    codigos = []
    for i in range(cantidad):
        codigo = leer_entero_validado(f"Ingresa el código #{i + 1} (entero positivo): ", minimo=1)
        if codigo is None:
            return None
        codigos.append(codigo)

    return sorted(codigos)


def main():
    print("=== BÚSQUEDA BINARIA (Códigos de Producto) ===")
    print("Escribe 'salir' en cualquier momento para terminar.")

    while True:
        codigos_ordenados = capturar_catalogo_ordenado()
        if codigos_ordenados is None:
            break

        print("\nCatálogo ordenado para búsqueda binaria:", codigos_ordenados)

        salir_programa = False
        while True:
            objetivo = leer_entero_validado(
                "\nIngresa el código a buscar (entero positivo o 'salir'): ", minimo=1
            )
            if objetivo is None:
                salir_programa = True
                break

            posicion, comparaciones = busqueda_binaria(codigos_ordenados, objetivo)

            print("--- Resultado ---")
            if posicion != -1:
                print(f"Código {objetivo} encontrado en el índice {posicion}.")
            else:
                print(f"El código {objetivo} no existe en el catálogo.")
            print(f"Iteraciones/comparaciones realizadas: {comparaciones}")

            buscar_otra = leer_opcion_sn_o_salir("\n¿Buscar otro código en este catálogo? (s/n o 'salir'): ")
            if buscar_otra is None:
                salir_programa = True
                break
            if not buscar_otra:
                break

        if salir_programa:
            break

        nueva_lista = leer_opcion_sn_o_salir("\n¿Deseas ingresar una lista nueva de códigos? (s/n o 'salir'): ")
        if nueva_lista is None or not nueva_lista:
            break

    print("\nPrograma finalizado. ¡Hasta luego!")


if __name__ == "__main__":
    main()