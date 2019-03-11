
# O(N^2)
def findSameName(listofName) :
    lenList = len(listofName)
    findMatch = list()
    for i in range(lenList-1) :
        for j in range(i+1, lenList) :
           if listofName[i] == listofName[j] :
               findMatch.append(listofName[i]) 
    return findMatch

listofName = ['Tom', 'Leah', 'Tina', 'Leah', 'chae', 'Tina']

result = findSameName(listofName)
print(result)