import pygame, sys
from pygame.locals import *
pygame.init()

# 화면 크기 설정
screen = pygame.display.set_mode((700, 580))

# 변수 설정
xpos = 50

while 1 :
    # 이벤트가 발생하면(pygame.event.get()) 버튼을 눌렀는지(QUIT)
    # 해당 루프안에 이벤트들이 다 종료되면 종료?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 종료한다
            sys.exit()

    # 좌표 이동
    xpos += 1

    # 화면 색깔
    # 빨강,초록,파랑
    screen.fill((255,255,255))

    # 마지막에 그릴 수록 맨 앞에 그려짐
    
    # screen에, 초록색으로(0,255,0), 해당 위치에(100,200), 크기(_원의 반지름 20)로 [두께를 추가할 수 있음] 원을 그려라
    pygame.draw.circle(screen, (0,255,0), (100, 200), 20, 4)

    # screen에, 빨간색으로, 위치, 가로길이, 세로길이(100,100,40,30)
    # 이떄 위치는 중심점이 아닌 왼쪽 맨 위 꼭지점의 위치
    pygame.draw.rect(screen,(255,0,0), (xpos,200,40,30))

    # 화면에 변화들을 출력
    # while 루프 실행되는 중에 생기는 변화들을 업데이트해서 화면에 표시해줌
    pygame.display.update()