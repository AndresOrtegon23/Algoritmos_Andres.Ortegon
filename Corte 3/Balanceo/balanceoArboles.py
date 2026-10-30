# Quiz 30/10/2026

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.clave = dato  # Compatibilidad
        self.izq = None
        self.der = None
        self.alt = 0      

def alt(n):
    return -1 if n is None else n.alt
 
def fe(n):
    return 0 if n is None else alt(n.izq) - alt(n.der)
 
def recalc(n):
    if n is not None:
        n.alt = 1 + max(alt(n.izq), alt(n.der))

def insertar(n, clave):
    if n is None: 
        return Nodo(clave)
    if clave < n.clave: 
        n.izq = insertar(n.izq, clave)
    elif clave > n.clave: 
        n.der = insertar(n.der, clave)
    recalc(n)
    return n

def rotarIzquierda(x):
    y = x.der
    B = y.izq
    y.izq = x
    x.der = B
    recalc(x)
    recalc(y)
    return y

def rotarDerecha(y):
    x = y.izq
    B = x.der
    x.der = y
    y.izq = B
    recalc(y)
    recalc(x)
    return x

def inorden(n, s):
    if n is None: return
    inorden(n.izq, s)
    s.append(n.clave)
    inorden(n.der, s)
    
def preorden(n, s):
    if n is None: return
    s.append(f"{n.clave}(fe={fe(n)})")
    preorden(n.izq, s)
    preorden(n.der, s)

def ver(titulo, raiz):
    s = []
    preorden(raiz, s)
    t = []
    inorden(raiz, t)
    print(f"\n{titulo}")
    print(f"  Preorden : {' '.join(s)}")
    print(f"  Inorden  : {t}")
    print(f"  Altura   : {alt(raiz)}")

c1 = int(input("Ingrese la clave 1: "))
c2 = int(input("Ingrese la clave 2: "))
c3 = int(input("Ingrese la clave 3: "))

raiz = None
for val in [c1, c2, c3]:
    raiz = insertar(raiz, val)

# 1. Estado inicial
ver("Árbol antes de rotar:", raiz)

# 2. Diagnóstico
factor_raiz = fe(raiz)
caso = "Equilibrado"

if factor_raiz > 1:
    caso = "LL" if fe(raiz.izq) >= 0 else "LR"
elif factor_raiz < -1:
    caso = "RR" if fe(raiz.der) <= 0 else "RL"

print(f"\n[Diagnóstico] Caso detectado: {caso} (FE raíz = {factor_raiz})")

# 3. Aplicación de rotación
if caso == "LL":
    raiz = rotarDerecha(raiz)
elif caso == "RR":
    raiz = rotarIzquierda(raiz)
elif caso == "LR":
    raiz.izq = rotarIzquierda(raiz.izq)
    recalc(raiz)
    raiz = rotarDerecha(raiz)
elif caso == "RL":
    raiz.der = rotarDerecha(raiz.der)
    recalc(raiz)
    raiz = rotarIzquierda(raiz)

# 4. Estado final
ver("Árbol después de rotar:", raiz)