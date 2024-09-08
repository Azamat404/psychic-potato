import pygame
pygame.init()
#pygame.transform.rotozoom(img,degree,scale)
window=(900,700)
screen=pygame.display.set_mode((window[0],window[1]))
backgraund=pygame.image.load("bg.png").convert()
earth=window[1]-55
FPS=60
font=pygame.font.SysFont("Arial", 40)
clock=pygame.time.Clock()
gameover=False
running=True
counter=0
class Character:
    def __init__(self,img,scale,lef,bot,x,y):
        self.sprite=pygame.transform.rotozoom(pygame.image.load(img),0,scale)
        self.rect=self.sprite.get_rect()
        self.rect.left=lef
        self.rect.bottom=bot
        self.speed=[x,y]
        self.jump_is=True
        self.jump_speed=20
        self.jump_counter=0
    def move(self):
        global FPS , counter

        self.rect=self.rect.move(self.speed)
        if self.rect.left<0:
            self.rect.right=window[0]
            FPS+=2
            counter+=1
    def gravity(self):
        if self.rect.bottom>earth:
            self.rect.bottom=earth

player=Character("fox.png", 0.2,50,earth,0,9)
ms=Character("ms.png",0.7, window[0],earth,-10 ,0)


while running:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                running=False
            if event.key == pygame.K_SPACE and player.rect.bottom==earth and not(player.jump_is):
                player.jump_is=True 
                player.jump_counter= player.jump_speed  
        if player.jump_is and player.jump_counter>0:
            player.rect.y -= player.jump_speed
            player.jump_counter -=1
        else: player.jump_is=False
        if player.rect.colliderect(ms.rect):
            gameover=True
        
        if not(gameover):
            player.move() 
            player.gravity()
            ms.move()
        else: 
            key=pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                counter=0
                FPS=60
                ms.rect.left=window[0]
                gameover=False

    screen.blit(backgraund,(0,0))
    screen.blit(player.sprite,player.rect) 
    screen.blit(ms.sprite,ms.rect) 
    text=font.render(F"СЧЕТ:{counter}",1,pygame.Color("black"))
    screen.blit(text,(10,10))
    if gameover:
        game_over_text=font.render("Конец игры", True, (180,0,0))
        screen.blit(game_over_text,(400,300))
    pygame.display.update()
    clock.tick(FPS)
    



























pygame.quit()
