# Insert Sort
# 삽입정렬

# O(N^2)
def insertSort(listofNum) :
    length = len(listofNum)
    for i in range(1, length) :
        j = i-1
        key = listofNum[i]
        while j >=0 and listofNum[j] > key :
            listofNum[j+1] = listofNum[j]
            j -= 1
        listofNum[j+1] = key
    return


def insertSort_desc(listofNum) :
    length = len(listofNum)
    for i in range(1, length) :
        j = i-1
        key = listofNum[i]
        while j >=0 and listofNum[j] < key :
            listofNum[j+1] = listofNum[j]
            j -= 1
        listofNum[j+1] = key
    return

listofNum = [5,2,1,3]
print('기존 리스트 :', listofNum)

insertSort(listofNum)
print('삽입정렬한 리스트 :', listofNum)

insertSort_desc(listofNum)
print('내림차순(삽입정렬) :',listofNum)