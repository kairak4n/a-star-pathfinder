import pygame
import math
from board import Board
import constants as ct
from node import Node

# Screen settings
screen = pygame.display.set_mode((ct.WIDTH, ct.HEIGHT))
pygame.display.set_caption("A* Path Finding Algorithm")

board = Board(5)

def main():
    pygame.init()
    screen = pygame.display.set_mode((ct.WIDTH, ct.HEIGHT))
    clock = pygame.time.Clock()

    start, end = None, None
    running = True
    started = False
    while running:
        board.draw_grid(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if started:
                continue
            if pygame.mouse.get_pressed()[0]:
                # left mouse button pressed
                pos = pygame.mouse.get_pos()
                x, y, z = board.pixel_to_cube(pos[0], pos[1])
                node = board.grid[x, y, z]
                if not start and node != end:
                    start = node
                    start.make_start()
                elif not end and node != start:
                    end = node
                    end.make_end()
                elif node != start and node != end:
                    node.make_barrier()
            elif pygame.mouse.get_pressed()[2]:
                # right mouse button pressed
                pos = pygame.mouse.get_pos()
                x, y, z = board.pixel_to_cube(pos[0], pos[1])
                node = board.grid[x, y, z]
                if node == start:
                    start = None
                elif node == end:
                    end = None
                node.reset()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                x, y, z = board.pixel_to_cube(mx, my)
        
        board.draw_grid(screen)
        
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()