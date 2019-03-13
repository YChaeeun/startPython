# Selection sort
# 작은 값을 찾아서 위치 바꾸기

# O(N^2)
def selectSort(listofNum) :
    length = len(listofNum)
    for i in range(0,length-1) :
        min_idx = i
        for j in range(i+1, length) :
            if listofNum[min_idx] > listofNum[j] :
                min_idx = j

        # 위치 바꾸기
        listofNum[i], listofNum[min_idx] = listofNum[min_idx], listofNum[i]
        

def selectSort_desc(listofNum) :
    length = len(listofNum)
    for i in range(0,length-1) :
        max_idx = i
        for j in range(i+1, length) :
            if listofNum[max_idx] < listofNum[j] :
                max_idx = j

        # 위치 바꾸기
        listofNum[i], listofNum[max_idx] = listofNum[max_idx], listofNum[i]

listofNum = [5,2,8,1,3,9,4,10,7,6]
print('기존 리스트 :', listofNum)

selectSort(listofNum)
print('선택정렬한 리스트 :', listofNum)

selectSort_desc(listofNum)
print('내림차순(선택정렬) :',listofNum)