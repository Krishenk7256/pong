from pygame import *
from random import randint
from time import time as timer
speed_x = 3
speed_y = 3
game = True
finish = False
background = (255, 255, 255)
class gameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(gameSprite):
    def updatel(self):
        
        keysl = key.get_pressed()
        if keysl[K_DOWN] and self.rect.y != 0:
            self.rect.y -= self.speed
        if keysl[K_UP] and self.rect.y != 350:
            self.rect.y += self.speed
    def updater(self):
        keysr = key.get_pressed()
        if keysr[K_w] and self.rect.y != 0:
            self.rect.y -= self.speed
        if keysr[K_s] and self.rect.y != 350:
            self.rect.y += self.speed
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render("Первый проеграл ахахах.", True, (0, 0, 0))
lose2 = font1.render("Второе проеграл хахахах.", True, (0, 0, 0))
window = display.set_mode((700, 500))
window.fill(background)
ball = gameSprite('ball.png', 350, 250, 40, 40, 5)
player1 = Player('stolb.png', 20, 200, 10, 150, 5)
player2 = Player('stolb.png', 680, 200, 10, 150, 5)
clock = time.Clock()

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:
        window.fill(background)
        player1.updatel()
        player1.reset()
        player2.updater()
        player2.reset()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > 500-40 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        if ball.rect.x > 700:
            finish = True
            window.blit(lose2, (200, 200))


    clock.tick(30)
    display.update()