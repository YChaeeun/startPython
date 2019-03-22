def solution(n):
    list1 = list(str(n))
    list1.sort(reverse=True)
    return int("".join(list1))

print(solution(11861743))