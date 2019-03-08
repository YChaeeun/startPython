# 1 부터 입력받은 N까지 모두 더하기

num = int(input('Enter number : '))

# O(n)
def sumAll_fromONEtoN(num) :
    sumAll = 0

    for idx in range(1, num+1) :    # range(1, num+1) : 1 부터 num 까지
        sumAll += idx
    return sumAll

resultSum = sumAll_fromONEtoN(num)
print(f'방법 1: 1부터 {num}까지의 합은 {resultSum}입니다.')


# O(1)
def Gauss_Sum(num):    # n(n+1) / 2
    GaussSum = num*(num+1) // 2   # // : 정수부를 확실하게 구하기 위해서
    return GaussSum

resultSum2 = Gauss_Sum(num)
print(f'방법 2: 1부터 {num}까지의 합은 {resultSum2}입니다.')