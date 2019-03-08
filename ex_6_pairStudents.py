
def pairStudents(listofStu) :
    pairs = list()
    lenList = len(listofStu)
    for i in range(0, lenList-1) :
        for j in range(i+1, lenList) :
            pairs.append(listofStu[i]+' - '+listofStu[j])

    return pairs

listofStudent = ['Tina', 'Leah', 'Lily','Ella']
print(pairStudents(listofStudent))