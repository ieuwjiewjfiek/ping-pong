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
#font = font.SysFont('Arial',50)
#win = font.render('YOU WIN!', True,(255, 0, 0))
#lose = font.render('YOU LOSE!', True,(255, 0, 0))

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
#    def fire(self):
#        bullet = Bullet('bullet.png',self.rect.centerx, self.rect.top, 8, 30, 30)
#        bullets.add(bullet)
#class Enemy(GameSprite):
#    def update(self):
#        self.rect.y += self.speed 
#        global lost
#        if self.rect.y >= 500:
#            self.rect.y = 0
#            self.rect.x = randint(20,600)
#            lost += 1
#class Bullet(GameSprite):
#    def update(self):
#        self.rect.y -= self.speed 
#        if self.rect.y <= 0:
#            self.kill()
#bullets = sprite.Group()
#monsters = sprite.Group()
#asteroids = sprite.Group()
#for i in range(5):
#    monster = Enemy('enemy.png', randint(20,600), 0, randint(1,2), 60, 60)               
#    monsters.add(monster)
#for c in range(2):
#    asteroid = Enemy('asteroid.png', randint(20,600), 0, randint(1,2), 50, 50)
#    asteroids.add(asteroid)
#
player1 = Player('racetka.png', 10, 20, 6, 40, 140)
player2 = Player('racetka.png', 650, 20, 6, 40, 140)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
#        elif e.type == KEYDOWN:
#            if e.key == K_SPACE:
#                fire_sound.play()
#                player.fire()
#            if e.key == K_v and finish == True:
#                for m in monsters:
#                    m.kill()
#                for b in bullets:
#                    b.kill()
#                for a in asteroids:
#                    a.kill()
#                lost = 0
#                kill = 0
#                for i in range(5):
#                    monster = Enemy('enemy.png', randint(20,600), 0, randint(1,2), 60, 60)               
#                    monsters.add(monster)
#                finish = False
#                for c in range(2):
#                    asteroid = Enemy('asteroid.png', randint(20,600), 0, randint(1,2), 50, 50)
#                    asteroids.add(asteroid)
                
                


    if finish != True:

        
        
        window.blit(background,(0, 0))

        player1.update_l()
        player1.reset()
        player2.update_r()
        player2.reset()
#        monsters.update()
#        monsters.draw(window)
#
#        bullets.update()
#        bullets.draw(window)

#        sprites_list1 = sprite.spritecollide(player, monsters, False)
#        for pl in sprites_list1:
#            finish = True
#            window.blit(lose, (245, 240))
#        sprites_list2 = sprite.groupcollide(monsters, bullets, True, True)
#        for mn in sprites_list2:
#            kill += 1
#            monster = Enemy('enemy.png', randint(20,600), 0, randint(1,2), 60, 60)               
#            monsters.add(monster)
#        text_win = font.render('Убито:' + str(kill), True,(255, 255, 224))
#        window.blit(text_win, (0, 40))

#        sprites_list3 = sprite.spritecollide(player, asteroids, False)
#        for pla in sprites_list3:
#            finish = True
#            window.blit(lose, (245, 240))
#        sprites_list4 = sprite.groupcollide(asteroids, bullets, True, True)
#        for mn in sprites_list4:
#            kill += 1
#            asteroid = Enemy('asteroid.png', randint(20,600), 0, randint(1,2), 60, 60)               
#            asteroids.add(asteroid)
#        text_win = font.render('Убито:' + str(kill), True,(255, 255, 224))
#        window.blit(text_win, (0, 40))
#
#        if lost == 30:  
#            window.blit(lose, (245, 240))
#            finish = True
#        if kill == 30:
#            window.blit(win, (245, 240))
#            finish = True


    display. update()
    clock.tick(FPS)