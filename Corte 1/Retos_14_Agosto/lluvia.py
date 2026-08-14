def obtener_racha_lluvia(arreglo):
    racha_actual = 0
    mejor_racha = 0

    for dia in arreglo:
        if dia == 1:
            racha_actual += 1
            # Actualizamos la mejor racha si la actual la supera
            if racha_actual > mejor_racha:
                mejor_racha = racha_actual
        else:
            # Si hay un 0, la racha actual vuelve a cero
            racha_actual = 0

    return mejor_racha

# Arreglo de prueba según el contexto
arreglo_dias = [0, 1, 1, 0, 1, 1, 1, 0, 1]
resultado_racha = obtener_racha_lluvia(arreglo_dias)

print(f"Arreglo de lluvia: {arreglo_dias}")
print(f"La longitud de la racha más larga de días con lluvia es: {resultado_racha}")