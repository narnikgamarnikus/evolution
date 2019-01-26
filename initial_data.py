# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

GRID_SIZE = 25
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 25
HEIGHT = 25
 
# This sets the margin between each cell
MARGIN = 1

# Set the HEIGHT and WIDTH of the screen

WINDOW_SIZE = [
    (WIDTH + MARGIN) * GRID_SIZE + MARGIN,
    (WIDTH + MARGIN) * GRID_SIZE + MARGIN
]

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = [[0 for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]
 
# Set row 0, cell 0 to one. (Remember rows and
# column numbers start at zero.)
grid[0][0] = 1