import math

class Three_in_line(object):

	def __init__(self):

		self.board = [[' ' for _ in range(3)] for _ in range(3)] # Creation of a matrix 3*3 representing the board
		
		# Assigning symbols to represent the "fichas" of the players
		self.player1 = 'X'  
		self.player2 = 'O' 

	def represent_board(self):

		'''
		Function that allows us to visualize the board
		'''

		print(f'Board:\n')

		print('-----')

		# Iterating through each of the 3 rows of the board
		for row in self.board:
			
			# Representation of the board:
			print('|'.join(row))
			print('-----')
			
	def is_board_full(self):

		'''
		Function that check if the board is full (no more space to put a piece)
		Output: True / False
		'''

		return

	def is_game_ended(self):

		'''
		Function that checks if the game has ended
		It does so by ckecking if the board is full or if one of the players has won
		Output: True / False
		'''

		return

	def check_winner(self, player):
	
		'''
		Function that takes self and the player as arguments and tells us if a determined player is  winner or not.
		Output: True / False
		'''

		# Iterating through each row
		for i in range(3):

			# Checking if the  current row has all elements equal to the given player
			if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
			
				return True # If the condition is met the player has won and we return True
	
		# Iterating through each column
		for j in range(3):
		
			# Checking if the  current row has all elements equal to the given player
			if self.board[0][j] == self.board[1][j] == self.board[2][j] == player:
			
				return True # If so we asume that the player has won and we return True
	
		# Checking the 2 possible diagonals using coordinates
		if self.board[0][0] == self.board[1][1] == self.board[2][2] == player or \
		   self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
		
			return True # If one of the diagonals have the same symbol the player has won and therefore e return True
	
		return False # If any of the conditions above are met the player has not won and we return False

	def evaluate(self):

		'''
		Function that checks if one of the players has won using the previous function check_winner

		Useful to implement it in the algorithm --> Three possible results: p1 won / p2 won / no winner
		'''

		return

	def get_moves(self):
		'''
		Function that creates all the possible moves for the bot
		'''

		return
	
	def algorithm_name(self):

		'''
		Function that has the logic of the bot
		It will decide which move of the possible moves is the best
		'''

		return
	
	def make_move(self, move, player):

		'''
		Function that modifies the board matrix to make the move

		Input: self, the move a player wants to do and which player will do the move
		'''

		return
	
	def play(self):
		
		'''
		Function that implements all the other functions so that it is possible to play
		'''

		return

def main():

	game = Three_in_line()

	game.represent_board()

if __name__ == "__main__":
	main()