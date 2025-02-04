import math
import constants as ct

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