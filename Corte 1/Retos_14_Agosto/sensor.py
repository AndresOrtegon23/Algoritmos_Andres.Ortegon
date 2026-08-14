while True:
    try:
        cantidad_datos = int(input("Ingrese la cantidad de lecturas a registrar: "))
        if cantidad_datos > 0:
            break
        else:
            print("La cantidad de datos debe ser mayor a 0.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

arreglo_lecturas = [0.0] * cantidad_datos

print("\nIngrese las lecturas (recuerde que -999 es una lectura dañada):")
for i in range(cantidad_datos):
    while True:
        try:
            lectura = float(input(f"Lectura {i + 1}: "))

            arreglo_lecturas[i] = lectura 
            break
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")

suma_validos = 0
cantidad_validos = 0
cantidad_descartados = 0

for lectura in arreglo_lecturas:
    if lectura == -999:
        cantidad_descartados += 1
    else:
        suma_validos += lectura
        cantidad_validos += 1


print("\n    Resultados del Análisis    ")
if cantidad_validos > 0:

    promedio = suma_validos / cantidad_validos
    print(f"El promedio real de las lecturas válidas es: {promedio:.2f}")
else:
    print("No se encontraron lecturas válidas para calcular el promedio.")
    
print(f"Se descartaron {cantidad_descartados} lecturas dañadas.")