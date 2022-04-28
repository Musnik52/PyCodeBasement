import pygame
from pygame.locals import *
import random

# parameters
size = width, height = (600, 630)
road_w = int(width/1.6)
roadmarks_w = int(width/80)
r_lane = width/2 + road_w/4
l_lane = width/2 - road_w/4
speed = 1

# initializing game
pygame.init()
running = True
# window size:
screen = pygame.display.set_mode(size)
# game caption - name
pygame.display.set_caption("Boris' Death Race Rally")

# load player car
car = pygame.image.load("car_game_project\car.png")
#car = pygame.transform.scale(car, (250, 250))
# initial location of car - bottom right
car_loc = car.get_rect()
car_loc.center = r_lane, height*0.8

# load enemy car
car2 = pygame.image.load("car_game_project\otherCar.png")
# initial location of car - upper left
car2_loc = car2.get_rect()
car2_loc.center = l_lane, height*0.2

speed_counter = 0
# the game loop
while running:
    # speed difficulty increase
    speed_counter += 1
    # increase after a few itterations
    if speed_counter == 1024:
        speed += 0.15
        speed_counter = 0
        print(f' LEVEL UP! Speed: {speed}')
    # animating enemy car
    car2_loc[1] += speed  # moving forward
    if car2_loc[1] > height:  # when reaching the bottom
        if random.randint(0, 1) == 0:
            # random appearance - top right
            car2_loc.center = r_lane, -600
        else:
            # random appearance - top left
            car2_loc.center = l_lane, -600
    # endgame - crashing cars
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 250:
        print("BOOM! CRASH!! GAME OVER!!!")
        running = False
    for event in pygame.event.get():
        # pressing the X buttom to quit
        if event.type == QUIT:
            print("GAME EXIT")
            running = False
        # pressing keys
        if event.type == KEYDOWN:
            # pressing left or "a" - move to the left
            if event.key in [K_a, K_LEFT]:
                if car_loc.x - int(road_w/2) < 20:  # left road limit
                    pass
                else:
                    car_loc = car_loc.move([-int(road_w/2), 0])
            # pressing right or "d" - move to the right
            if event.key in [K_d, K_RIGHT]:
                if car_loc.x + int(road_w/2) > int(road_w):  # right road limit
                    pass
                else:
                    car_loc = car_loc.move([int(road_w/2), 0])
    # screen color - background
    screen.fill((60, 220, 0))
    # drawing the road
    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (width/2 - road_w/2, 0, road_w, height))
    # draw roadmarks
    pygame.draw.rect(  # center
        screen,
        (255, 255, 255),
        (width/2 - roadmarks_w/2, 0, roadmarks_w, height))
    pygame.draw.rect(  # left side
        screen,
        (255, 240, 60),
        (width/2 - road_w/2 + roadmarks_w*2, 0, roadmarks_w, height))
    pygame.draw.rect(  # right side
        screen,
        (255, 240, 60),
        (width/2 + road_w/2 - roadmarks_w*3, 0, roadmarks_w, height))

    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    # apply changes
    pygame.display.update()

# collapsing the game-app
pygame.quit()
