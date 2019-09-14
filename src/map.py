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

    def draw_background(self, screen, player):
        window_size = screen.get_size()
        layer_offset_x = 0
        layer_offset_y = 0

        for layer_index in range(0, 5):
            for j, tile_row in enumerate(self.layers[layer_index].tiles):
                for i, tile_index in enumerate(tile_row):
                    if tile_index == 0:
                        continue

                # rect = pygame.Rect((j * 32) - layer_offset_x, (i * 32) - layer_offset_y, CONFIG.WINDOW_WIDTH, CONFIG.WINDOW_HEIGHT)
                rect = pygame.Rect(j * 32, i * 32, window_size[0], window_size[1])
                screen.blit(self.tileset.tiles[tile_index], rect)


    def draw_foreground(self, screen, entity):
        pass
