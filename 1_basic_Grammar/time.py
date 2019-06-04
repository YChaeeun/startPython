from datetime import datetime

now = datetime.today()
print(now.weekday())
print(now.month)
print(now.day)

week = now.weekday()
if week == 0 :
    print('월요일')
elif week == 1:
    print('화요일')
elif week == 2:
    print('수요일')
elif week == 3:
    print('목요일')
elif week == 4:
    print('금요일')
elif week == 5:
    print('토요일')
else :
    print('일요일')