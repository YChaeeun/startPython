def solution(a, b):
    week = ['THU','FRI','SAT','SUN', 'MON', 'TUE', 'WED']
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    sumofdays = b
    for i in range(0,a-1) :
        sumofdays += days[i]
    
    return week[sumofdays % 7]

a = 5
b = 24
print(solution(a,b))