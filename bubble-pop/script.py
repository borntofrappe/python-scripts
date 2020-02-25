import pygame
from circle import Circle

# game dict
game = {
    "title": "Bubble Pop",
    "background": (255, 255, 255),
    "width": 600,
    "height": 600
}

# game entities
player = Circle(game["width"] / 2, game["height"])
bullets = []

# setup
pygame.init()
screen = pygame.display.set_mode((game["width"], game["height"]))

pygame.display.set_caption(game["title"])
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# game loop
running = True
while running:
    # react to events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # stop player when the left/right key are released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.stop()

        # update the horizontal direction and enable the movement when the left/right key are pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if not player.is_moving:
                    player.move_left()
                    player.move()
            if event.key == pygame.K_RIGHT:
                if not player.is_moving:
                    player.move_right()
                    player.move()

            if event.key == pygame.K_UP:
                bullet = Circle(player.x, player.y, 5, 0)
                bullets.append(bullet)

    screen.fill(game["background"])

    # player
    if player.is_moving:
        player.update()
    pygame.draw.circle(screen, player.color, [
                       player.x, player.y], player.r, player.w)

    # bullets
    # remove the shape when it exceeds the height of the screen
    for bullet in bullets:
        bullet.move_up()
        pygame.draw.circle(screen, bullet.color, [
                           bullet.x, bullet.y], bullet.r, bullet.w)
        if bullet.y <= 0:
            bullets.remove(bullet)

    # update
    pygame.display.update()
