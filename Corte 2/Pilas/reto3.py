# Evaluador de Notación Polaca Inversa (RPN) - Nivel Principiante
# Ejemplo: "tres, cuatro, más" se representa como la lista [3, 4, "+"]

# 1. Creamos la pila vacía (una lista normal de Python)
pila = []

# 2. Definimos la expresión directamente como elementos listos para evaluar
# (Los números van como números y los operadores como texto)
expresion = [3, 4, "+"]

print("--- EXPRESIÓN INICIAL ---")
print("Elementos:", expresion)
print("-" * 30)

# 3. Recorremos cada elemento de la expresión uno por uno
for elemento in expresion:
    
    # Si el elemento es un número, lo guardamos en la pila (PUSH)
    if type(elemento) == int or type(elemento) == float:
        pila.append(elemento)
        print(f"Guardamos el número {elemento} en la pila -> Pila: {pila}")
        
    # Si el elemento es un operador (+, -, *, /)
    elif elemento == "+" or elemento == "-" or elemento == "*" or elemento == "/":
        
        # Sacamos los últimos dos números de la pila (POP)
        # El segundo en salir es 'a' y el último en salir es 'b'
        b = pila.pop()
        a = pila.pop()
        
        # Hacemos la operación matemática básica
        if elemento == "+":
            resultado = a + b
        elif elemento == "-":
            resultado = a - b
        elif elemento == "*":
            resultado = a * b
        elif elemento == "/":
            resultado = a / b
            
        # Metemos el resultado parcial de vuelta a la pila
        pila.append(resultado)
        print(f"Operamos {a} {elemento} {b} = {resultado} -> Pila: {pila}")

# 4. El resultado final es el único número que queda atrapado en la pila
resultado_final = pila.pop()

print("-" * 30)
print(f"El resultado final de la expresión es: {resultado_final}")