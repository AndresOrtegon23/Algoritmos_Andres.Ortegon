Algoritmo Adivinar_Numero
	Definir bajo, alto, intento, contador Como Entero
	Definir respuesta Como Cadena
	bajo <- 1
	alto <- 100
	contador <- 0
	respuesta <- ''
	Escribir 'Piensa un número del 1 al 100.'
	Escribir 'Respóndeme siempre con: mayor, menor o correcto.'
	Mientras respuesta<>'correcto' Y bajo<=alto Hacer
		contador <- contador+1
		intento <- trunc((bajo+alto)/2)
		Escribir 'Intento ', contador
		Escribir '¿Es el número ', intento, '?'
		Escribir 'Dime si tu numero es mayor, menor o correcto:'
		Leer respuesta
		Si respuesta='mayor' Entonces
			Escribir 'Como es mayor, descartamos del ', bajo, ' al ', intento
			bajo <- intento+1
		SiNo
			Si respuesta='menor' Entonces
				Escribir 'Como es menor, descartamos del ', intento, ' al ', alto
				alto <- intento-1
			SiNo
				Si respuesta='correcto' Entonces
					Escribir 'Encontré el número.'
				FinSi
			FinSi
		FinSi
	FinMientras
	Escribir 'Adiviné el número secreto en ', contador, ' intentos'
FinAlgoritmo
