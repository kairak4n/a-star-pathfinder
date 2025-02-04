import pygame
import math
from board import Board
import constants as ct

# Screen settings
screen = pygame.display.set_mode((ct.WIDTH, ct.HEIGHT))
pygame.display.set_caption("Hexagonal grid (Cube Coordinates)")

board = Board(5)

def draw_hex(surface, x, y, z, color):
    px, py = board.cube_to_pixel(x, y, z)
    points = [
        (
            px + ct.HEX_SIZE * math.cos(math.pi / 3 * i),
            py + ct.HEX_SIZE * math.sin(math.pi / 3 * i)
        ) for i in range(6)
    ]
    pygame.draw.polygon(surface, color, points, 2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((ct.WIDTH, ct.HEIGHT))
    clock = pygame.time.Clock()

    grid = {(x, y, z): True for x in  range(-5, 6) for y in range(-5, 6) for z in range(-5, 6) if x + y + z == 0}
    start, end = None, None

    running = True
    while running:
        screen.fill(ct.WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                x, y, z = board.pixel_to_cube(mx, my)
        
        for (x, y, z) in grid:
            color = ct.BLACK
            draw_hex(screen, x, y, z, color)
        
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()