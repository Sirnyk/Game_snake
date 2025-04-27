import pygame

class Field:
    def __init__(self, x, y, side, block_side):
        self.x = x
        self.y = y
        self.side = side
        self.block_side = block_side