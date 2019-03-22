#sum([i for i in range(1,num+1) if i%2 ==0])

# 짝수 합 구하기
def sumeven(num):
    a = list()
    for i in range(1,num+1):
        a.append(i)
    return sum(list(filter(lambda i:i%2==0, a)))
