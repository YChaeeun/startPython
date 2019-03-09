# 이전 연습문제를 재귀호출로 구성하기

def recur_sumAll(num):
    if num <= 1:
        return 1
    return num+recur_sumAll(num-1)

print(recur_sumAll(10))