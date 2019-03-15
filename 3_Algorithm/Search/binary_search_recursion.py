# Binary Search_recursion

# O(logN)
def binarySearch_recursion(listofNum, num, start, end) :

    if start > end :
        return -1

    mid = (start+end) // 2
    if num == listofNum[mid] :
        return mid
    elif num > listofNum[mid] :
        return binarySearch_recursion(listofNum, num, mid+1, end)
    elif num < listofNum[mid] :
        return binarySearch_recursion(listofNum, num, start, mid-1)

    return -1


listofNum = [2,7,6,8,9,3,1,17,5,12,10,25]
listofNum.sort() # 이진탐색은 오름차순 정렬이 된 리스트에만 적용 가능
print(listofNum)

# 찾고자 하는 숫자 입력받기
num = input('찾고자 하는 정수를 입력하세요: ')
if num.isdecimal() :
    num = int(num)
    print('num :', num)
else :
    print('잘못된 입력입니다.')


start = 0
end = len(listofNum)-1

foundNum = binarySearch_recursion(listofNum, num, start, end)

# 결과 출력
if foundNum > 0 :
    print(f'{num} 리스트 인덱스번호는 {foundNum}입니다.')
else :
    print('찾고자 하는 숫자가 없습니다.')