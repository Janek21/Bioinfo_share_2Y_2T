
class Board:
	"""
	Board for a backtracking N-queens exercise
	Main goal is to allow for a very clear backtracking program
	"""
	
	def __init__(self):
		"""
		See Wirth PASCAL solution on Wikipedia
		(except that sets are used instead of bool arrays,
		and that rows and columns are indexed from 0)
		Queens will come one per row
		We keep track of covered columns and diagonals
		x: positions of placed queens in top rows
		a: covered columns
		c: covered main diagonals "i-j == constant"
		b: covered secondary diagonals "i+j == constant"
		Size given by length of x (number of queens)
		"""
		self.x = []
		self.a = set() 
		self.b = set()
		self.c = set()
	
	def free(self, i, j):
		"""
		Is position row == i, column == j free?
		Since no other queen at same row, just check column and diags
		"""
		return j not in self.a and \
		   i + j not in self.b and \
		   i - j not in self.c

	def put_q(self, i, j):
		"""
		Put a new queen at position row == i, column == j
		Row is always first empty row
		"""
		self.x.append(j)
		self.a.add(j)
		self.b.add(i + j)
		self.c.add(i - j)

	def remove_q(self, i, j):
		"""
		Remove existing queen, leave free column and diagonals
		Row is always last nonempty row
		"""
		self.x.pop()
		self.a.remove(j)
		self.b.remove(i + j)
		self.c.remove(i - j)

	def draw(self):
		N = len(self.x) # board size
		print('._' + ' _' * (N - 1) + ' .')
		for c in self.x:
			print('|' + '_ ' * c + '_Q' + '_ ' * (N - c  - 1) + '|')
		print()
		print()


def attempt(row, board, size):
	"""
	Recursive backtracking procedure
	Try finding a position for a queen in that row of the board, 
	and then in all subsequent rows
	Report all solutions found
	"""
	if row == size:
		"all queens set, report solution and keep searching"
		board.draw()
	else:
		for column in range(size):
			if board.free(row, column):
				board.put_q(row, column)
				attempt(row + 1, board, size)
				board.remove_q(row, column)



if __name__ == "__main__":
	board = Board()
	size = int(input("How many queens? "))
	attempt(0, board, size)
