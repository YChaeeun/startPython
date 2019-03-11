
# 제일 큰 숫자를 찾는 함수
def findMax(listOfnum) :
    tempMax = listOfnum[0]
    for idx, num in enumerate(listOfnum) :
        if tempMax < num :
            tempMax = num
            maxisHere = idx
    MaxinList = tempMax
    return MaxinList, maxisHere

listOfnum = list()

# 사용자에게 숫자 입력받기
print('정수 10개를 입력하세요')
for _ in range(10) :
    num = int(input('Enter the num :'))
    listOfnum.append(num)

Max, maxisHere = findMax(listOfnum)
print(f'입력받은 숫자는 {listOfnum}입니다.')
print(f'그중 가장 큰 숫자는 {maxisHere+1}번째 자리 에 위치한 {Max}입니다.')