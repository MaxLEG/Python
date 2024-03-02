import sys
import pygame


def run_game():
    """initialazes the game and creates a screen object"""
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    """assign background color"""
    bg_color = (230, 230, 230)
    """start he main game loop"""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                """each reloop the screen is redrawn"""
                screen.fill(bg_color)
        """display the last drawn screen"""
        pygame.display.flip()


run_game()
