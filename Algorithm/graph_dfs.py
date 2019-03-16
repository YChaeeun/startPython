
def dfs(graph, start,visited):

    if start not in visited:
        visited.append(start)
        for node in graph[start]:
            dfs(graph,node, visited)
            
    return visited


graph1 = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}

graph2 = {
    'A' : ['B','D','G'],
    'B' : ['A', 'C'],
    'C' : ['B'],
    'D' : ['A', 'E', 'F'],
    'E' : ['D'],
    'F' : ['D'],
    'G' : ['A']
}

print(dfs(graph2,'B', []))