class Pila:
    def __init__(self):self.items = []
    def apilar(self,x):self.items.append(x)
    def desapilar(self):
        if self.vacia():return None
        return self.items.pop()
    def cima(self):return None if self.vacia() else self.items[-1]
    def vacia(self):return len(self.items) == 0
    #apilar sobre un array apilo al final O(1) sobre una 
    # lista enlazada apilo al inicio O(1) 
    # desapilar sobre un array desapilo al final O(1) 
    # sobre una lista enlazada desapilo al inicio O(1)
    
    # (a[b]{c}) y (a[b)c] pila cada vez 
    # que se abre un corchete o paréntesis se apila 
    # y cada vez que se cierra se desapila 
    # y se compara con el tope de la pila 
    # si es igual se desapila sino no es balanceado
    
    def balanceados(s):
        p = Pila()
        pares={')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in '([{': p.apilar(c)
            elif c in ')]}':
                if p.desapilar() != pares[c]: return False
        return True

print("Con return True")
print(Pila.balanceados("[]{}"))     
print(Pila.balanceados("([)]"))     
print(Pila.balanceados("((()"))     
print(Pila.balanceados("{}[]()"))   
    #([]{})
    #([)]
    #((()
    #{}[]()