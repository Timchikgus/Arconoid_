from pygame import *
from random import randint
from time import sleep
class Game_Sprite(sprite.Sprite):
    def __init__(self,picture, w, h, coord_x, coord_y):
        super().__init__()
        self.image = transform.scale(image.load(picture),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = coord_x
        self.rect.y = coord_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
win_height = 500
win_width = 700
miteors = sprite.Group()
bullets = sprite.Group()
class Player(Game_Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
        Game_Sprite.__init__(self, player_image,player_x, player_y, size_x, size_y)
        self.y_speed = player_y_speed
        self.x_speed = player_x_speed
    def update(self):
        if self.rect.x >= 413:
            self.rect.x = 413
        if self.rect.x <= -10:
            self.rect.x = -10
        if self.rect.y >= 630:
            self.rect.y = 630
        if self.rect.y <= 0:
            self.rect.y = 0
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
    def fire(self):
        bullet = Bullet('Пуля.png',20 , 30,self.rect.centerx,  self.rect.top,  -10)
        bullets.add(bullet)
class Bullet(Game_Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        Game_Sprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
        
    def update(self):
        self.rect.y += self.speed
        if self.rect.x >= 800:
            self.kill()
        if self.rect.x <= -100:
            self.kill()
        if self.rect.y >= 700:
            self.kill()
        if self.rect.y <= 0:
            self.kill()
class Miteors(Game_Sprite):
    def __init__(self,picture, w, h, coord_x, coord_y, spin, speed_metior_x, speed_metior_y):
        Game_Sprite.__init__(self,picture, w, h, coord_x, coord_y)
        self.speed_y = speed_metior_y
        self.spin = spin
        self.speed_x = speed_metior_x
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        window.fill((10,10,10))
        if self.rect.y >=800:
            self.kill()
font.init()
window = display.set_mode((500, 750))
window.fill((10,10,10))
Hiro = Player('Корабль.png', 100, 100, 160, 600, 0, 0)
image.load("Космос_.png")
timer = 10
End = False
m = 20
n = 0
fon = font.SysFont(None, 40)
def create_miteor():
    s_x = randint(2, 20)
    s_y= randint(-5, 5)
    x_spavn = randint(0, 500)
    h_w = randint(50,200)
    miteor = Miteors('Метиор.png',h_w,h_w , x_spavn,-30,0,s_y,s_x)
    miteors.add(miteor)
while End != True:
    time.delay(45)
    window.fill((10,10,10))
    for e in event.get():
        if e.type == QUIT:
            End = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                Hiro.fire()
            if e.key == K_LEFT:
                Hiro.x_speed = -5
            if e.key == K_RIGHT:
                
                Hiro.x_speed = 5
            if e.key == K_UP:
                
                Hiro.y_speed = -5
            if e.key == K_DOWN:
                
                Hiro.y_speed = 5
        elif e.type == KEYUP:
            if e.key == K_LEFT:
                
                Hiro.x_speed = 0
            if e.key == K_RIGHT:
                
                Hiro.x_speed = 0
            if e.key == K_UP:
                
                Hiro.y_speed = 0
            if e.key == K_DOWN:
                
                Hiro.y_speed = 0
            if e.key == QUIT:
                exit()
            if e.key == K_ESCAPE:
                exit()
            # elif e.key == K_m:
                # create_miteor()
    if timer >= 10:
        Hiro.fire()
        timer = 0
    else:
        timer += 1.5
    
    if m >= 10:
        create_miteor()
        m = 0
    else:
        m += 1
    
    miteors.update()
    miteors.draw(window)
    bullets.update()
    bullets.draw(window)
    Hiro.reset()
    Hiro.update()
    if sprite.groupcollide(miteors, bullets, True, True):
        n += 1
        schot = fon.render('Счёт:' + str(n), True,(255, 255, 255))
        window.blit(schot,  (100,100))
        # print(n)
    schot = fon.render('Счёт:' + str(n), True,(255, 255, 255))
    window.blit(schot,  (100,100))
    if sprite.spritecollide(Hiro, miteors, False):
        img = image.load('Over.png')
        window.fill((0,0,0)) 
        window.blit(transform.scale(img, (200,200)), (150, 275))
        End = True
    display.update()

sleep(3)
