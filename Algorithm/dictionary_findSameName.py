
# O(n)
def findSameName(listName) :
    dictName = dict()

    # 이름들이 반복된 횟수 저장
    for name in listName :
        if name in dictName :
            dictName[name] += 1
        else :
            dictName[name] = 1

    repeatedName = set()

    # 횟수가 2개 이상인 이름들을 집합에 저장(add)
    for name in dictName :
        if dictName[name] > 1 :
            repeatedName.add(name)
    
    return repeatedName


listName = ['Tina', 'Leah', 'Jenny', 'Leah', 'Jessy']


print(findSameName(listName))