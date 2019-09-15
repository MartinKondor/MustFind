"""
Map classes for loading and storing maps/tilesets.
"""
import pygame

from consts import TILESET_FOLDER
from layer import Layer
from tileset import Tileset
from config import CONFIG


class Map:
    """
    Represents the map for the game.
    
    Example usage:
    ```
    import map
    default_map = map.Map(MAP_FOLDER + 'sky.tcm')
    print(default_map)
    ```
    """

    def __init__(self, file_name):
        self.tileset = Tileset()
        self.layers = []

        # Reading from file
        lines = None
        file = open(file_name, 'r')
        lines = file.read()
        file.close()
        lines = lines.splitlines()

        current_layer = Layer()
        in_a_layer = False
        in_a_tile = False
        is_tile_set_loaded = False

        # Parse file line by line
        for line in lines:
            if not line or line.isspace():
                continue

            # Load tileset
            if not is_tile_set_loaded and line.split('=')[0].strip() == 'tileset_file':
                self.tileset.load(TILESET_FOLDER + line.split('=')[1].strip())
                is_tile_set_loaded = True
                continue

            if line.strip() == '{':
                in_a_layer = True
                continue
            elif line.strip() == '}':
                self.layers.append(current_layer)
                current_layer = Layer()
                in_a_layer = False
                continue

            if not in_a_layer:
                continue

            if line.strip() == '[':
                in_a_tile = True
                continue
            elif line.strip() == ']':
                in_a_tile = False
                continue

            if not in_a_tile:
                # We are not in a tile but in a layer,
                # so let's parse in the properties of the layer
                parts = line.strip().split('=')

                if len(parts) != 2:
                    continue

                current_layer.set_property(parts[0].strip(), parts[1].strip())
                continue

            # Parse in a tilerow
            tile_row = [int(val.strip()) for val in line.strip().split(',') if val]
            current_layer.tiles.append(tile_row)

    def draw(self, screen, player, from_layer_index=0, to_layer_index=5):
        """
        Draw the tiles what the user can see.
        """
        for layer_index in range(from_layer_index, to_layer_index):
            for y, tiles in enumerate(self.layers[layer_index].tiles):
                for x, tile in enumerate(tiles):
                    if tile == 0:
                        continue

                    screen.blit(self.tileset.tiles[tile], (x * 32, y * 32))

        """
        start_x = 0
        start_y = 0
        end_x = 0
        end_y = 0
        layer_offset_x = 0
        layer_offset_y = 0
        inCamX = 0
        inCamY = 0

        for layer_index in range(from_layer_index, to_layer_index):
            layer_offset_x = inCamX * (self.layers[layer_index].x_speed - 1)
            layer_offset_y = inCamY * (self.layers[layer_index].y_speed - 1)

            start_x = int((inCamX + layer_offset_x) / 32 - 1)
            if start_x < 0:
                start_x = 0

            start_y = int((inCamY + layer_offset_y) / 32 - 1)
            if start_y < 0:
                start_y = 0

            end_x = int((inCamX + CONFIG.WINDOW_WIDTH + layer_offset_x) / 32)
            if end_x > len(self.layers[layer_index].tiles[0]) - 1:
                end_x = len(self.layers[layer_index].tiles[0]) - 1
            
            end_y = int((inCamY + CONFIG.WINDOW_HEIGHT + layer_offset_y) / 32)
            if end_y > len(self.layers[layer_index].tiles) - 1:
                end_y = len(self.layers[layer_index].tiles) - 1

            for y in range(start_y, end_y):
                for x in range(start_x, end_x):
                    screen.blit(self.tileset.tiles[y][x], (x * 32, y * 32))
        """
