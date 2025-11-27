import pygame
from settings import TILE_SIZE, COLOR_FLOOR, COLOR_WALL


class Tile(pygame.sprite.Sprite):
    """Tile simples (chão ou parede)."""
    def __init__(self, x, y, tile_type):
        super().__init__()
        self.tile_type = tile_type

        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        if tile_type == "wall":
            self.image.fill(COLOR_WALL)
        else:
            self.image.fill(COLOR_FLOOR)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x * TILE_SIZE, y * TILE_SIZE)


def load_level(map_path, all_sprites, walls, floors):
    """
    Lê o arquivo de mapa e cria os tiles.
    Caracteres:
      # = parede
      . = chão
      P = ponto de spawn do player (chão + spawn)
    """
    spawn_x, spawn_y = 3, 3  # padrão caso não tenha 'P'

    with open(map_path, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]

    for y, row in enumerate(lines):
        for x, char in enumerate(row):
            if char == "#":
                tile = Tile(x, y, "wall")
                walls.add(tile)
                all_sprites.add(tile)
            elif char == ".":
                tile = Tile(x, y, "floor")
                floors.add(tile)
                all_sprites.add(tile)
            elif char == "P":
                tile = Tile(x, y, "floor")
                floors.add(tile)
                all_sprites.add(tile)
                spawn_x, spawn_y = x, y

    return spawn_x, spawn_y
