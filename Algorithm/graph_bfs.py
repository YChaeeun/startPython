
def search_bfs(graph, start) :
    qu = list()
    visited = set()

    qu.append(start)
    visited.add(start)

    while qu :
        node = qu.pop(0)
        for x in graph[node] :
            if x not in visited :
                qu.append(x)
                visited.add(x)
    return visited


graph = {
    1 : [2,3],
    2: [1,4,5],
    3 : [1],
    4: [2],
    5 : [2]
}

print(search_bfs(graph, 1))