def obtener_racha_lluvia(arreglo):
    racha_actual = 0
    mejor_racha = 0

    for dia in arreglo:
        if dia == 1:
            racha_actual += 1

            if racha_actual > mejor_racha:
                mejor_racha = racha_actual
        else:
            racha_actual = 0

    return mejor_racha

arreglo_dias = [0, 1, 1, 0, 1, 1, 1, 0, 1]
resultado_racha = obtener_racha_lluvia(arreglo_dias)

print(f"Arreglo de lluvia: {arreglo_dias}")
print(f"La longitud de la racha más larga de días con lluvia es: {resultado_racha}")