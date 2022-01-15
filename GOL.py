# Made by Eric Johansson
# Date 15/1/2022
# Version 1.0
import os
import time




# Creates a 20x20 board filled with " " with a border of "#"s and some "*"s in starting positions 
def createBoard():
		board = []
		for i in range(22):
				board.append([])
				for j in range(22):
						if i == 0 or i == 21 or j == 0 or j == 21:
								board[i].append("#")
						else:
								board[i].append(" ")
		board[2][2] = "*"
		board[3][3] = "*"
		board[4][3] = "*"
		board[4][2] = "*"
		board[4][1] = "*"
		return board

# Prints out the board
def printBoard(board):
		for i in board:
				for j in i:
						print(j, end="")
				print()

# checks all of the neighbors of a cell and returns the number of neighbors, including diagonals
def countNeighbors(board, i, j):
		count = 0
		if board[i-1][j] == "*":
				count += 1
		if board[i+1][j] == "*":
				count += 1
		if board[i][j-1] == "*":
				count += 1
		if board[i][j+1] == "*":
				count += 1
		if board[i-1][j-1] == "*":
				count += 1
		if board[i-1][j+1] == "*":
				count += 1
		if board[i+1][j-1] == "*":
				count += 1
		if board[i+1][j+1] == "*":
				count += 1
		return count


# Checks if the cells should die, stay alive or be born in the next generation
def updateBoard(board):
		newBoard = createBoard()
		for i in range(1, 21):
				for j in range(1, 21):
						if board[i][j] == "*":
							if countNeighbors(board, i, j) < 2:
								newBoard[i][j] = " "
							elif countNeighbors(board, i, j) > 3:
								newBoard[i][j] = " "
							else:
								newBoard[i][j] = "*"
						elif board[i][j] == " ":
							if countNeighbors(board, i, j) == 3:
								newBoard[i][j] = "*"
							else:
								newBoard[i][j] = " "
		return newBoard

# Main function
def rungame():
	generations = int(input("How many generations? "))
	board = createBoard()
	os.system('cls') # Clears the screen. Change to 'clear' if on mac
	printBoard(board)
	time.sleep(0.5) # Pauses the game for 0.5 seconds

	for i in range(generations-1):
		os.system('cls') # Clears the screen. Change to 'clear' for mac
		board = updateBoard(board)
		printBoard(board)
		time.sleep(0.5) # Pauses the game for 0.5 seconds




rungame()