
def mergeSort_desc(listofNum) :
    
    if len(listofNum) <= 1:
        return 

    mid = len(listofNum) // 2

    # 그룹 나누기
    list1 = listofNum[:mid]
    list2 = listofNum[mid:]

    mergeSort_desc(list1)    # 첫번째 그룹 정렬
    mergeSort_desc(list2)    # 두번째 그룹 정렬

    # 병합
    i_1 = 0
    i_2 = 0
    i_num = 0

    while len(list1) > i_1 and len(list2) > i_2 :
        if list1[i_1] > list2[i_2] :
            listofNum[i_num] = list1[i_1]
            i_1 += 1
            i_num += 1
        else :
            listofNum[i_num] = list2[i_2]
            i_2 += 1
            i_num += 1

    while i_1 < len(list1) :
        listofNum[i_num] = list1[i_1]
        i_1 += 1
        i_num += 1

    while i_2 < len(list2) :
        listofNum[i_num] = list2[i_2]
        i_2 += 1
        i_num += 1

listofNum = [5,3,1,4,2]
print('기존 리스트 :', listofNum)

mergeSort_desc(listofNum)
print('내림차순(Merge) :',listofNum)