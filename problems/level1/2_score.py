
def solution(answer) :
    list1 = [1,2,3,4,5]
    list2 = [2,1,2,3,2,4,2,5]
    list3 = [3,3,1,1,2,2,4,4,5,5]

    answer2 = list()

    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for idx in range(0,len(answer)) :
        if list1[idx % len(list1)] == answer[idx] :
            cnt1 += 1
        if list2[idx % len(list2)] == answer[idx] :
            cnt2 += 1
        if list3[idx % len(list3)] == answer[idx] :
            cnt3 += 1

    maxint=max(cnt1, cnt2, cnt3)

    if maxint == cnt1 :
        answer2.append(1)
    if maxint == cnt2 :
        answer2.append(2)
    if maxint == cnt3 :
        answer2.append(3)
    

    return answer2

answer = [1,3,2,4,2]
print(solution(answer))