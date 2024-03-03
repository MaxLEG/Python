import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        """create new bullet and include in groupe of bullets"""
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
        elif event.key == pygame.K_q:
            sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


"""         elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship) """


def update_screen(ai_settings, screen, ship, alien, bullets):
    """update screen images and update screen"""
    screen.fill(ai_settings.bg_color)
    """All bullets are displayed behind the images of the ship and the aliens"""
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    """all bullets printing """
    ship.blitme()
    aliens.draw(screen)
    alien.blitme()
    """display the last drawn screen"""
    pygame.display.flip()


def update_bullets(bullets):
    """updates bullets positions and destroys old bullets"""


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determines the number of rows that fit on the screen.""" ""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_fleet(ai_settings, alien_width):
    """create a fleet of aliens"""
    """create of alien and calculate number of aliens in line"""

    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_numberь row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    """creating 1st line of alien"""
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, alien_number)
