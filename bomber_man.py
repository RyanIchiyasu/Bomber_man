import pygame
from pygame.locals import *
import time
import sys
import random

class Player:
    def __init__(self):
        self.position_x = 0
        self.position_y = 0
        self.direction = 'down'
        self.strength = 1
    def Draw(self):
        if self.direction == 'down':
            screen.blit(player_down, (self.position_x, self.position_y))
        elif self.direction == 'up':
            screen.blit(player_up, (self.position_x, self.position_y))
        elif self.direction == 'left':
            screen.blit(player_left, (self.position_x, self.position_y))
        elif self.direction == 'right':
            screen.blit(player_right, (self.position_x, self.position_y))

class Bomb:
    def __init__(self, player_position_x, player_position_y, player_strength):
        self.position_x = player_position_x
        self.position_y = player_position_y
        self.time = 500
        self.strength = player_strength
    def Draw(self):
        if self.time % 50 >= 0 and self.time % 50 < 25:
            screen.blit(bomb_black, (self.position_x, self.position_y))
        else:
            screen.blit(bomb_red, (self.position_x, self.position_y))
    def TimeReduce(self):
        self.time = self.time - 1

class Flame:
    def __init__(self, bomb_position_x, bomb_position_y, bomb_strength):
        self.position_x = []
        self.position_y = []
        for i in range(5):
            self.position_x.append(bomb_position_x + 25 + random.randint(-100,100))
            self.position_y.append(bomb_position_y + 25 + random.randint(-100,100))
        self.time = 50
        self.strength = bomb_strength
    def Draw(self):
        for i in range(5):
            screen.blit(fire, (self.position_x[i], self.position_y[i]))
    def TimeReduce(self):
        self.time = self.time - 1

class Dragon:
    def __init__(self):
        self.position_x = 225
        self.position_y = 225
        self.direction = 'down'
        self.change_direction_timer = 50
    def Draw(self):
        if self.direction == 'down':
            screen.blit(dragon_down, (self.position_x, self.position_y))
        elif self.direction == 'up':
            screen.blit(dragon_up, (self.position_x, self.position_y))
        elif self.direction == 'left':
            screen.blit(dragon_left, (self.position_x, self.position_y))
        elif self.direction == 'right':
            screen.blit(dragon_right, (self.position_x, self.position_y))
    def ChangeDirection(self):
        self.change_direction_timer -= 1
        if self.change_direction_timer == 0:
            self.change_direction_timer = random.randint(100, 200)
            new_direction = random.randint(0, 3)
            if new_direction == 0:
                self.direction = 'up'
            elif new_direction == 1:
                self.direction = 'down'
            elif new_direction == 2:
                self.direction = 'left'
            elif new_direction == 3:
                self.direction = 'right'
    def Move(self):
        if self.direction == 'up':
            self.position_y -= 1
            if self.position_y < 0:
                self.position_y = 0
                self.ChangeDirection()
        elif self.direction == 'down':
            self.position_y += 1
            if self.position_y > 450:
                self.position_y = 450
                self.ChangeDirection()
        elif self.direction == 'left':
            self.position_x -= 1
            if self.position_x < 0:
                self.position_x = 0
                self.ChangeDirection()
        elif self.direction == 'right':
            self.position_x += 1
            if self.position_x > 450:
                self.position_x = 450
                self.ChangeDirection()

class barrel:
    def __init__(self):
        self.position_x = 0
        self.position_y = 0
        self.content = 'fire'
    def Draw(self):
        screen.blit(bomb_black, (self.position_x, self.position_y))

##########################################
#INITIALIZE
##########################################
pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Bomber Man')

wallpaper = pygame.image.load("wallpaper.jpg").convert_alpha()

player_down = pygame.image.load("player_down.png").convert_alpha()
player_up = pygame.image.load("player_up.png").convert_alpha()
player_right = pygame.image.load("player_right.png").convert_alpha()
player_left = pygame.image.load("player_left.png").convert_alpha()

bomb_black = pygame.image.load("bomb_black.png").convert_alpha()
bomb_red = pygame.image.load("bomb_red.png").convert_alpha()

dragon_up = pygame.image.load("dragon_up.png").convert_alpha()
dragon_down = pygame.image.load("dragon_down.png").convert_alpha()
dragon_left = pygame.image.load("dragon_left.png").convert_alpha()
dragon_right = pygame.image.load("dragon_right.png").convert_alpha()

stone = pygame.image.load("stone.png").convert_alpha()
barrel = pygame.image.load("barrel.png").convert_alpha()
fire = pygame.image.load("fire.png").convert_alpha()

player = Player()
dragon = Dragon()
all_bomb = []
all_flame = []

##########################################
#FUNCTION
##########################################
def KeyCheck():
    key = pygame.key.get_pressed()
    if key[K_LEFT]:
        player.position_x -= 1
        if player.position_x < 0:
            player.position_x = 0
        player.direction = 'left'
    elif key[K_RIGHT]:
        player.position_x += 1
        if player.position_x > 450:
            player.position_x = 450
        player.direction = 'right'
    elif key[K_DOWN]:
        player.position_y += 1
        if player.position_y > 450:
            player.position_y = 450
        player.direction = 'down'
    elif key[K_UP]:
        player.position_y -= 1
        if player.position_y < 0:
            player.position_y = 0
        player.direction = 'up'

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                new_bomb = Bomb(player.position_x, player.position_y, player.strength)
                all_bomb.append(new_bomb)

def BombDraw():
    for index, bomb in enumerate(all_bomb):
        bomb.TimeReduce()
        if bomb.time <= 0:
            del all_bomb[index]
            new_flame = Flame(bomb.position_x, bomb.position_y, bomb.strength)
            all_flame.append(new_flame)
        else:
            bomb.Draw()

def FlameDraw():
    for index, flame in enumerate(all_flame):
        flame.TimeReduce()
        if flame.time == 0:
            del all_flame[index]
        else:
            flame.Draw()

##########################################
#MAIN FUNCTION
##########################################
while True:
    KeyCheck()

    screen.blit(wallpaper,(0,0))
    BombDraw()
    FlameDraw()
    player.Draw()
    dragon.ChangeDirection()
    dragon.Move()
    dragon.Draw()
    pygame.display.update()

    time.sleep(0.005)
