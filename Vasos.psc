Algoritmo Vasos
    Definir mano_derecha, mano_izquierda Como Caracter
    Definir vaso_A, vaso_B, vaso_C Como Caracter
    vaso_A <- "Jugo de naranja"
    vaso_B <- "Agua"
    vaso_C <- "Vacío"
    mano_derecha <- "Libre"
    mano_izquierda <- "Libre"
    
	
    Escribir "Paso 1 y 2: Extiendes tus manos, coges el Vaso A con la derecha y el Vaso C con la izquierda."
    mano_derecha <- "Sosteniendo Vaso A (Jugo)"
    mano_izquierda <- "Sosteniendo Vaso C (Vacío)"
    
    Escribir "Inclinas el Vaso A sobre el Vaso C y viertes todo el jugo."
    vaso_C <- vaso_A
    vaso_A <- "Vacío"
    
    Escribir "Paso 3: Sueltas el Vaso A dejándolo sobre la mesa."
    mano_derecha <- "Libre"
    vaso_A <- "Vacío (en mesa)"
    
    Escribir "Con tu mano derecha, coges el Vaso B. Lo inclinas sobre el Vaso A y viertes el agua."
    mano_derecha <- "Sosteniendo Vaso B (Agua)"
    vaso_A <- vaso_B
    vaso_B <- "Vacío"
    
    Escribir "Sueltas el Vaso B dejándolo en la mesa."
    mano_derecha <- "Libre"
    vaso_B <- "Vacío (en mesa)"
    
    Escribir "Coges el Vaso C con la mano derecha, lo acercas al Vaso B y viertes el jugo."
    mano_derecha <- "Sosteniendo Vaso C (Jugo)"
    vaso_B <- vaso_C
    vaso_C <- "Vacío"
    
    Escribir "Sueltas el Vaso C dejándolo en la mesa."
    mano_izquierda <- "Libre"
    mano_derecha <- "Libre"
    vaso_C <- "Vacío (en mesa)"
    
    Escribir "Vaso A ahora tiene: ", vaso_A
    Escribir "Vaso B ahora tiene: ", vaso_B
    Escribir "Vaso C ahora está: ", vaso_C
FinAlgoritmo