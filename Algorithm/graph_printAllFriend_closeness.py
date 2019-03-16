
def printAll_close(f_info, start):

    qu = list()
    done = set()

    qu.append((start,0))   # 친밀도 기록, 튜플로 저장
    done.add(start)

    while qu :
        friendtoprint, close = qu.pop(0)
        print(friendtoprint, close)

        for friend in f_info[friendtoprint] :
            if friend not in done :
                qu.append((friend, close+1))
                done.add(friend)


    return



friend_info = {
        'Summer' : ['Tina', 'Leah', 'Lily'],
        'Tina' : ['Summer', 'Leah'],
        'Leah' : ['Summer', 'Tina', 'Lily', 'Jessy'],
        'Lily' : ['Summer', 'Leah'],
        'Jessy' : ['Leah', 'Michelle'],
        'Michelle' : ['Jessy'],
        'Erica' : ['Noah'],
        'Noah' : ['Erica']
}

printAll_close(friend_info, 'Summer')