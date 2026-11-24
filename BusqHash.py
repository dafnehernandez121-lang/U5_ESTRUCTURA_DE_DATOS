def funcion_hash(clave, tamano_tabla):
    return clave % tamano_tabla


def insertar_alumno(tabla_hash, matricula, datos_alumno):
    indice = funcion_hash(matricula, len(tabla_hash))
    for i, (clave_existente, _) in enumerate(tabla_hash[indice]):
        if clave_existente == matricula:
            tabla_hash[indice][i] = (matricula, datos_alumno)
            return
    tabla_hash[indice].append((matricula, datos_alumno))


def buscar_alumno(tabla_hash, matricula):
    indice = funcion_hash(matricula, len(tabla_hash))
    revisiones = 0
    for clave_existente, datos_alumno in tabla_hash[indice]:
        revisiones += 1
        if clave_existente == matricula:
            return indice, datos_alumno, revisiones
    return indice, None, revisiones


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


def leer_texto_validado(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto.lower() == "salir":
            return None
        if not texto:
            print("Entrada inválida: el campo no puede estar vacío.")
            continue
        if not any(caracter.isalpha() for caracter in texto):
            print("Entrada inválida: ingresa un nombre o descripción con letras.")
            continue
        return texto


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


def capturar_tabla_hash():
    tamano_tabla = leer_entero_validado(
        "\nIngresa el tamaño de la tabla hash (mínimo 1, ej. 7): ", minimo=1
    )
    if tamano_tabla is None:
        return None

    cantidad = leer_entero_validado("¿Cuántos alumnos deseas registrar? (mínimo 1): ", minimo=1)
    if cantidad is None:
        return None

    tabla_hash = [[] for _ in range(tamano_tabla)]

    for i in range(cantidad):
        print(f"\nAlumno #{i + 1}:")
        matricula = leer_entero_validado("  Matrícula (entero positivo): ", minimo=1)
        if matricula is None:
            return None

        nombre = leer_texto_validado("  Nombre y carrera: ")
        if nombre is None:
            return None

        insertar_alumno(tabla_hash, matricula, nombre)

    return tabla_hash


def main():
    print("=== BÚSQUEDA HASH (Directorio de Alumnos por Matrícula) ===")
    print("Escribe 'salir' en cualquier momento para terminar.")

    while True:
        tabla_hash = capturar_tabla_hash()
        if tabla_hash is None:
            break

        salir_programa = False
        while True:
            matricula_buscar = leer_entero_validado(
                "\nIngresa la matrícula a buscar (entero positivo o 'salir'): ", minimo=1
            )
            if matricula_buscar is None:
                salir_programa = True
                break

            indice, datos, revisiones = buscar_alumno(tabla_hash, matricula_buscar)

            print("--- Resultado ---")
            if datos is not None:
                print(f"Alumno encontrado en la cubeta hash [{indice}]: {datos}")
            else:
                print(f"No se encontró la matrícula {matricula_buscar} (cubeta evaluada: [{indice}]).")
            print(f"Revisiones realizadas en la cubeta: {revisiones}")

            buscar_otra = leer_opcion_sn_o_salir("\n¿Buscar otra matrícula en esta tabla? (s/n o 'salir'): ")
            if buscar_otra is None:
                salir_programa = True
                break
            if not buscar_otra:
                break

        if salir_programa:
            break

        nueva_lista = leer_opcion_sn_o_salir("\n¿Deseas ingresar una lista nueva de alumnos? (s/n o 'salir'): ")
        if nueva_lista is None or not nueva_lista:
            break

    print("\nPrograma finalizado. ¡Hasta luego!")


if __name__ == "__main__":
    main()