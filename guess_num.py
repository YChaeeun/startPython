
import random
import time

# https://github.com/YChaeeun/startPython

# YChaeeun
# se_same5315@naver.com

def main():
    print()
    game_title = set_TITLE(30)
    

    gamer_name = set_GAMER_name( game_title )

    MAIN_GAME = True
    while MAIN_GAME:
        ai_num    = None
        try_count = 0

        result = False
        while not result :
            try_count, gamer_num = set_Gamer_NUM( try_count )
            ai_num = set_ai_num(ai_num)
            result = game_play(gamer_num, ai_num)

        game_result(gamer_name, try_count)
        MAIN_GAME = try_AGAIN(MAIN_GAME)
    print('Bye bye 다음에 다시 만나요!\n')
    time.sleep(2)

def isEngOrKo(input_string) :
    k_cnt = 0
    e_cnt = 0

    # ord(c) : c의 아스키 코드값을 반환하는 함수
    for n in input_string :
        if (ord('가') <= ord(n) <= ord('힣')) or (ord('ㄱ') <= ord(n) <= ord('ㅎ')) :
            k_cnt += 1
        elif ord('a') <= ord(n.lower()) <= ord('z') :
            e_cnt += 1

    if k_cnt > 1 :
        return 'k'
    else :
        return 'e'


def set_TITLE( title_num ) :
    GAME_TITLE_LEN = title_num
    print('숫자를 맞춰라!\n')
    print('제작 : YChaeeun')

    prompt = '게임 제목을 입력하세요(최대 %s자) : ' % GAME_TITLE_LEN
    msg_1  = '게임 제목은 최대 %s자 입니다.\n' % GAME_TITLE_LEN

    while True :
        game_title = input(prompt).strip()
        print()
        if not game_title :
            print('제목을 입력하세요\n')
        elif len(game_title) > GAME_TITLE_LEN :
            print(msg_1)
        else :
            #print(game_title)
            break

    if isEngOrKo(game_title) == 'k' :
        num = 4
    else :
        num = 2

    msg_2   = ' {0:^%s} ' % GAME_TITLE_LEN
    
    print( '='*(GAME_TITLE_LEN+num) )
    print( msg_2.format( game_title ) )

    if isEngOrKo(game_title) == 'k' :
        msg_2   = ' {0:^%s} ' % (GAME_TITLE_LEN+2)

    print( msg_2.format( 'v1.0.0' ) )
    print( '='*(GAME_TITLE_LEN+num) )

    return game_title

def set_GAMER_name(game_title) :
    nameCheck = False
    while not nameCheck :
        gamer_name = input('\n플레이어의 이름을 입력해주세요 : ').strip()
        if not gamer_name :
            print('이름을 입력하세요')
            continue
        nameCheck = True

    msg_3 = '\n안녕하세요 %s님, 게임 "%s"에 오신걸 환영합니다!' % (gamer_name, game_title)
    print(msg_3)
    print()
    game_comments = '''
    숫자를 맞춰라!

    제가 생각한 숫자를 맞춰보세요 (0~99 사이)
    시도한 횟수가 적을 수록 높은 점수를 얻을 수 있습니다!
    그럼 시작해 볼까요 :D   '''
    
    import sys
    for n in range(len(game_comments)) :
        time.sleep(0.1)
        sys.stdout.write(game_comments[n])
        sys.stdout.flush()

    print()
    print()
    return gamer_name

def set_Gamer_NUM( try_count) :

    while True:
        gamer_num = input('예상한 숫자를 입력해주세요(0~99) : ').strip()
        try_count += 1

        if not gamer_num :
            print('숫자를 입력하세요\n')
        elif not gamer_num.isnumeric():
            print('0~99의 정수값을 입력해주세요\n')
        else :
            gamer_num = int(gamer_num)
            if gamer_num > 99 or gamer_num < 0 :
                print('0~99의 정수값을 입력해주세요\n')
                continue
            break
    return try_count, gamer_num

def set_ai_num(ai_num) :
    if not ai_num :
        ai_num = random.randint(0,99)
    return ai_num

def game_play(gamer_num, ai_num) :
    result = False
    if gamer_num > ai_num :
        print(f'AI의 숫자는 {gamer_num} 보다 작습니다.\n')
    elif gamer_num < ai_num :
        print(f'AI의 숫자는 {gamer_num} 보다 큽니다.\n')
    else :
        print('정답입니다!\n')
        result = True
    return result

def game_result(gamer_name, try_count) :
    score = (20-try_count)*5
    print('%s님의 총 시도 횟수는 %s회 입니다.' %(gamer_name, try_count))
    print('%s님의 점수는 %s입니다.\n' %(gamer_name, score) )
    if score > 80 :
        print('잘하셨어요!')
    elif score > 50 :
        print('괜찮아요!')
    elif score > 30 :
        print('좀 더 노력하세요')
    else :
        print('아.. 아쉬워요 다시 한 번?')
    print()
def try_AGAIN(MAIN_GAME) :
    while True :
        ment = '게임을 다시 진행하시겠습니까?(Y/N) '
        replay = input(ment).strip().upper()
        print()
        if  replay == 'Y' :
            break
        elif replay == 'N' :
            MAIN_GAME = False
            break
        else :
            print('정확하게 입력해주세요\n')
    return MAIN_GAME
        

if __name__ == '__main__' :
    #print('->', __name__)
    main()