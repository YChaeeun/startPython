
def solution(answer) :
    list1 = [1,2,3,4,5]
    list2 = [2,1,2,3,2,4,2,5]
    list3 = [3,3,1,1,2,2,4,4,5,5]
    
    score = [0,0,0]
    result = list()

    for idx, answer in enumerate(answer) :
        if list1[idx % len(list1)] == answer :
            score[0] += 1
        if list2[idx % len(list2)] == answer :
            score[1] += 1
        if list3[idx % len(list3)] == answer :
            score[2] += 1

    for idx, s in enumerate(score) :
        if s == max(score):
            result.append(idx+1)
    
    return result

answer = [1,3,2,4,2]
print(solution(answer))