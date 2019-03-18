
def search_bfs(graph, start) :
    qu = list()
    visited = set()  

    result = list()
    # list보다 빠른 검색 속도, 그렇지만 순서가 없는 자료형이라 return visited 하면 안돼
    # 1) 값을 저장할 result 리스트를 따로 만들던지, 2) 결과를 바로바로 프린트하던지, 3) visited를 set말고 list로 구현한뒤 return 하던지

    qu.append(start)
    result.append(start)
    visited.add(start)

    while qu :
        node = qu.pop(0)
        print(node)  # 대신 바로 print
        for x in graph[node] :
            if x not in visited :
                qu.append(x)
                result.append(x)
                visited.add(x)
    
    return result


graph = {
    1 : [2,3],
    2: [1,4,5],
    3 : [1],
    4: [2],
    5 : [2]
}

print(search_bfs(graph, 1))