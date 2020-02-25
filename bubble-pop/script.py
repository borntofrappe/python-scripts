import pygame
from entities import Player, Enemy, Bullet

game = {
    "title": "PoP",
    "background": (40, 40, 40),
    "width": 700,
    "height": 450
}

player = Player(game["width"] // 2, game["height"])
bullets = []
enemies = []
columns = 10
rows = 3
for row in range(rows):
    for column in range(columns):
        y = 20 + game["height"] // 2 // rows * row
        x = 20 + game["width"] // columns * column
        enemy = Enemy(x, y)
        enemies.append(enemy)

# setup
pygame.init()
screen = pygame.display.set_mode((game["width"], game["height"]))

pygame.display.set_caption(game["title"])
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
speed = 0
# game loop
running = True
while running:
    speed += 1
    if speed >= 4:
        speed = 0
        if player.is_moving:
            player.update()

        for bullet in bullets:
            bullet.update()

        for enemy in enemies:
            enemy.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.stop()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if not player.is_moving:
                    player.move_left()
                    player.move()
            if event.key == pygame.K_RIGHT:
                if not player.is_moving:
                    player.move_right()
                    player.move()

            if event.key == pygame.K_UP and len(bullets) < player.bullets:
                bullet = Bullet(player.x, player.y - player.r)
                bullets.append(bullet)

            if event.key == pygame.K_q:
                running = False
            if event.key == pygame.K_n:
                enemy = Enemy(20, 20)
                enemies.append(enemy)

    # boundaries
    if player.x < 0:
        player.stop()
        player.x = 0

    if player.x > game["width"]:
        player.stop()
        player.x = game["width"]

    screen.fill(game["background"])

    pygame.draw.circle(screen, player.color, [
                       player.x, player.y], player.r, player.w)

    for bullet in bullets:
        pygame.draw.circle(screen, bullet.color, [
                           bullet.x, bullet.y], bullet.r, bullet.w)
        if bullet.y <= 0:
            bullets.remove(bullet)

        for enemy in enemies:
            if bullet.x > enemy.x - enemy.r and bullet.x < enemy.x + enemy.r and bullet.y < enemy.y + enemy.r and bullet.y > enemy.y - enemy.r:
                bullets.remove(bullet)
                enemies.remove(enemy)

    for enemy in enemies:
        if enemy.x < 0:
            enemy.x = 0
            enemy.bounce()
        if enemy.x > game["width"]:
            enemy.x = game["width"]
            enemy.bounce()

        if enemy.y > game["height"] - 20:
            running = False

        pygame.draw.circle(screen, enemy.color, [
                           enemy.x, enemy.y], enemy.r, enemy.w)

    # update
    pygame.display.update()
