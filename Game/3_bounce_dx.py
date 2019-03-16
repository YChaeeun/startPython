import pygame, sys, random, os
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()


pygame.display.set_caption("참새 대잔치")
screen = pygame.display.set_mode((1000,680))


current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'images')
badbird_img  = pygame.image.load(os.path.join(image_path, 'bird.png'))

class Badbird :
    def __init__(self) :
        self.x = random.randint(0,850) # 이미지의 가로 길이를 고려
        self.y = -100

        self.dy = random.randint(2,6)
        self.dx = random.choice((-1, 1))*self.dy

    def move(self) :
        self.x += self.dx
        self.dy += 0.1  # 물체 가속
        self.y += self.dy

    def draw(self) :
        screen.blit(badbird_img, (self.x, self.y))
    
    def bounce(self) :
        if 0 < self.x  or self.x > 850 :  # 벽에 부딪히면, 방향을 바꿈
            self.dx *= -1

    def off_screen(self) :
        return self.y > 680



badbird = Badbird()

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT :
            sys.exit()

    screen.fill((255,255,255))

    badbird.move()
    badbird.bounce()
    badbird.draw()

    if badbird.off_screen() :
        badbird = Badbird()

    
    pygame.display.update()