
def findGCD(num1, num2) :
    idx = min(num1,num2)
    while idx >0 :
        if num1 % idx == 0 and num2 % idx == 0 :
            return idx
        else :
            idx -= 1

print(findGCD(7, 12))


# 유클리드 호제법
# gcd(a,b) = gcd(b, a%b)
def gcd_Euclid(num1, num2) :
    if num2 == 0:
        return num1
    return gcd_Euclid(num2, num1%num2)


print(gcd_Euclid(60,24))