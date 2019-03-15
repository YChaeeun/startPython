# 이전 연습문제를 재귀호출로 구성하기

def recur_findMaxNum(listofNum, idx):
    
    if idx == 0 :
        return listofNum[0]
    print('처음 ', idx, listofNum[idx])
    maxNum = recur_findMaxNum(listofNum, idx-1)

    print('그다음 ', idx, listofNum[idx], maxNum)
    if maxNum < listofNum[idx] :
        maxNum = listofNum[idx]

    print('반환값', maxNum)
    return maxNum

listofNum = [1,6,2,7,9]
print(recur_findMaxNum(listofNum, len(listofNum)-1))