import constants as ct
import math
import pygame

class Node:
    def __init__(self, x, y, z, total_rows):
        self.x = x
        self.y = y
        self.z = z
        self.px, self.py = self.cube_to_pixel(x, y, z)
        self.color = ct.WHITE
        self.neighbours = []
        self.total_rows = total_rows
    
    @staticmethod
    def cube_to_pixel(x, y, z):
        px = ct.HEX_SIZE * (3/2 * x) + ct.WIDTH // 2
        py = ct.HEX_SIZE * (math.sqrt(3) * (z + x / 2)) + ct.HEIGHT // 2
        return (px, py)

    def get_pos(self):
        return self.x, self.y, self.z

    def is_closed(self):
        return self.color == ct.RED

    def is_open(self):
        return self.color == ct.GREEN
    
    def is_barrier(self):
        return self.color == ct.BLACK
    
    def is_start(self):
        return self.color == ct.ORANGE
    
    def is_end(self):
        return self.color == ct.TURQUOISE
    
    def reset(self):
        self.color = ct.WHITE
    
    def make_closed(self):
        self.color = ct.RED

    def make_open(self):
        self.color = ct.GREEN

    def make_barrier(self):
        self.color = ct.BLACK
    
    def make_start(self):
        self.color = ct.ORANGE
    
    def make_end(self):
        self.color = ct.TURQUOISE
    
    def make_path(self):
        self.color = ct.PURPLE

    def draw(self, win):
        points = [
            (
                self.px + ct.HEX_SIZE * math.cos(math.pi / 3 * i),
                self.py + ct.HEX_SIZE * math.sin(math.pi / 3 * i)
            ) for i in range(6)
        ]
        pygame.draw.polygon(win, self.color, points)
        pygame.draw.polygon(win, ct.BLACK, points, 2)
    
    def update_neighbours(self, grid):
        pass

    def __lt__(self, other):
        return False