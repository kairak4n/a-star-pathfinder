import pygame
import math

pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hexagonal grid (Cube Coordinates)")

# Hexagon settings
HEX_SIZE = 40 # Hex edge length
GRID_RADIUS = 3 # Size of hexagonal grid

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

# Function to compute pixel position from cube coordinates
def cube_to_pixel(x, y, z):
    px = HEX_SIZE * (3/2 * x) + WIDTH // 2
    py = HEX_SIZE * (math.sqrt(3) * -(z + x / 2)) + HEIGHT // 2
    return (px, py)