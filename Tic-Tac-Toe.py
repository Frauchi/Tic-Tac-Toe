board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
player = 1


def translate_tile(value):
	if value == 0:
		tile = " "
	elif value == 1:
		tile = "X"
	else:
		tile = "O"

	return tile


def print_board(current_board):
	print("")
	print("  A   B   C")
	print("1", translate_tile(current_board[0][0]), "|", translate_tile(current_board[0][1]), "|", translate_tile(current_board[0][2]))
	print("  ---------")
	print("2", translate_tile(current_board[1][0]), "|", translate_tile(current_board[1][1]), "|", translate_tile(current_board[1][2]))
	print("  ---------")
	print("3", translate_tile(current_board[2][0]), "|", translate_tile(current_board[2][1]), "|", translate_tile(current_board[2][2]))
	print("")


def translate_column(letter):
	letter = letter.upper()

	if letter == "A":
		translated_column = 0
	elif letter == "B":
		translated_column = 1
	else:
		translated_column = 2

	return translated_column


def translate_row(digit):
	translated_row = int(digit) - 1

	return translated_row


def check_line(line, updated_board):
	cell1 = line[0]
	row1 = cell1[0]
	column1 = cell1[1]
	value1 = updated_board[row1][column1]
	
	cell2 = line[1]
	row2 = cell2[0]
	column2 = cell2[1]
	value2 = updated_board[row2][column2]
	
	cell3 = line[2]
	row3 = cell3[0]
	column3 = cell3[1]
	value3 = updated_board[row3][column3]
	
	if value1 == value2 == value3:
		return value1
	else:
		return 0


def obtain_winner(updated_board):
	row1 = [(0,0), (0,1), (0,2)]
	row2 = [(1,0), (1,1), (1,2)]
	row3 = [(2,0), (2,1), (2,2)]
	column1 = [(0,0), (1,0), (2,0)]
	column2 = [(0,1), (1,1), (2,1)]
	column3 = [(0,2), (1,2), (2,2)]
	diagonal = [(0,0), (1,1), (2,2)]
	antidiagonal = [(0,2), (1,1), (2,0)]

	lines = [row1, row2, row3, column1, column2, column3, diagonal, antidiagonal]
	
	for line in lines:
		line_value = check_line(line, updated_board)
		if line_value != 0:
			return line_value
	
	return 0


def board_is_full(board):
	for row in board:
		for value in row:
			if value == 0:
				return False
	return True	


name1 = input("Write player 1's name: ")
name2 = input("Write player 2's name: ")


while obtain_winner(board) == 0 and board_is_full(board) != True:
	print_board(board)
	move = input("Place your tile: ")
	letter = move[0]
	digit = move[1]

	column = translate_column(letter)
	row = translate_row(digit)

	if board[row][column] != 0:
		print("The cell you picked is already taken, please, choose another.")
	else:
		board[row][column] = player #actualiza
	
		if player == 1:
			player = 2
		elif player == 2:
			player = 1


winner = obtain_winner(board)

if winner == 0:
	print("Draw")
else:
	if winner == 1:
		name = name1
	else:
		name = name2

	print("Condragulations, " + name + "!")
