import math
import constants as ct
from node import Node
import pygame
from queue import PriorityQueue

class Board:
    def __init__(self, radius):
        self.radius = radius
        self.grid = self.make_grid()

    @staticmethod
    def cube_to_pixel(x, y, z):
        px = ct.HEX_SIZE * (3/2 * x) + ct.WIDTH // 2
        py = ct.HEX_SIZE * (math.sqrt(3) * (z + x / 2)) + ct.HEIGHT // 2
        return (px, py)
    
    def pixel_to_cube(self, px, py):
        px = px - ct.WIDTH // 2
        py = py - ct.HEIGHT // 2
        x = (px * 2/3) / ct.HEX_SIZE
        z = (-1/3 * px + math.sqrt(3)/3 * py) / ct.HEX_SIZE
        y = -x - z 
        x, y, z = self.cube_round(x, y, z)
        return self.cube_round(x, y, z)

    @staticmethod
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

    @staticmethod
    def h(n1, n2):
        x1, y1, z1 = n1.get_pos()
        x2, y2, z2 = n2.get_pos()
        ax, ay, az = abs(x1 - x2), abs(y1 - y2), abs(z1 - z2)
        return max(ax, ay, az)

    def astar(self, draw, grid, start, end):
        count = 0
        open_set = PriorityQueue()
        open_set.put((0, count, start))
        came_from = {}
        g_score = { grid[coord]: float("inf") for coord in grid}
        g_score[start] = 0
        f_score = { grid[coord]: float("inf") for coord in grid}
        f_score[start] = self.h(start, end)

        open_set_hash = {start}

        while not open_set.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            current = open_set.get()[2]
            open_set_hash.remove(current)

            if current == end:
                while current != start:
                    current.make_path()
                    current = came_from[current]
                print('path found')
                return True

            for neighbour in current.neighbours:
                temp_g_score = g_score[current] + 1
                if temp_g_score < g_score[neighbour]:
                    g_score[neighbour] = temp_g_score
                    f_score[neighbour] = temp_g_score + self.h(neighbour, end)
                    came_from[neighbour] = current
                    if neighbour not in open_set_hash:
                        count += 1
                        open_set.put((f_score[neighbour], 1, neighbour))
                        open_set_hash.add(neighbour)
                        neighbour.make_open()
            
            draw()

            if current != start:
                current.make_closed()
        print('path not found')
        return False


    def make_grid(self):
        grid = {}
        r = self.radius
        for x in range(-r, r + 1):
            for y in range(-r, r + 1):
                for z in range(-r, r + 1):
                    if x + y + z == 0:
                        grid[(x, y, z)] = Node(x, y, z, self.radius)
        return grid

    def draw_grid(self, win):
        win.fill(ct.WHITE)
        for pos in self.grid:
            self.grid[pos].draw(win)
        pygame.display.update()
