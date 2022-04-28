import pygame
pygame.font.init()
pygame.mixer.init()

# parameters
size = width, height = (900, 500)
screen = pygame.display.set_mode(size)
spaceship_size = spaceship_w, spaceship_h = (55, 40)
border = pygame.Rect(width//2 - 5, 0, 10, height)
pygame.display.set_caption("Boris' Space Fight")  # window caption
fps = 60  # refresh rate
jump = 5  # moving distance
bullet_limit = 3
bullet_speed = 7  # shooting speed (faster than the ship)
space_bg = pygame.transform.scale(pygame.image.load(  # importing a pic as BG
    'space_fight_game_project\Assets\space.png'), (width, height))

# special fonts
endgame_font = pygame.font.SysFont('comicsans', 100)
health_font = pygame.font.SysFont('comicsans', 40)

# sound effects
hit_sound = pygame.mixer.Sound(
    'space_fight_game_project\Assets\Gun+Silencer.mp3')
shooting_sound = pygame.mixer.Sound(
    'space_fight_game_project\Assets\Grenade+1.mp3')


# hit event creation
yellow_hit = pygame.USEREVENT + 1
red_hit = pygame.USEREVENT + 2

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red_c = (255, 0, 0)
yellow_c = (255, 255, 0)

# spaceships
spaceship_yellow_img = pygame.image.load(
    'space_fight_game_project\Assets\spaceship_yellow.png')
spaceship_yellow = pygame.transform.rotate(pygame.transform.scale(
    spaceship_yellow_img, spaceship_size), 270)  # rotating to the left & scaling the image
spaceship_red_img = pygame.image.load(
    'space_fight_game_project\Assets\spaceship_red.png')
spaceship_red = pygame.transform.rotate(pygame.transform.scale(
    spaceship_red_img, spaceship_size), 90)  # rotating to the right & scaling the image


def red_move(keys_pressed, red):
    if keys_pressed[pygame.K_a] and red.x - jump + spaceship_w/4 > 0:  # red left till left limit
        red.x -= jump
    # red right till border
    if keys_pressed[pygame.K_d] and red.x + jump + spaceship_w/2 < border.x - 5:
        red.x += jump
    if keys_pressed[pygame.K_w] and red.y - jump > 0:  # red up till upper limit
        red.y -= jump
    # red down til lower limit
    if keys_pressed[pygame.K_s] and red.y + jump + spaceship_w/2 < height - 19:
        red.y += jump


def yellow_move(keys_pressed, yellow):
    if keys_pressed[pygame.K_LEFT] and yellow.x - jump > border.x:
        yellow.x -= jump
    if keys_pressed[pygame.K_RIGHT] and yellow.x + jump + spaceship_w/2 < width:
        yellow.x += jump
    if keys_pressed[pygame.K_UP] and yellow.y - jump > 0:
        yellow.y -= jump
    if keys_pressed[pygame.K_DOWN] and yellow.y + jump + spaceship_w/2 < height - 19:
        yellow.y += jump


def bullets_handle(yellow_bullets, red_bullets, yellow, red):
    for bullet in red_bullets:
        bullet.x += bullet_speed
        if yellow.colliderect(bullet):  # if bullet hit the yellow ship
            pygame.event.post(pygame.event.Event(
                yellow_hit))  # calling special event
            red_bullets.remove(bullet)
        elif bullet.x > width:
            red_bullets.remove(bullet)

    for bullet in yellow_bullets:
        bullet.x -= bullet_speed
        if red.colliderect(bullet):  # if bullet hit the red ship
            pygame.event.post(pygame.event.Event(
                red_hit))  # calling special event
            yellow_bullets.remove(bullet)
        elif bullet.x < 0:
            yellow_bullets.remove(bullet)


def winner(text):
    text_declare = endgame_font.render(text, 1, white)
    screen.blit(text_declare, (width//2 - text_declare.get_width() //
                2, height//2 - text_declare.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)


def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    screen.blit(space_bg, (0, 0))  # background - pic loaded
    pygame.draw.rect(screen, black, border)  # border manifestation
    red_health_txt = health_font.render(f'HP: {red_health}', 1, white)
    yellow_health_txt = health_font.render(f'HP: {yellow_health}', 1, white)
    screen.blit(yellow_health_txt,
                (width - yellow_health_txt.get_width() - 10, 10))
    screen.blit(red_health_txt, (10, 10))
    screen.blit(spaceship_red, (red.x, red.y))  # red spaceship manifestation
    # yellow spaceship manifestation
    screen.blit(spaceship_yellow, (yellow.x, yellow.y))
    for bullet in red_bullets:
        pygame.draw.rect(screen, red_c, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(screen, yellow_c, bullet)
    pygame.display.update()


def main():
    # spaceships health
    red_health = 10
    yellow_health = 10
    # bullets lists
    yellow_bullets = []
    red_bullets = []
    # red ship parameters
    red = pygame.Rect(300, 100, spaceship_w, spaceship_h)
    # yellow ship parameters
    yellow = pygame.Rect(600, 100, spaceship_w, spaceship_h)
    clock = pygame.time.Clock()
    # main game loop
    run = True
    while run:
        # loop speed control
        clock.tick(fps)
        # event watcher
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                # shooting red bullets
                if event.key == pygame.K_LCTRL and len(red_bullets) < bullet_limit:
                    shooting_sound.play()
                    bullet = pygame.Rect(
                        red.x + red.width, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                # shooting yellow bullets
                if event.key == pygame.K_RCTRL and len(yellow_bullets) < bullet_limit:
                    shooting_sound.play()
                    bullet = pygame.Rect(
                        yellow.x, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
            if event.type == red_hit:
                hit_sound.play()
                red_health -= 1
                if red_health <= 0:
                    winner('YELLOW WINS!')
                    run = False
            if event.type == yellow_hit:
                hit_sound.play()
                yellow_health -= 1
                if yellow_health <= 0:
                    winner('RED WINS!')
                    run = False
        keys_pressed = pygame.key.get_pressed()  # key pressing event
        red_move(keys_pressed, red)
        yellow_move(keys_pressed, yellow)
        bullets_handle(yellow_bullets, red_bullets, yellow, red)
        draw_window(red, yellow, red_bullets, yellow_bullets,
                    red_health, yellow_health)

    main()


if __name__ == "__main__":
    main()
