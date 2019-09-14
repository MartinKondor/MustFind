"""
Tileset for maps.
"""
import os
import zipfile

import pygame

from consts import TILESET_FOLDER


class Tileset:

    def __init__(self):
        self.mask = []
        self.tiles = []
        self.image = None

    def load_mask(self, file_name):
        mask_file = open(file_name, 'r')
        mask_content = mask_file.read()
        mask_file.close()
        
        for line in mask_content.splitlines():
            if not line or line.isspace():
                continue
            
            self.mask.append([int(val) for val in list(line) if val])

    def load(self, file_name):
        should_extract = True
        cache_file_name = TILESET_FOLDER + 'cache/info.txt'

        # Check cache for exsisting files
        if os.path.exists(cache_file_name) and os.path.isfile(cache_file_name):
            with open(cache_file_name, 'r') as file:
                lines = [line for line in file.read().splitlines() if line and not line.isspace()]
                parts = [p.strip() for p in lines[0].strip().split('=') if p and not p.isspace()]
                
                if parts[0] == 'file' and parts[1] == file_name:
                    should_extract = False

        if should_extract:

            # Extract zip file to the 'TILESET_FOLDER + cache'
            tct_file = zipfile.ZipFile(file_name, 'r')
            tct_file.extractall(TILESET_FOLDER + 'cache')
            tct_file.close()

            # Put an info file here to
            # not extract the same files again
            info = open(cache_file_name, 'w+')
            info.write('file=' + file_name)
            info.close()

        # Load tileset files from cache
        self.load_mask(TILESET_FOLDER + 'cache/mask.msk')
        self.image = pygame.image.load(TILESET_FOLDER + 'cache/image.png')

        # Load the tileset matrix
        img_size = self.image.get_size()

        for j in range(int(img_size[1] / 32)):
            for i in range(10):
                self.image.set_clip(pygame.Rect(i * 32, j * 32, 32, 32))
                self.tiles.append(self.image.subsurface(self.image.get_clip()))
