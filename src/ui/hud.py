import pygame
from settings import COLOR_TEXT


def draw_ui(screen, player):
    """Desenha uma HUD bem simples (HP no canto)."""
    font = pygame.font.SysFont("arial", 18)
    hp_text = font.render(f"HP: {player.hp}", True, COLOR_TEXT)
    screen.blit(hp_text, (10, 10))
