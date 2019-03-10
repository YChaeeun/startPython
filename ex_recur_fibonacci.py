
def fibo(num):
    if num <= 1:
        print('처음', num)
        return num
    print('다음', num, num-2, num-1)
    return fibo(num-2) + fibo(num-1)


print(fibo(6))
