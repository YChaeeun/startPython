# 미로탈출하기
# 그래프


def findPath(maze, start,end) :
    
    qu = list()
    visited = set()

    qu.append(start)
    visited.add(start)

    while qu :
        path = qu.pop(0)
        v = path[-1]  # 리스트의 맨 뒤 값
        print('path :',path, '/ v :', v)
        print('visited : ', visited)

        if v == end :
            return path
        for x in maze[v] :
            print('for문 시작')
            if x not in visited:
                qu.append(path+x)
                visited.add(x)
                print('qu', qu)
                print()

    return '?'

maze = {
    'a' :['e'],
    'b' : ['c','f'], 
    'c' :['b', 'd'],
    'd' : ['c'], 
    'e' :['a', 'i'],
    'f' : ['b', 'g', 'j'], 
    'g' :['f', 'h'],
    'h' : ['g', 'l'], 
    'i' :['e', 'm'],
    'j' : ['f', 'k', 'n'], 
    'k' :['j', 'o'],
    'l' : ['h', 'p'], 
    'm' :['i', 'n'],
    'n' : ['m', 'j'], 
    'o' :['k'],
    'p' : ['l'] 
}

path = findPath(maze, 'a', 'p')
print(path)