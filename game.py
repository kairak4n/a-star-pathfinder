import pygame
import math

pygame.init()

# Screen settings
WIDTH, HEIGHT = 1200, 800
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

# Function to compute pixel position of the center of the hexagon
def cube_to_pixel(x, y, z):
    px = HEX_SIZE * (3/2 * x) + WIDTH // 2
    py = HEX_SIZE * (math.sqrt(3) * (z + x / 2)) + HEIGHT // 2
    return (px, py)

def pixel_to_cube(px, py):
    px = px - WIDTH // 2
    py = py - HEIGHT // 2
    x = (px * 2/3) / HEX_SIZE
    z = (-1/3 * px + math.sqrt(3)/3 * py) / HEX_SIZE
    y = -x - z 
    x, y, z = cube_round(x, y, z)
    print("Pixels: ", px, py)
    print("Coords: ", x,y,z)
    return cube_round(x, y, z)

def cube_round(x, y, z):
    rx, ry, rz = round(x), round(y), round(z)
    dx, dy, dz = abs(rx - x), abs(ry - y), abs(rz - z)

    if dx > dy and dx > dz:
        rx = -ry - rz
    elif dy > dz:
        ry = -rx - rz
    else:
        rz = -rx - ry
    
    return rx, ry, rz

def draw_hex(surface, x, y, z, color):
    px, py = cube_to_pixel(x, y, z)
    points = [
        (
            px + HEX_SIZE * math.cos(math.pi / 3 * i),
            py + HEX_SIZE * math.sin(math.pi / 3 * i)
        ) for i in range(6)
    ]
    pygame.draw.polygon(surface, color, points, 2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    grid = {(x, y, z): True for x in  range(-5, 6) for y in range(-5, 6) for z in range(-5, 6) if x + y + z == 0}
    start, end = None, None

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                x, y, z = pixel_to_cube(mx, my)
        
        for (x, y, z) in grid:
            color = BLACK
            draw_hex(screen, x, y, z, color)
        
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()