# Función recursiva simple para calcular la potencia
def calcularPotenciaSimple(baseNumero, exponenteNumero):
    # Caso base: cualquier número elevado a 0 es 1
    if exponenteNumero == 0:
        return 1
    
    # Caso recursivo: multiplica la base por la potencia con el exponente menos uno
    return baseNumero * calcularPotenciaSimple(baseNumero, exponenteNumero - 1)

# Función recursiva 
def calcularPotenciaOptimizada(baseNumero, exponenteNumero):
    # Caso base: cualquier número elevado a 0 es 1
    if exponenteNumero == 0:
        return 1
    
    # Verificamos si el exponente es par
    if exponenteNumero % 2 == 0:
        # Calculamos la mitad de la potencia de forma recursiva
        mitadPotencia = calcularPotenciaOptimizada(baseNumero, exponenteNumero // 2)
        
        # Multiplicamos el resultado de la mitad por sí mismo
        return mitadPotencia * mitadPotencia
    
    # Caso si el exponente es impar: sacamos un factor y reducimos a par
    return baseNumero * calcularPotenciaOptimizada(baseNumero, exponenteNumero - 1)

import time

# Definimos los valores de prueba
basePrueba = 2
exponentePrueba = 500

# Medición del tiempo para la versión simple
tiempoInicioSimple = time.perf_counter()
resultadoSimple = calcularPotenciaSimple(basePrueba, exponentePrueba)
tiempoFinSimple = time.perf_counter()
duracionSimple = tiempoFinSimple - tiempoInicioSimple

# Medición del tiempo para la versión optimizada
tiempoInicioOpt = time.perf_counter()
resultadoOpt = calcularPotenciaOptimizada(basePrueba, exponentePrueba)
tiempoFinOpt = time.perf_counter()
duracionOpt = tiempoFinOpt - tiempoInicioOpt

# Mostramos los resultados en consola
print(f"Resultado Simple: {resultadoSimple}")
print(f"Tiempo Simple: {duracionSimple:.8f} segundos")
print(f"---")
print(f"Resultado Optimizado: {resultadoOpt}")
print(f"Tiempo Optimizado: {duracionOpt:.8f} segundos")