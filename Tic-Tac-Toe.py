tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
jugador = 1


def traducir_ficha(valor):
	if valor == 0:
		ficha = " "
	elif valor == 1:
		ficha = "X"
	else:
		ficha = "O"

	return ficha


def pintar_tablero(tablero_actual):
	print("")
	print("  A   B   C")
	print("1", traducir_ficha(tablero_actual[0][0]), "|", traducir_ficha(tablero_actual[0][1]), "|", traducir_ficha(tablero_actual[0][2]))
	print("  ---------")
	print("2", traducir_ficha(tablero_actual[1][0]), "|", traducir_ficha(tablero_actual[1][1]), "|", traducir_ficha(tablero_actual[1][2]))
	print("  ---------")
	print("3", traducir_ficha(tablero_actual[2][0]), "|", traducir_ficha(tablero_actual[2][1]), "|", traducir_ficha(tablero_actual[2][2]))
	print("")


def traducir_columna(letra_introducida):
	letra_introducida = letra_introducida.upper()

	if letra_introducida == "A":
		columna_traducida = 0
	elif letra_introducida == "B":
		columna_traducida = 1
	else:
		columna_traducida = 2

	return columna_traducida


def traducir_fila(digito_introducido):
	fila_traducida = int(digito_introducido) - 1

	return fila_traducida


def comprobar_raya(raya_introducida, tablero_actualizado):
	celda1 = raya_introducida[0]
	fila1 = celda1[0]
	columna1 = celda1[1]
	valor1 = tablero_actualizado[fila1][columna1]
	
	celda2 = raya_introducida[1]
	fila2 = celda2[0]
	columna2 = celda2[1]
	valor2 = tablero_actualizado[fila2][columna2]
	
	celda3 = raya_introducida[2]
	fila3 = celda3[0]
	columna3 = celda3[1]
	valor3 = tablero_actualizado[fila3][columna3]
	
	if valor1 == valor2 == valor3:
		return valor1
	else:
		return 0


def obtener_ganador(tablero_actualizado):
	fila_1 = [(0,0), (0,1), (0,2)]
	fila_2 = [(1,0), (1,1), (1,2)]
	fila_3 = [(2,0), (2,1), (2,2)]
	columna_1 = [(0,0), (1,0), (2,0)]
	columna_2 = [(0,1), (1,1), (2,1)]
	columna_3 = [(0,2), (1,2), (2,2)]
	diagonal = [(0,0), (1,1), (2,2)]
	antidiagonal = [(0,2), (1,1), (2,0)]

	rayas = [fila_1, fila_2, fila_3, columna_1, columna_2, columna_3, diagonal, antidiagonal]
	
	for raya in rayas:
		valor_raya = comprobar_raya(raya, tablero_actualizado)
		if valor_raya != 0:
			return valor_raya
	
	return 0


def tablero_lleno(tablero):
	for fila in tablero:
		for valor in fila:
			if valor == 0:
				return False
	return True	


nombre1 = input("Introduce el nombre del jugador 1: ")
nombre2 = input("Introduce el nombre del jugador 2: ")


while obtener_ganador(tablero) == 0 and tablero_lleno(tablero) != True:
	pintar_tablero(tablero)
	movimiento = input("Coloca tu ficha: ")
	letra = movimiento[0]
	digito = movimiento[1]

	columna = traducir_columna(letra)
	fila = traducir_fila(digito)

	if tablero[fila][columna] != 0:
		print("La casilla seleccionada ya está llena, por favor, elige otra.")
	else:
		tablero[fila][columna] = jugador #actualiza
	
		if jugador == 1:
			jugador = 2
		elif jugador == 2:
			jugador = 1


ganador = obtener_ganador(tablero)

if ganador == 0:
	print("Empate")
else:
	if ganador == 1:
		nombre = nombre1
	else:
		nombre = nombre2

	print("Enhorabuena, " + nombre + "!")
