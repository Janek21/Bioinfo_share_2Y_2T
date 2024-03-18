import sys
import math
import os

class N_in_line(object):

	def __init__(self):

		self.n = 3  # Setting 3 as default
		self.obj = 3  # Setting 3 as default

		# Creation of a matrix n*n representing the board (default: 3*3)
		self.board = [[' ' for _ in range(self.n)] for _ in range(self.n)]

		# Initializing the players
		self.player1 = ''
		self.player2 = ''

	def change_n(self):
		'''
		Function that asks the player for the size of the board
		'''
		print("Please enter the number of rows and columns you want the board to have")
		n = sys.stdin.readline().strip()

		if n.isspace():  # If no value is entered, keeping the default one
			pass
		elif not n.isdigit():  # Checking if the input is a digit
			print('Invalid input. Try again.\n')
			self.change_n()
		else:
			n = int(n)  # Transforming into integer

			if n >= 3:
				self.n = n  # Changing n inside the class
				self.board = [[' ' for _ in range(self.n)] for _ in range(self.n)]  # Creation of the n*n board
				print(f"You have selected a {self.n}x{self.n} board\n")
			else:
				print("The input is too small. Try again. \n")
				self.change_n()

	def change_obj(self):
		'''
		Function that allows the player to configure the nº of tokens in a row needed to win
		'''
		print("Please enter the number of tokens in a row to win")
		n = sys.stdin.readline().strip()

		if n.isspace():  # If no value is entered, keeping the default one
			pass
		elif not n.isdigit():  # Checking if the input is a digit
			print('Invalid input. Try again.\n')
			self.change_obj()
		elif int(n) > self.n: # Checking for a coherent objective
			print(f'The number of tokens in a row of your input is too high. Try again\n')
			self.change_obj()
		elif int(n) < 3:
			print("The input is too small. Try again. \n")
			self.change_obj()
		else:
			n = int(n)  # Transforming into integer
			self.obj = n  # Changing n inside the class
			print(f"To win you need {self.obj} tokens in a row to win\n")

	def represent_board(self):
		'''
		Function that allows us to visualize the board
		'''
		line = '-' * self.n + '-' * (self.n - 1)  # Calculating the number of dashes needed for each line depending on n
		print(line)

		# Iterating through each of the n rows of the board
		for row in self.board:
			# Representation of the board:
			print('|'.join(row))
			print(line)

		print()  # Empty line as separator

	def is_board_full(self):
		'''
		Function that checks if the board is full (no more space to put a piece)
		Output: True / False
		'''

		# Iterating through each cell of the matrix
		for i in range(self.n):
			for j in range(self.n):
				# Checking if there is an empty cell in the board
				if self.board[i][j] == ' ':
					return False  # If so the board is not full and we return False
		return True

	def is_game_ended(self):
		'''
		Function that checks if the game has ended (to know when to finish the game)
		It does so by checking if the board is full or if one of the players has won
		Output: True / False
		'''
		# Checking if one of the players have won and if the board is full or not
		return self.check_winner(self.player1) or self.check_winner(self.player2) or self.is_board_full()

	def check_winner(self, player):
		"""
		Function that takes self and the player as arguments and tells us if a determined player is the winner or not.
		Output: True / False
		"""
		# Check rows
		for i in range(self.n):
			row_count = 0
			for j in range(self.n):
				if self.board[i][j] == player:
					row_count += 1
					if row_count == self.obj:
						# Check if the next cell is empty or belongs to the opponent
						if j == self.n - 1 or self.board[i][j + 1] != player:
							return True
				else:
					row_count = 0

		# Check columns
		for j in range(self.n):
			col_count = 0
			for i in range(self.n):
				if self.board[i][j] == player:
					col_count += 1
					if col_count == self.obj:
						# Check if the next cell is empty or belongs to the opponent
						if i == self.n - 1 or self.board[i + 1][j] != player:
							return True
				else:
					col_count = 0

		# Check diagonals
		for i in range(self.n - self.obj + 1):  # Iterate over rows
			for j in range(self.n - self.obj + 1):  # Iterate over columns
				# Check diagonal going from bottom-left to top-right
				count = 0
				for k in range(self.obj):
					if self.board[i + k][j + k] == player:
						count += 1
						if count == self.obj:
							# Check if the next cell is empty or belongs to the opponent
							if (i + k == self.n - 1 or j + k == self.n - 1) or self.board[i + k + 1][j + k + 1] != player:
								return True
					else:
						count = 0

				# Check diagonal going from top-left to bottom-right
				count = 0
				for k in range(self.obj):
					if self.board[i + self.obj - k - 1][j + k] == player:
						count += 1
						if count == self.obj:
							# Check if the next cell is empty or belongs to the opponent
							if (i + self.obj - k - 1 == self.n - 1 or j + k == self.n - 1) or self.board[
								i + self.obj - k - 2][j + k + 1] != player:
								return True
					else:
						count = 0

		return False  # If the function continues until here it means that the player has not won, so returning False

	def ask_move(self):
		'''
		Function that asks the player for it's next move
		'''
		print("Please do your move (Input example: '>>>row column')")
		move = sys.stdin.readline().strip().split()  # Getting and formatting input from stdin
		print()  # Formatting output

		if len(move) != 2:
			print("Invalid input. Try again.\n")
			self.ask_move()
		elif not move[0].isdigit() or not move[1].isdigit():  # Checking that the input is correct
			print("Invalid input. Try again.\n")
			self.ask_move()
		else:
			return int(move[0]) - 1, int(move[1]) - 1  # Returning the coordinates (from userfriendly to programming logic) if the input is correct

	def choose_player(self):
		'''
		Function that allows the player to change it's token
		'''
		print('Choose your symbol: X / O (Upper)')
		symb = sys.stdin.readline().strip()

		if symb == 'X':
			self.player1 = 'X'
			self.player2 = 'O'
		elif symb == 'O':
			self.player1 = 'O'
			self.player2 = 'X'
		else:
			print("Invalid input. Try again.\n")
			self.choose_player()

		print()  # Formatting the output (empty line)

	def get_moves(self):
		'''
		Function that looks for all the possible moves for the bot
		'''
		moves = []  # Creating empty list to store all the legal moves

		# Iterating through each cell of the board matrix
		for i in range(self.n):
			for j in range(self.n):
				# Checking if there is an empty space
				if self.board[i][j] == ' ':
					moves.append((i, j))  # If there is an empty space we append its coordinates into the moves list

		return moves

	def check_potential_win(self, move, player):
		"""
		Check if placing a token at the specified position could potentially lead to a win.
		"""
		x, y = move

		self.make_move(move, player) # Does the move in the board but it will erase it once the cheacking is done

		# Check rows
		row_count = 0
		for j in range(self.n):
			if self.board[x][j] == player:
				row_count += 1
				if row_count == self.obj:
					self.make_move(move, ' ')
					return True
			else:
				row_count = 0

		# Check columns
		col_count = 0
		for i in range(self.n):
			if self.board[i][y] == player:
				col_count += 1
				if col_count == self.obj:
					self.make_move(move, ' ')
					return True
			else:
				col_count = 0

		# Check main diagonals
		for i in range(self.n - self.obj + 1):
			for j in range(self.n - self.obj + 1):

				# Check diagonal going from top-left to bottom-right
				count = 0
				for k in range(self.obj):
					if self.board[i + k][j + k] == player:
						count += 1
						if count == self.obj:
							self.make_move(move, ' ')
							return True

				# Check diagonal going from bottom-left to top-right
				count = 0
				for k in range(self.obj):
					if self.board[i + self.obj - k - 1][j + k] == player:
						count += 1
						if count == self.obj:
							self.make_move(move, ' ')
							return True

		# Check secondary diagonals (for non-square boards)
		if self.n != self.obj:  # Only need to check if the board is not square and obj is not equal to n
			for i in range(self.n - self.obj + 1):
				for j in range(self.obj - 1, self.n):

					# Check diagonal going from top-right to bottom-left
					count = 0
					for k in range(self.obj):
						if self.board[i + k][j - k] == player:
							count += 1
							if count == self.obj:
								self.make_move(move, ' ')
								return True

					# Check diagonal going from bottom-right to top-left
					count = 0
					for k in range(self.obj):
						if self.board[i + self.obj - k - 1][j - k] == player:
							count += 1
							if count == self.obj:
								self.make_move(move, ' ')
								return True
							
		self.make_move(move, ' ')
		return False
	
	def check_col_row(self, move, player):
		'''
		Function that  checks whether a column or row has a token of a determined token
		'''
		x, y = move

		row, col = False, False
		
		for i in range(self.n):
			
			for j in range(self.n):

				if self.board[x][j] == player:
					row = True

				elif self.board[i][y] == player:
					col = True
		
		return row, col

	def heuristic(self, move, player):
		"""
		Custom heuristic function to evaluate the desirability of a move.
		It has in account the following info:
		- If there is a winner move for the bot
		- Winner moves avaliable for the oponent (to make the bot stop them)
		- Critical positions:
			· Exact center of the board
			· Corners
			· Edges
			· Proximity to the center of the board
		- Movility (avaliable moves after  the current one)
		"""
		x, y = move
		score = 0

		# Check for potential winning moves
		if self.check_potential_win(move, player):
			score += 1000  # High score for potential wins

		# Check for blocking opponent's potential wins
		opponent = self.player2 if player == self.player1 else self.player1
		if self.check_potential_win(move, opponent):
			score += 500  # Moderate score for blocking opponent's win

		# Control of the center
		center = self.n // 2
		distance_to_center = abs(x - center) + abs(y - center)
		#score += max(0, (self.n // 2) - distance_to_center) * 10

		# Occupying critical positions (e.g., corners and edges)
		if distance_to_center == 0:
			score += 100
		elif (x, y) in [(0, 0), (0, self.n - 1), (self.n - 1, 0), (self.n - 1, self.n - 1)]:
			score += 50  # Higher score for occupying corners
			score += max(0, (self.n // 2) - distance_to_center) * 10
		elif x == 0 or x == self.n - 1 or y == 0 or y == self.n - 1:
			score += 20  # Moderate score for occupying edges
			score += max(0, (self.n // 2) - distance_to_center) * 10

		row_check, col_check = self.check_col_row(move, opponent)

		if row_check and col_check == True:
			score -= 20
		elif row_check == True or  col_check == True:
			score -= 10

		# Mobility
		num_available_moves_after = len(self.get_moves())
		score += num_available_moves_after * 5

		return score

	def min_max(self, player, depth, alpha, beta):
		'''
		Minimax algorith with Alpha-Beta Pruning optimization
		'''
		# Base case: check if the game has ended or if the depth limit has been reached
		if self.is_game_ended() or depth == 0:
			if self.check_winner(self.player1):  # If player1 wins, return a positive score
				return 1, None
			elif self.check_winner(self.player2):  # If player2 wins, return a negative score
				return -1, None
			else:  # Otherwise, it's a draw
				return 0, None

		# If it's player1's turn, initialize best_score to negative infinity
		best_score = -math.inf if player == self.player1 else math.inf
		best_move = None

		# Get all possible moves for the current player
		possible_moves = self.get_moves()

		# Sort moves based on some heuristic (e.g., center of the board first)
		possible_moves.sort(key=lambda move: self.heuristic(move, player), reverse=True)

		# For each possible move, evaluate the score using recursive min_max
		for move in possible_moves:
			# Make the move
			self.make_move(move, player)
			# Calculate the score for this move by recursively calling min_max for the other player
			score, _ = self.min_max(self.player1 if player == self.player2 else self.player2, depth - 1, alpha, beta)
			# Undo the move
			self.make_move(move, ' ')

			# Update the best_score and best_move based on the current player
			if player == self.player1:  # If it's player1's turn
				if score > best_score:
					best_score = score
					best_move = move
				alpha = max(alpha, best_score)
			else:  # If it's player2's turn
				if score < best_score:
					best_score = score
					best_move = move
				beta = min(beta, best_score)

		# Perform alpha-beta pruning
			if alpha >= beta:
				break

		return best_score, best_move

	def make_move(self, move, player):
		'''
		Function that modifies the board matrix to make the move
		Input: self, the move (i,j as positions) and which player will do the move
		'''
		i, j = move  # Separating the variable move into the 2 indices
		self.board[i][j] = player  # Modifying the pos i,j of the matrix board with the symbol of the player

	def play(self):
		'''
		Function that calls all the other functions so that it is possible to play
		'''
		os.system('cls' if os.name == 'nt' else 'clear')
		print('Welcome to N in a row\n')

		self.change_n()
		os.system('cls' if os.name == 'nt' else 'clear')
		self.change_obj()
		os.system('cls' if os.name == 'nt' else 'clear')
		self.choose_player()
		os.system('cls' if os.name == 'nt' else 'clear')
		self.represent_board()  # Representing the board

		while not self.is_game_ended():
			if self.player1 == 'X':
				m = self.ask_move()  # Player moves first so we ask for its move
				while m not in self.get_moves():  # Checking if a move is illegal
					print("Illegal move. Try again.\n")
					m = self.ask_move()  # Asking for a new move
				self.make_move(m, self.player1)  # Doing player's move
				os.system('cls' if os.name == 'nt' else 'clear')
				self.represent_board()  # Representing the board

				score, best_move = self.min_max(self.player2, depth=6, alpha=-math.inf, beta=math.inf)  # Computing the best move for the bot

				if best_move is not None:
					self.make_move(best_move, self.player2)
					self.represent_board()  # Representing the board
					print(f'The BOT moved at position {best_move[0] + 1}, {best_move[1] + 1}\n')
			
			else:
				score, best_move = self.min_max(self.player2, depth=6, alpha=-math.inf, beta=math.inf)  # Computing the best move for the bot

				if best_move is not None:
					self.make_move(best_move, self.player2)
					self.represent_board()  # Representing the board
					print(f'The BOT moved at position {best_move[0] + 1}, {best_move[1] + 1}\n')
				
				if self.is_game_ended()==True: break

				m = self.ask_move()  # Player moves first so we ask for its move
				while m not in self.get_moves():  # Checking if a move is illegal
					print("Illegal move. Try again.\n")
					m = self.ask_move()  # Asking for a new move
				self.make_move(m, self.player1)  # Doing player's move
				os.system('cls' if os.name == 'nt' else 'clear')
				self.represent_board()  # Representing the board

		if self.is_board_full():  # Checking if the board is full
			print('The board is full. No winners')
		elif self.check_winner(self.player1):  # Checking if the player has won
			print("Congratulations, you won!")
		elif self.check_winner(self.player2):  # Checking if the bot has won
			print("You lost! Better luck next time.")
		else:  # Possible errors
			print("Something unexpected has occurred. Please restart the game.")

def main():
	game = N_in_line()
	game.play()

if __name__ == "__main__":
	main()