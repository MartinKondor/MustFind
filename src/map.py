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
            layer_offset_x = player.camera_x * self.layers[layer_index].x_speed + self.layers[layer_index].x_offset
            layer_offset_y = player.camera_y * self.layers[layer_index].y_speed + self.layers[layer_index].y_offset

            start_x = layer_offset_x / 32 - 2
            if start_x < 0:
                start_x = 0
            
            start_y = layer_offset_y / 32 - 2
            if start_y < 0:
                start_y = 0

            end_x = int((CONFIG.WINDOW_WIDTH + layer_offset_x) / 32)
            if end_x < len(self.layers[layer_index].tiles[0]) - 1:
                end_x = len(self.layers[layer_index].tiles[0]) - 1

            end_y = int((CONFIG.WINDOW_HEIGHT + layer_offset_y) / 32)
            if end_y < len(self.layers[layer_index].tiles) - 1:
                end_y = len(self.layers[layer_index].tiles) - 1

            for y, tiles in enumerate(self.layers[layer_index].tiles):
                if y < start_y:
                    continue
                elif y > end_y:
                    break

                for x, tile in enumerate(tiles):
                    if tile == 0 or x < start_x:
                        continue
                    elif x > end_x:
                        break

                    screen.blit(self.tileset.tiles[tile], (x * 32 - layer_offset_x, y * 32 - layer_offset_y))

    @staticmethod 
    def get_tile(map, layer, x_tile, y_tile):
        """
        :returns int: the tileid of the tile at x_tile and y_tile
        """
        x_tile, y_tile = int(x_tile), int(y_tile)

        if x_tile >= 0 and x_tile < (len(map.layers[layer].tiles[0]) - 1) and y_tile >= 0 and y_tile < (len(map.layers[layer].tiles) - 1):
            return map.layers[layer].tiles[y_tile][x_tile]
        return 0

    @staticmethod
    def is_masked_pixel(map, layer, x_pos, y_pos):
        """
        :returns bool: true if a pixel in map is masked in layer at (x_pos, yPos)
        """
        x_pos, y_pos = int(x_pos), int(y_pos)

        if x_pos >= 0 and x_pos < (len(map.layers[layer].tiles[0]) - 1) * 32 and y_pos >= 0 and y_pos < (len(map.layers[layer].tiles) - 1) * 32:
            tile_at_coords = Map.get_tile(map, layer, x_pos / 32, y_pos / 32)
            x_tile = tile_at_coords % 10
            y_tile = int(tile_at_coords / 10)
            return bool(map.tileset.mask[y_tile * 32 + y_pos % 32][x_tile * 32 + x_pos % 32])
        return True

    @staticmethod
    def is_masked_h_line(map, layer, x_pos, y_pos, length):
        """
        :returns bool: true if any pixel in map is masked in layer from (x_pos, y_pos) to (x_pos + length, y_pos)
        """
        x_pos, y_pos, length = int(x_pos), int(y_pos), int(length)

        if length >= 0: 
            for i in range(x_pos, x_pos + length):
                if Map.is_masked_pixel(map, layer, i, y_pos):
                    return True
        else:
            for i in range(x_pos - length, x_pos, -1):
                if Map.is_masked_pixel(map, layer, i, y_pos):
                    return True
        return False

    @staticmethod
    def masked_top_v_line(map, layer, x_pos, y_pos, length):
        """
        :returns int: the index of the topmost masked pixel in inMap in layer from (x_pos, y_pos) to (x_pos, y_pos + length)
        """
        x_pos, y_pos, length = int(x_pos), int(y_pos), int(length)

        for i in range(length):
            if Map.is_masked_pixel(map, layer, x_pos, y_pos + i):
                return i
        return length

    @staticmethod
    def masked_top_v_area(map, layer, x_pos, y_pos, h_length, v_length):
        """
        :returns int: the index of the topmost horizontal line it finds a masked pixel in
        """
        x_pos, y_pos, h_length, v_length = int(x_pos), int(y_pos), int(h_length), int(v_length)

        if v_length >= 0:
            for i in range(v_length):
                if Map.is_masked_h_line(map, layer, x_pos, y_pos + i, h_length):
                    return i
        else:
            for i in range(v_length, 0, -1):
                if Map.is_masked_h_line(map, layer, x_pos, y_pos + i, h_length):
                    return i
        return v_length

    @staticmethod
    def masked_first_h_area(map, layer, x_pos, y_pos, h_length, v_length):
        """
        :returns int: the index of the first vertical line it finds a masked pixel in
        """
        x_pos, y_pos, h_length, v_length = int(x_pos), int(y_pos), int(h_length), int(v_length)

        if h_length >= 0:
            for i in range(h_length):
                if Map.masked_top_v_line(map, layer, x_pos + i, y_pos, v_length):
                    return i
        else:
            for i in range(h_length, 0, -1): 
                if Map.masked_top_v_line(map, layer, x_pos + i, y_pos, v_length):
                    return i
            
        return h_length
