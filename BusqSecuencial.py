def busqueda_secuencial(lista, objetivo):
    comparaciones = 0
    for indice, elemento in enumerate(lista):
        comparaciones += 1
        if elemento == objetivo:
            return indice, comparaciones
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
    while True:
        opcion = input(mensaje).strip().lower()
        if opcion == "salir":
            return None
        if opcion in ("s", "si", "sí"):
            return True
        if opcion in ("n", "no"):
            return False
        print("Entrada inválida: escribe 's' para sí, 'n' para no, o 'salir' para terminar.")


def capturar_lista():
    cantidad = leer_entero_validado("\n¿Cuántas calificaciones deseas ingresar? (mínimo 1): ", minimo=1)
    if cantidad is None:
        return None

    calificaciones = []
    for i in range(cantidad):
        calif = leer_entero_validado(f"Ingresa la calificación #{i + 1} (0-100): ", minimo=0, maximo=100)
        if calif is None:
            return None
        calificaciones.append(calif)

    return calificaciones


def main():
    print("=== BÚSQUEDA SECUENCIAL (Calificaciones de 0 a 100) ===")
    print("Escribe 'salir' en cualquier momento para terminar.")

    while True:
        calificaciones = capturar_lista()
        if calificaciones is None:
            break

        print("\nLista registrada:", calificaciones)

        salir_programa = False
        while True:
            objetivo = leer_entero_validado(
                "\nIngresa la calificación a buscar (0-100 o 'salir'): ", minimo=0, maximo=100
            )
            if objetivo is None:
                salir_programa = True
                break

            posicion, comparaciones = busqueda_secuencial(calificaciones, objetivo)

            print("--- Resultado ---")
            if posicion != -1:
                print(f"Calificación {objetivo} encontrada en el índice {posicion} (posición #{posicion + 1}).")
            else:
                print(f"La calificación {objetivo} no existe en la lista.")
            print(f"Comparaciones realizadas: {comparaciones}")

            buscar_otra = leer_opcion_sn_o_salir("\n¿Buscar otra calificación en esta lista? (s/n o 'salir'): ")
            if buscar_otra is None:
                salir_programa = True
                break
            if not buscar_otra:
                break

        if salir_programa:
            break

        nueva_lista = leer_opcion_sn_o_salir("\n¿Deseas ingresar una lista nueva? (s/n o 'salir'): ")
        if nueva_lista is None or not nueva_lista:
            break

    print("\nPrograma finalizado. ¡Hasta luego!")


if __name__ == "__main__":
    main()