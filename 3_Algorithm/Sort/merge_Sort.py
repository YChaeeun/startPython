# MergeSort
# 재귀함수를 이용하여 그룹을 나누고, 이후 병합하는 알고리즘

# O(N^logN)
def mergeSort(listofNum) :
    
    if len(listofNum) <= 1:
        print('return')
        return 

    mid = len(listofNum) // 2

    # 그룹 나누기
    list1 = listofNum[:mid]
    list2 = listofNum[mid:]

    print('나누기 1', mid)
    mergeSort(list1)    # 첫번째 그룹 정렬
    print('첫번째', list1)
    print()
    print('나누기 2', mid)
    mergeSort(list2)    # 두번째 그룹 정렬
    print('두번째', list2)

    # 병합
    i_1 = 0
    i_2 = 0
    i_num = 0

    print('병합시작')
    while len(list1) > i_1 and len(list2) > i_2 :
        if list1[i_1] < list2[i_2] :
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
    print('병합 끝\n')



listofNum = [5,3,1,4,2]
print('기존 리스트 :', listofNum)

mergeSort(listofNum)
print('Merge Sort 리스트 :', listofNum)
