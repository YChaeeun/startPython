
# O(n)
def factorial_1(num):
    result = 1
    for idx in range(2,num+1) :
        result *= idx
    return result

#print(factorial_1(2))

# recursive
# O(n)
def recur_factorial(num):
    if num <= 1 :    # 종료조건
        return 1
    print(num)
    return num * recur_factorial(num-1)

print(recur_factorial(4))