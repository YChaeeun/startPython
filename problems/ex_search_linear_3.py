
def findStudent(studentID) :
    studentIDList = [39, 14,67,105]
    studentNameList = ['Tina', 'Leah', 'Michelle', 'Lily']

    for idx in range(len(studentIDList)) :
        if studentID == studentIDList[idx] :
            return studentNameList[idx]
    return '?'

studentID = 55
print(findStudent(studentID))