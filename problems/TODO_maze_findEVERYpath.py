# 미로탈출하기
# 그래프


# 다양한 경로를 모두 찾으려면 어떻게 해야 할까??? 흠...

def findPath(maze, start,end) :
    
    qu = list()
    visited = set()

    result = list()

    qu.append(start)
    visited.add(start)

    while qu : 
        path = qu.pop(0)
        print(path)
        print('v', visited)
        v = path[-1]
        if v == end :
            result.append(path)  # visited 때문에 path 가 최종적으로 한 개 밖에 안 나와
        for x in maze[v] :
            if x not in visited :
                qu.append(path+x)
                visited.add(x)
        

    # 최단 경로
    if result :
        print(result)
        shortest = result[0]
        for idx in range(0, len(result)) :
            if len(shortest) > len(result[idx]) :
                shortest = result[idx]
        return shortest
        
    else :
        return '?'

maze = {
    'a' :['f'],
    'b' : ['c','g'], 
    'c' :['n', 'd'],
    'd' : ['c', 'e'], 
    'e' :['d'],
    'f' : ['a', 'k'], 
    'g' :['b', 'h', 'l'],
    'h' : ['g', 'c', 'i'], 
    'i' :['n', 'j'],
    'j' : ['i', 'o'], 
    'k' :['f', 'l'],
    'l' : ['g', 'm', 'q'], 
    'm' :['l', 'n', 'r'],
    'n' : ['m', 'o', 's'], 
    'o' :['j', 'n'],
    'p' : ['k', 'q'],
    'q' : ['l', 'p', 'r'],
    'r' :['m', 'q'],
    's' : ['n','t', 'x'],
    't' :['s', 'y'],
    'u' :['p', 'v'],
    'v' : ['u'],
    'w' :['r'],
    'x' : ['s', 'y'],
    'y' : ['t', 'x']
}

path = findPath(maze, 'a', 'y')
print(path)