
# 여러 개의 값들의 위치를 찾을 때 O(mn)
def linearSearch_2(listofNum, findNumList):
    numidxList = list()
    for i in range(0, len(listofNum)):
        for findNum in findNumList :
            if listofNum[i] == findNum :
                numidxList.append(i)
                findNumList.remove(findNum)
    return numidxList

# 중복된 특정 값의 위치를 모두 찾고 싶을 때 O(n)
def linearSearch_3(listofNum, findNum):
    numidxList = list()
    for idx in range(0, len(listofNum)):
        if listofNum[idx] == findNum :
            numidxList.append(idx)
    return numidxList

listofNum = [12,4,15, 1,6,3,7,9,21,4,5,97,1,33]
findNumList = [3, 4, 1, 21]

print(linearSearch_2(listofNum, findNumList))


findNum = 1
print(linearSearch_3(listofNum, findNum))
