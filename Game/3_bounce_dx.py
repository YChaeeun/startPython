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
        self.dx = 3  # x축 이동을 조절하는 변수

    def move(self) :
        self.dx += self.dx

        self.dy += 0.1  # 물체 가속
        self.y += self.dy

        if 100 < self.y < 150  :
            self.x += 15
        if self.y > 200:
            self.x -= 15

    def draw(self) :
        screen.blit(badbird_img, (self.x, self.y))

    
    def bounce(self) :
        if 0 < self.x  or self.x > 850 :  # 벽에 부딪히면, 방향을 바꿈
            self.dx *= -1


badbird = Badbird()

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT :
            sys.exit()

    screen.fill((255,255,255))

    badbird.move()
    badbird.draw()
    badbird.bounce()
    
    pygame.display.update()