def jugar_craps():
    print("   JUEGO DE CRAPS (A UN SOLO TIRO)")
    
    # Solicitar al usuario los valores de los dados de forma manual
    dado1 = int(input("Ingresa el valor del primer dado (1-6): "))
    dado2 = int(input("Ingresa el valor del segundo dado (1-6): "))
    
    suma = dado1 + dado2
    
    print(f"\nDado 1: {dado1}")
    print(f"Dado 2: {dado2}")
    print(f"Suma total: {suma}")
    
    # Reglas de victoria: 2, 3, 7, 11, 12
    if suma in (2, 3, 7, 11, 12):
        print("¡Resultado: HAS GANADO!\n")
    else:
        print("Resultado: HAS PERDIDO.\n")

if __name__ == "__main__":
    jugar_craps()