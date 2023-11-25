from pygame import *
from random import randint
mixer.init()
font.init()
window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('background.jpg'),(700, 500))

clock = time.Clock()
FPS = 60
#mixer.music.load('space.ogg')
#mixer.music.play()
#fire_sound = mixer.Sound('fire.ogg')
font = font.SysFont('Arial',50)
lose1 = font.render('Ракетка 1 проиграла!', True,(220, 20, 60))
lose2 = font.render('Ракетка 2 проиграла!', True,(220, 20, 60))
game = True
finish = False
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, x_size, y_size):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (x_size, y_size))        
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.x_size = x_size
        self.y_size = y_size
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 395:
            self.rect.y += self.speed   
ball = GameSprite('ball.png',300, 180, 13,60, 60)
player1 = Player('racetka.png', 10, 20, 6, 40, 140)
player2 = Player('racetka.png', 650, 20, 6, 40, 140)
speed_x = 3
speed_y = 3
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if finish != True:
        window.blit(background,(0, 0))
        
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        player1.update_l()
        player1.reset()
        ball.reset()
        player2.update_r()
        player2.reset()
    if ball.rect.y > 430 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1 
    if ball.rect.x < -40 :
        finish = True
        window.blit(lose1, (152, 215))
    if ball.rect.x > 680:
        window.blit(lose2, (152, 215))
        finish = True
    display. update()
    clock.tick(FPS)
