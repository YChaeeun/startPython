
# 순차 탐색 
# 최악의 경우 시간복잡도 O(n)
def linearSearch(listofNum, findNum):
    for idx in range(0, len(listofNum)):
        if listofNum[idx] == findNum :
            return idx
    return -1

# 리스트
listofNum = [12,4,15,6,3,7,9,21,4,5,97,1,33]

# 사용자에게 findNum을 입력받기
while True:
    findNum = input('찾고자하는 숫자를 입력하세요(정수) : ')

    if findNum.isdecimal() :
        findNum = int(findNum)
        break
    else :
        print('정수를 입력해주세요\n')

# 함수 호출하기
findNumIndex = linearSearch(listofNum, findNum)

# 결과 출력하기
if findNumIndex >0 : 
    print(f'{findNum}은 리스트의 {findNumIndex+1}번째 위치에 있습니다.')
else :
    print('찾고자 하는 숫자가 리스트에 없습니다.')