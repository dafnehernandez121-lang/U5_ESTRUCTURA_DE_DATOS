def quicksort(tiempos):
    if len(tiempos) <= 1:
        return tiempos

    pivote = tiempos[len(tiempos) // 2]
    izquierda = [t for t in tiempos if t < pivote]
    centro = [t for t in tiempos if t == pivote]
    derecha = [t for t in tiempos if t > pivote]

    return quicksort(izquierda) + centro + quicksort(derecha)


def main():
    while True:
        print("\n=== TABLA DE POSICIONES - CARRERA 5K (Quicksort) ===")
        print("1. Registrar tiempos de corredores y ordenar")
        print("2. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "2":
            print("Cerrando registro de la carrera.")
            break
        elif opcion == "1":
            try:
                cantidad = int(input("\n¿Cuántos corredores llegaron a la meta?: "))
                if cantidad <= 0:
                    print("Ingresa una cantidad mayor a 0.")
                    continue

                tiempos = []
                for i in range(cantidad):
                    tiempo = float(input(f"Minutos del corredor #{i + 1}: "))
                    tiempos.append(tiempo)

                print(f"\nTiempos de llegada sin ordenar: {tiempos}")
                podio = quicksort(tiempos)
                print(f"Resultados ordenados (1er lugar al último): {podio}")
            except ValueError:
                print("Error: Ingresa únicamente números.")
        else:
            print("Opción inválida. Selecciona 1 o 2.")


if __name__ == "__main__":
    main()