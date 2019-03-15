
# Graph

def printAllFriends(f_info, start) :

    qu = list()
    done = set()

    qu.append(start)
    done.add(start)

    while qu :
        friendtoprint = qu.pop(0)
        print(friendtoprint)

        for friend in f_info[friendtoprint] :
            if friend not in done :
                qu.append(friend)
                done.add(friend)


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


printAllFriends(friend_info, 'Tina')
