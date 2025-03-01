import pygame
import random
SCREEN_WIDTH,SCREEN_HEIGHT=500,600
MOVEMENT_SPEED= 7
FONT_SIZE= 72
pygame.init()
background_image = pygame.transform.scale("C:\Users\user\python programms\hand-drawn-video-game-background_23-2150307800.avif")
(SCREEN_WIDTH,SCREEN_HEIGHT)
font=pygame.font.SysFont('Tiles new roman'FONT_SIZE)
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super() .__init__()
        self.image =pygame.Surface[width,height]
        self.image.fill(pygame.color('dodgerblue'))
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect = self.image.get_rect()
    def move(self,x_change,y_change):
        self.rect.x = max(
            min(self.rect.x+ x_change,SCREEN_WIDTH-self.rect.width), 0)
        self.rect.y = max(
            min(self.rect.y+ y_change,SCREEN_WIDTH-self.rect.width), 0)
screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
pygame.display.set_caption("Sprite collision")
all_sprites = pygame.sprite.group()
sprite1=Sprite(pygame.color('black'),20,30)
sprite1.rect.x,sprite1.rect.y=random.randint(
    0,SCREEN_WIDTH-sprite1.rect.width), random.randint(
        0,SCREEN_HEIGHT - sprite1.rect.height)
all_sprites.add(sprite1)
sprite2=Sprite(pygame.color('black'),20,30)
sprite2.rect.x,sprite1.rect.y=random.randint(
    0,SCREEN_WIDTH-sprite1.rect.width), random.randint(
        0,SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite2)
running, won=True or False
clock = pygame.time.clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN
        and event.key == pygame.K_x):
            runninr = False
            if not won:
                keys = pygame 

    

        
        
