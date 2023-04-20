from Item import Item


class Wall(Item):
    def __init__(self, surface, pos_x, pos_y, width, height, color):
        super().__init__(surface, pos_x, pos_y, width, height, color)
