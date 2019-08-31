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
        self.life = 5
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
        self.hit = 0
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
        self.attack_timer = random.randint(200, 400)
        self.life = 5
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
    def Attack(self):
        self.attack_timer -= 1
        if self.attack_timer == 0:
            self.attack_timer = random.randint(200, 400)
            return 1
        else:
            return 0

class Scorpion:
    def __init__(self, dragon_position_x, dragon_position_y, dragon_direction):
        if dragon_direction == 'up':
            self.position_x = dragon_position_x
            self.position_y = dragon_position_y - 50
            self.direction = 'up'
        elif dragon_direction == 'down':
            self.position_x = dragon_position_x
            self.position_y = dragon_position_y + 50
            self.direction = 'down'
        elif dragon_direction == 'left':
            self.position_x = dragon_position_x - 50
            self.position_y = dragon_position_y
            self.direction = 'left'
        elif dragon_direction == 'right':
            self.position_x = dragon_position_x + 50
            self.position_y = dragon_position_y
            self.direction = 'right'

        self.change_direction_timer = 10
        self.time = 1000
        self.life = 1
        self.speed = random.randint(1,2)

    def Draw(self):
        if self.direction == 'down':
            screen.blit(scorpion_down, (self.position_x, self.position_y))
        elif self.direction == 'up':
            screen.blit(scorpion_up, (self.position_x, self.position_y))
        elif self.direction == 'left':
            screen.blit(scorpion_left, (self.position_x, self.position_y))
        elif self.direction == 'right':
            screen.blit(scorpion_right, (self.position_x, self.position_y))

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
            self.position_y -= self.speed
            if self.position_y < 0:
                self.position_y = 0
                self.ChangeDirection()
        elif self.direction == 'down':
            self.position_y += self.speed
            if self.position_y > 450:
                self.position_y = 450
                self.ChangeDirection()
        elif self.direction == 'left':
            self.position_x -= self.speed
            if self.position_x < 0:
                self.position_x = 0
                self.ChangeDirection()
        elif self.direction == 'right':
            self.position_x += self.speed
            if self.position_x > 450:
                self.position_x = 450
                self.ChangeDirection()

    def TimeReduce(self):
        self.time = self.time - 1

class Text:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.time = 100
    def Draw(self):
        screen.blit(killed_text, (self.position_x, self.position_y))
    def TimeReduce(self):
        self.time -= 1

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

scorpion_up = pygame.image.load("scorpion_up.png").convert_alpha()
scorpion_down = pygame.image.load("scorpion_down.png").convert_alpha()
scorpion_left = pygame.image.load("scorpion_left.png").convert_alpha()
scorpion_right = pygame.image.load("scorpion_right.png").convert_alpha()

stone = pygame.image.load("stone.png").convert_alpha()
barrel = pygame.image.load("barrel.png").convert_alpha()
fire = pygame.image.load("fire.png").convert_alpha()

font = pygame.font.Font(None, 35)
killed_text = font.render("killed", True,(128, 0, 128))

player = Player()
dragon = Dragon()
all_bomb = []
all_flame = []
all_scorpion = []
all_text = []
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

def ScorpionDraw():
    for index, scorpion in enumerate(all_scorpion):
        scorpion.TimeReduce()
        if scorpion.time == 0:
            del all_scorpion[index]
        else:
            scorpion.ChangeDirection()
            scorpion.Move()
            scorpion.Draw()

def TextDraw():
    for index, text in enumerate(all_text):
        text.TimeReduce()
        if text.time == 0:
            del all_text[index]
        else:
            text.Draw()

def HitCheck():
    for flame in all_flame:
        for i in range(5):
            if (abs(flame.position_x[i] - dragon.position_x) < 50) and (abs(flame.position_y[i] - dragon.position_y) < 50) and (flame.hit == 0):
                print('Hit Boss')
                dragon.life -= 1
                flame.hit = 1
                print('dragon life = ' + str(dragon.life))
        for i in range(5):
            for index, scorpion in enumerate(all_scorpion):
                if (abs(flame.position_x[i] - scorpion.position_x) < 50) and (abs(flame.position_y[i] - scorpion.position_y) < 50):
                    print('Hit Scorpion')
                    scorpion.life -= 1
                    new_text = Text(scorpion.position_x, scorpion.position_y)
                    all_text.append(new_text)
                    print('scorpion life = ' + str(scorpion.life))
                    if scorpion.life == 0:
                        del all_scorpion[index]

def DragonAttack():
    attack = dragon.Attack()
    if attack == 1:
        new_scorpion = Scorpion(dragon.position_x, dragon.position_y, dragon.direction)
        all_scorpion.append(new_scorpion)

##########################################
#MAIN FUNCTION
##########################################
while True:
    KeyCheck()

    screen.blit(wallpaper,(0,0))
    BombDraw()
    FlameDraw()
    TextDraw()
    player.Draw()
    DragonAttack()
    ScorpionDraw()
    HitCheck()
    dragon.ChangeDirection()
    dragon.Move()
    dragon.Draw()
    pygame.display.update()

    time.sleep(0.005)
