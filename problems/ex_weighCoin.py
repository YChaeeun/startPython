
import random

numofCoins = random.randint(50,200)
FAKE = random.randint(1,numofCoins)

def weighCoin(a,b,c,d): 
    # 저울 역할을 하는 함수 b-a == d-c
    # a~b 그룹과 c~d 그룹의 동전 개수는 같음

    if a <= FAKE <= b :  # 가짜동전이 a ~ b 사이에 있는 경우 (a~b 그룹의 무게가 더 가벼운 경우)
        return -1
    elif c <= FAKE <= d : # 가짜동전이 c~d 사이에 있는 경우 (c~d 그룹의 무게가 더 가벼운 경우)
        return 1
    else :
        return 0          # a~b 그룹과 c~d 그룹의 무게가 같은 경우 (가짜동전이 사이에 없음)
    

def find_fakeCoin(left, right):  # 가짜 코인을 찾는 함수
    
    if left == right :
        return left

    half = (right - left +1) // 2
    left_1 = left
    left_2 = left+half-1
    right_1 = left+half
    right_2 = right_1+half -1

    result = weighCoin(left_1, left_2, right_1, right_2)
    if result == -1 :
        return find_fakeCoin(left_1,left_2)
    elif result == 1 :
        return find_fakeCoin(right_1, right_2)
    else :
        return right



print('FAKE coin : ', FAKE, numofCoins)
print(find_fakeCoin(0, numofCoins))