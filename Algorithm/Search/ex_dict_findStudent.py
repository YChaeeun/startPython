
def findStudent(studentID) :
    studentIDList = [39, 14,67,105]
    studentNameList = ['Tina', 'Leah', 'Michelle', 'Lily']

    dictStudent = dict()

    for i in range(len(studentIDList)) :
        dictStudent[studentIDList[i]] = studentNameList[i]

    try : 
        return dictStudent[studentID]
    except :
        return '?'

studentID = 55
print(findStudent(studentID))