# ---------
# CONSTANTS
# ---------

# --- PIXELS ---

WIDTH = 600
HEIGHT = 600

ROWS = 4
COLS = 4
SQSIZE = WIDTH // COLS

LINE_WIDTH = 15
CIRC_WIDTH = 15
CROSS_WIDTH = 20

RADIUS = SQSIZE // 4

OFFSET = 50

# --- COLORS ---

LINE_COLOR = (23, 145, 135)
CIRC_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

w = [(CIRC_COLOR[pos] + CROSS_COLOR[pos])/2 for pos in range(3)]

BG_COLOR = (w[0], w[1], w[2])
LINE_COLOR = (w[0]-20, w[1]-20, w[2]-20)
print(BG_COLOR)
