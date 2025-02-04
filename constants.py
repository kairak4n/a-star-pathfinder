HEX_SIZE = 40 # Hex edge length
WIDTH, HEIGHT = 1200, 800

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 100, 255)

# Hexagon grid directions (cubic)
DIRECTIONS = [
    (1, -1, 0), # Southeast, +x -y
    (1, 0, -1), # Northeast, +x -z
    (0, 1, -1), # North, +y -z
    (-1, 1, 0), # Northwest, +y -x
    (-1, 0, 1), # Southwest, +z -x
    (0, -1, 1)  # South, +z -y
]