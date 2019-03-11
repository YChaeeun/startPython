
num = int(input('Enter the num : '))

# O(n)
def sumAllSquare(num) :
    sumAllSquare = 0
    for idx in range(1,num+1) :
        sumAllSquare += idx**2
    return sumAllSquare

resultSum = sumAllSquare(num)
print(f'방법 1: 1부터 {num}까지의 합은 {resultSum}입니다.')

# O(1)
def sumAllSquare_2(num) :
    sumAllSquare2 = num*(num+1)*(2*num+1) // 6
    return sumAllSquare2

resultSum2 = sumAllSquare_2(num)
print(f'방법 2: 1부터 {num}까지의 합은 {resultSum2}입니다.')

