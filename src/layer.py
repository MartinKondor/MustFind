"""
Map layer.
"""


class Layer:
    
    def __init__(self):
        self.tiles = []
        self.x_pos = 0
        self.y_pos = 0
        self.x_speed = 0
        self.y_speed = 0
        self.x_speed_auto = 0
        self.y_speed_auto = 0
        self.x_offset = 0
        self.y_offset = 0

    def set_property(self, key, value):
        if 'xOffset' == key:
            self.x_offset = float(value)
        if 'yOffset' == key:
            self.y_offset = float(value)
        if 'xSpeed' == key:
            self.x_speed = float(value)
        if 'ySpeed' == key:
            self.y_speed = float(value)
        if 'xSpeedAuto' == key:
            self.x_speed_auto = float(value)
        if 'ySpeedAuto' == key:
            self.y_speed_auto = float(value)
