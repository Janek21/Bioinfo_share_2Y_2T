from pytokr import pytokr

inp = pytokr()

while True:
	max_val = int(inp())
	box_size = int(inp())
	box = []
	for x in range(box_size):
		box.append(int(inp()))
	print(box)
