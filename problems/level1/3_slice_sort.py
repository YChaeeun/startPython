
def solution(array, commands):
    answer = list()
    for _, c in enumerate(commands) :
        new = array[c[0]-1:c[1]]
        new.sort()
        num = new[c[2]-1]
        answer.append(num)
    return answer

def solution_2(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))
print(solution_2(array, commands))