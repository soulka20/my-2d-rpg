import sys
from pathlib import Path

import pygame

from settings import WIDTH, HEIGHT, FPS, COLOR_BG
from world.tiles import load_level
from entities.player import Player
from ui.hud import draw_ui


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("RPG 2D - Esqueleto")
        self.clock = pygame.time.Clock()

        # Grupos de sprites
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()

        # Câmera
        self.camera_x = 0
        self.camera_y = 0

        self.player = None

        # Caminho do mapa (baseado na raiz do projeto)
        base_dir = Path(__file__).resolve().parent.parent
        map_path = base_dir / "data" / "maps" / "map1.txt"

        # Carrega o mapa e cria o player
        spawn_x, spawn_y = load_level(map_path, self.all_sprites,
                                      self.walls, self.floors)
        self.player = Player(spawn_x, spawn_y, self.walls)
        self.all_sprites.add(self.player)

    def update_camera(self):
        # Câmera centrada no player (sem suavização)
        self.camera_x = self.player.rect.centerx - WIDTH // 2
        self.camera_y = self.player.rect.centery - HEIGHT // 2

    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)

            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Lógica
            self.all_sprites.update()
            self.update_camera()

            # Desenho
            self.draw()

        pygame.quit()
        sys.exit()

    def draw(self):
        self.screen.fill(COLOR_BG)

        # Pisos
        for tile in self.floors:
            self.screen.blit(
                tile.image,
                (tile.rect.x - self.camera_x, tile.rect.y - self.camera_y),
            )

        # Paredes
        for wall in self.walls:
            self.screen.blit(
                wall.image,
                (wall.rect.x - self.camera_x, wall.rect.y - self.camera_y),
            )

        # Player
        self.screen.blit(
            self.player.image,
            (self.player.rect.x - self.camera_x,
             self.player.rect.y - self.camera_y),
        )

        # HUD
        draw_ui(self.screen, self.player)

        pygame.display.flip()


if __name__ == "__main__":
    Game().run()
