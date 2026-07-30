Algoritmo Prioridad_Salud
    Definir edad, minutos_espera Como Entero
    Definir condicion_urgencia, prioridad Como Caracter
    
    Escribir "Ingrese la edad del paciente:"
    Leer edad
    
    Escribir "¿Tiene condición de urgencia? (si / no):"
    Leer condicion_urgencia
    
    Escribir "¿Cuántos minutos lleva esperando?: "
    Leer minutos_espera
    
	
    Si condicion_urgencia = "si" Entonces
        Escribir ">> El paciente presenta una condición de urgencia médica."
        Escribir ">> La salud inmediata está por encima de todo."
        prioridad <- "Alta"
    Sino
        Escribir ">> No hay urgencia médica crítica."
        
        Si edad >= 60 O minutos_espera > 30 Entonces
            Si edad >= 60 Y minutos_espera > 30 Entonces
                Escribir ">> El paciente es adulto mayor Y lleva una espera prolongada."
            Sino
                Si edad >= 60 Entonces
                    Escribir ">> El paciente es adulto mayor (atención prioritaria)."
                Sino
                    Escribir ">> El paciente supera el tiempo límite de espera."
                FinSi
            FinSi
            prioridad <- "Media"
        Sino
            Escribir ">> Criterio aplicado: Paciente joven, sin urgencia y con tiempo de espera bajo."
            prioridad <- "Baja"
        FinSi
    FinSi
    
    Escribir "Nivel de prioridad asignado: ", prioridad
FinAlgoritmo