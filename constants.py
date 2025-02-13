HEX_SIZE = 20 # Hex edge length
WIDTH, HEIGHT = 2400, 1400
GRID_RADIUS =  20

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# Hexagon grid directions (cubic)
DIRECTIONS = [
    (1, -1, 0), # Southeast, +x -y
    (1, 0, -1), # Northeast, +x -z
    (0, 1, -1), # North, +y -z
    (-1, 1, 0), # Northwest, +y -x
    (-1, 0, 1), # Southwest, +z -x
    (0, -1, 1)  # South, +z -y
]