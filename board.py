from constants import HEX_SIZE, WIDTH, HEIGHT
import math

class Board:
    def __init__(self, radius):
        self.radius = radius
        self.grid = {
            (x, y, z): True 
            for x in range(-radius, radius + 1) 
            for y in range(-radius, radius + 1) 
            for z in range(-radius, radius + 1) 
            if x + y + z == 0
        }

    @staticmethod
    def cube_to_pixel(x, y, z):
        px = HEX_SIZE * (3/2 * x) + WIDTH // 2
        py = HEX_SIZE * (math.sqrt(3) * (z + x / 2)) + HEIGHT // 2
        return (px, py)
    
    def pixel_to_cube(self, px, py):
        px = px - WIDTH // 2
        py = py - HEIGHT // 2
        x = (px * 2/3) / HEX_SIZE
        z = (-1/3 * px + math.sqrt(3)/3 * py) / HEX_SIZE
        y = -x - z 
        x, y, z = self.cube_round(x, y, z)
        print("Pixels: ", px, py)
        print("Coords: ", x,y,z)
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