import pygame
from settings import TILE_SIZE, COLOR_PLAYER


class Player(pygame.sprite.Sprite):
    """Jogador controlável."""
    def __init__(self, x, y, walls_group):
        super().__init__()

        self.image = pygame.Surface((TILE_SIZE - 6, TILE_SIZE - 6))
        self.image.fill(COLOR_PLAYER)
        self.rect = self.image.get_rect()
        self.rect.center = (
            x * TILE_SIZE + TILE_SIZE // 2,
            y * TILE_SIZE + TILE_SIZE // 2,
        )

        self.speed = 3
        self.walls_group = walls_group

        # Futuro: status, inventário, facção, etc.
        self.hp = 100

    def handle_input(self):
        keys = pygame.key.get_pressed()
        dx = dy = 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx = -self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy = -self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy = self.speed

        return dx, dy

    def move_and_collide(self, dx, dy):
        # Movimento no eixo X
        self.rect.x += dx
        for wall in self.walls_group:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left
                elif dx < 0:
                    self.rect.left = wall.rect.right

        # Movimento no eixo Y
        self.rect.y += dy
        for wall in self.walls_group:
            if self.rect.colliderect(wall.rect):
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                elif dy < 0:
                    self.rect.top = wall.rect.bottom

    def update(self):
        dx, dy = self.handle_input()
        self.move_and_collide(dx, dy)
