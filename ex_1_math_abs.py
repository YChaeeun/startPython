import math

num = int(input('Enter number: '))

def makeAbs(num):
    if num >= 0 :
        return print(num)
    else :
        return print(-num)

def absSquare(num) :
    numSquared = num*num
    return print(math.sqrt(numSquared))

# math.sqrt(num) : num 루트

makeAbs(num)
absSquare(num)



