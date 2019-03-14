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

        self.dy = 0  # 물체가 이동하는 것을 가속 (y축 이동을 조절하는 변수)

    def move(self) :
        self.dy += 1  # 물체 가속
        self.y += self.dy

    def draw(self) :
        screen.blit(badbird_img, (self.x, self.y))


badbird = Badbird()

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT :
            sys.exit()

    screen.fill((255,255,255))

    badbird.move()
    badbird.draw()
    
    pygame.display.update()