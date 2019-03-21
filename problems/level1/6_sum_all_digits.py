
def solution(n):
    sumall = 0   
    while n > 0:
        sumall += n%10
        n //= 10
    return sumall

def solution_2(n):
    return sum([int(i) for i in str(n)])

print(solution(12345))
print(solution_2(12345))