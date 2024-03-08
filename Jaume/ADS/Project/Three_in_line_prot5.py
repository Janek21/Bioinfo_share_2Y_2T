import sys
import math

class N_in_line(object):

	def __init__(self):
		
		self.n = 3 # Setting 3 as deffault
		self.obj = 3

		# Creation of a matrix n*n representing the board (default: 3*3)
		self.board = [[' ' for _ in range(self.n)] for _ in range(self.n)] 
		
		# Initializing the players
		self.player1 = ''  
		self.player2 = ''
		
	def change_n(self):

		print("Please enter the nº of rows and columns you want the board to have")

		n = sys.stdin.readline().strip()

		if n.isspace(): # If  no value is entered, keeping the default one
			pass

		elif  not n.isdigit(): # Checking if the input is a digit

			print('Invalid input. Try again.\n')
			self.change_n()

		else:

			n = int(n) # Transforming into integer

			self.n = n # Changing n inside the class

			self.board = [[' ' for _ in range(self.n)] for _ in range(self.n)] # Creation of the n*n board
			print(f"You have selected a {self.n}x{self.n} board\n")

	def change_obj(self):

		print("Please enter the nº of tokens in a row to win")

		n = sys.stdin.readline().strip()

		if n.isspace(): # If  no value is entered, keeping the default one
			pass

		elif  not n.isdigit(): # Checking if the input is a digit

			print('Invalid input. Try again.\n')
			self.change_n()

		elif int(n) > self.n:

			print(f'The nº of tokens in a row of your input is too high. Try again\n')
			self.change_obj()

		else:

			n = int(n) # Transforming into integer

			self.obj = n # Changing n inside the class

			print(f"To win you need {self.obj} tokens in a row to win\n")

	def represent_board(self):

		'''
		Function that allows us to visualize the board
		'''
		line = '-' * self.n + '-' * (self.n - 1) # Calculating the nº of dashes needed for each line depending on n
		print(line)

		# Iterating through each of the n rows of the board
		for row in self.board:
			
			# Representation of the board:
			print('|'.join(row))
			print(line)

		print() # Empty line as separator
			
	def is_board_full(self):

		'''
		Function that check if the board is full (no more space to put a piece)
		Output: True / False
		'''

		# Iterating throug each cell of the matrix
		for i in range(self.n):

			for j in range(self.n):

				# Cheking if there is an empty cell in the board
				if self.board[i][j] == ' ':

					return False # If so the board is not false and we return False

		return True

	def is_game_ended(self):

		'''
		Function that checks if the game has ended (to know when to finish the game)
		It does so by ckecking if the board is full or if one of the players has won
		Output: True / False
		'''

		# Cheking if one of the players have won and if the board is full or not
		return self.check_winner(self.player1) or self.check_winner(self.player2) or self.is_board_full()

	def check_winner(self, player):
		"""
		Function that takes self and the player as arguments and tells us if a determined player is the winner or not.
		Output: True / False
		"""
		# Initialize counters for rows, columns, and diagonals
		for i in range(self.n):
			row_count = 0
			col_count = 0
			for j in range(self.n):
				# Counting player symbols in rows and columns
				if self.board[i][j] == player:
					row_count += 1
					if row_count == self.obj:
						return True
				if self.board[j][i] == player:
					col_count += 1
					if col_count == self.obj:
						return True

		# Checking diagonals
		main_diag_count = 0
		sec_diag_count = 0
		for i in range(self.n):
			if self.board[i][i] == player:
				main_diag_count += 1
				if main_diag_count == self.obj:
					return True
			if self.board[i][self.n - i - 1] == player:
				sec_diag_count += 1
				if sec_diag_count == self.obj:
					return True

		# Check other diagonals
		for i in range(self.n - self.obj + 1):  # Iterate over rows
			for j in range(self.n - self.obj + 1):  # Iterate over columns
				# Check diagonal going from bottom-left to top-right
				count = 0
				for k in range(self.obj):
					if self.board[i + k][j + k] == player:
						count += 1
				if count == self.obj:
					return True
				# Check diagonal going from top-left to bottom-right
				count = 0
				for k in range(self.obj):
					if self.board[i + self.obj - k - 1][j + k] == player:
						count += 1
				if count == self.obj:
					return True

		return False  # If the function continues until here it means that the player has not won so returning False

	def ask_move(self):

		print("Please do your move (Input example: '>>>i j')")

		move = sys.stdin.readline().strip().split() # Getting and formating input from stdin
		print() # Formatting output

		if  len(move) != 2:
			print("Invalid input. Try again.\n")
			self.ask_move()
		
		elif not move[0].isdigit() or not move[1].isdigit(): # Checking that the input is correct

			print("Invalid input. Try again.\n")
			self.ask_move()
		
		else:
			return int(move[0])-1, int(move[1])-1 # Returning the coordinates (User frendly) if the input is correct
	
	def choose_player(self):

		print('Chose your symbol: X / O (Upper)')
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

		print() # Formatting the output (empty line)

	def get_moves(self):
		'''
		Function that looks for all the possible moves for the bot
		'''

		moves = [] # Creating empty list to store all the legal moves

		# Iterating through each cell of the board matrix
		for i in range(self.n):

			for j in range(self.n):
				
				# Checking if there is an empty space
				if self.board[i][j] == ' ':
					
					moves.append((i, j)) # If there is an empty space we append it's coordinates into the moves list

		return moves
	
	def min_max(self, player, depth, alpha, beta):

		'''
		Function that implements the min max with alpha and beta prouring algorithm to select the best movement
		It will decide which move of the possible moves is the best
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
		if player == self.player1:
			best_score = -math.inf
		else:  # If it's player2's turn, initialize best_score to positive infinity
			best_score = math.inf

		best_move = None

		# Get all possible moves for the current player
		possible_moves = self.get_moves()

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

		i, j = move # Separing the variable move into the 2 indices

		self.board[i][j] = player # Modifying the pos i,j of the matrix board with the symbol of the player
	
	def play(self):
		'''
		Function that calls all the other functions so that it is possible to play
		'''
		print('Welcome to N in a row\n')

		self.change_n() # 

		self.change_obj()

		self.choose_player()
		
		self.represent_board() # Representing the board

		while self.is_game_ended() == False:

			m = self.ask_move() # Player moves first so we ask for it's move

			while m not in self.get_moves(): # Checking if a move is illegal

				print("Illegal move. Try again.\n")

				m = self.ask_move() # Aking for a new move
			
			self.make_move(m, self.player1) # Doing player's move

			self.represent_board() # Representing the board
			
			score, best_move = self.min_max(self.player2, depth=self.n, alpha=-math.inf, beta=math.inf) # Computing the best move for the bot
			
			if best_move is not None:
				self.make_move(best_move, self.player2)
				self.represent_board() # Representing the board

		if self.is_board_full(): # Checking if the board is full

			print('The board is full. No winners')

		elif self.check_winner(self.player1): # Checking if the player has won

			print("Congralutations, you won!")

		elif self.check_winner(self.player2): # Checking if the bot has won

			print("You lost! Better luck next time.")

		else: # Possible errors
			print("Something unexpected has occurred. Please restart de game.")

def main():
	game = N_in_line()

	game.play()

if __name__ == "__main__":
	
	main()