import pygame
from random import randint
from entities import Player, Enemy, Bullet

# game setup
game = {
    "title": "Shoot!",
    "background": (40, 40, 40),
    "width": 700,
    "height": 450
}

player = Player(game["width"] // 2, game["height"])
bullets = []
squadron = []


def rand_x(n, r, dx):
    if dx == 1:
        return randint(r, game["width"] - r * n)
    else:
        return randint(r * 2, game["width"] - r)


def rand_y():
    return randint(0, game["height"] // 3)


def rand_dx():
    rand = randint(0, 1)
    if rand == 0:
        return 1
    else:
        return -1


def add_enemies():
    n = randint(3, 7)
    dx = rand_dx()
    r = 15
    x_0 = rand_x(n, r, dx)
    y = rand_y()
    enemies = []

    for i in range(n):
        x = x_0 + (r * n - r * i) * dx
        enemy = Enemy(x, y, r - i, 0, dx)
        enemies.append(enemy)
    squadron.append(enemies)


add_enemies()
add_enemies()

# window setup
pygame.init()
screen = pygame.display.set_mode((game["width"], game["height"]))

pygame.display.set_caption(game["title"])
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)


# cheeky way to update the integer position at a slower rate
speed = 0
# game loop
running = True
while running:
    # update game entities
    speed += 1
    if speed >= 5:
        speed = 0
        if player.is_moving:
            player.update()

        for bullet in bullets:
            bullet.update()

        for enemies in squadron:
            for enemy in enemies:
                enemy.update()

    # react to events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.stop()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

            # move player
            if event.key == pygame.K_LEFT:
                if not player.is_moving:
                    player.move_left()
                    player.move()
            if event.key == pygame.K_RIGHT:
                if not player.is_moving:
                    player.move_right()
                    player.move()

            # fire bullet
            if event.key == pygame.K_UP and len(bullets) < player.bullets:
                bullet = Bullet(player.x, player.y - player.r)
                bullets.append(bullet)

            # add new squad from the top
            if event.key == pygame.K_n:
                add_enemies()

    # boundaries
    if player.x < 0:
        player.stop()
        player.x = 0

    if player.x > game["width"]:
        player.stop()
        player.x = game["width"]

    # draw entities
    screen.fill(game["background"])

    # plyaer
    pygame.draw.circle(screen, player.color, [
                       player.x, player.y], player.r, player.w)

    # bullets
    for bullet in bullets:
        pygame.draw.circle(screen, bullet.color, [
                           bullet.x, bullet.y], bullet.r, bullet.w)
        if bullet.y <= 0:
            bullets.remove(bullet)
        # collision detection between the bullet and the squad
        # remove every enemy following the one being hit
        for enemies in squadron:
            for enemy in enemies:
                if bullet.x > enemy.x - enemy.r and bullet.x < enemy.x + enemy.r and bullet.y < enemy.y + enemy.r and bullet.y > enemy.y - enemy.r:
                    bullets.remove(bullet)
                    index = enemies.index(enemy)
                    for i in range(len(enemies) - index):
                        enemies.pop()
                if len(enemies) == 0:
                    squadron.remove(enemies)
                    add_enemies()
    # enemies
    for enemies in squadron:
        for enemy in enemies:
            if enemy.x < 0:
                enemy.x = 0
                enemy.bounce()
            if enemy.x > game["width"]:
                enemy.x = game["width"]
                enemy.bounce()

            # terminate the game when reaching the bottom
            if enemy.y > game["height"] - 20:
                running = False

            pygame.draw.circle(screen, enemy.color, [
                enemy.x, enemy.y], enemy.r, enemy.w)

    pygame.display.update()
