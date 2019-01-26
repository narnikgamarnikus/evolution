import pygame
 
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
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = [[0 for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]
 
# Set row 0, cell 0 to one. (Remember rows and
# column numbers start at zero.)
grid[0][0] = 1
 
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen

WINDOW_SIZE = [
    (WIDTH + MARGIN) * GRID_SIZE + MARGIN,
    (WIDTH + MARGIN) * GRID_SIZE + MARGIN
]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Array Backed Grid")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            if pos[0] < WINDOW_SIZE[0] and pos[1] < WINDOW_SIZE[1]:
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
                if grid[row][column] == 0: 
                    grid[row][column] = 1
                else:
                    grid[row][column] = 0
                print("Click ", pos, "Grid coordinates: ", row, column)
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            rect = [
              (MARGIN + WIDTH) * column + MARGIN,
              (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT
            ]
            pygame.draw.rect(screen, color, rect)
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()