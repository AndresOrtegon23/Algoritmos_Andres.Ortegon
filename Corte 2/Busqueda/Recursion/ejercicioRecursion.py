import time

nivel = 0 

def factorial (n):
    global nivel
    print ("| " * nivel + f"factorial {n} entra")
    nivel += 1
    r = 1 if n <= 1 else n * factorial (n-1)
    nivel -= 1
    print("|  " * nivel + f"factorial({n}) devuelve {r}")
    return r

def fibonacci(n):
    global i
    i += 1
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

r = factorial(4)
print(f"Resultado = {r}")
print()

i = 0

w = fibonacci(10)

inicio = time.perf_counter()

print ("Fibonacci de 10 = ", w)
print("Cantidad de llamadas recursivas = ", i)
print("Tiempo de ejecucion=", time.perf_counter() - inicio)

