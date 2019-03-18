

graph = {
    'A' : ['B','D','G'],
    'B' : ['A', 'C'],
    'C' : ['B'],
    'D' : ['A', 'E', 'F'],
    'E' : ['D'],
    'F' : ['D'],
    'G' : ['A']
}


# 너비우선 탐색
def bfs(graph, start):
    qu = list()
    visited = list()  
    
    # set은 중복을 허용하지 않고, 순서가 없는 자료형. 검색을 할 때 빠르게 할 수 있음!! hash로 짜여져 있기 때문이래
    # 근데 지금은 검색해야 하는 양이 적기 때문에 그냥 visited 를 리스트로 짜겠음....

    qu.append(start)
    visited.append(start)

    while qu :
        node = qu.pop(0)
        for x in graph[node] :
            if x not in visited :
                qu.append(x)
                visited.append(x)

    return visited


# 넓이우선 탐색
def dfs(graph, node, visited):

    if node not in visited :
        visited.append(node)
        for x in graph[node] :
            dfs(graph, x, visited)

    return visited

print(bfs(graph, 'A'))

print('dfs', dfs(graph, 'A', []))