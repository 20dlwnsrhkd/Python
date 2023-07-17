def dfs(graph, v, visited):
    visited[v]= True
    print("DFS 탐색 순서",[v] ,v,end='' )
    for i in graph[v]:
        if not visited[i]:
            print("방문하지 않은 노드 발견: ",graph[i])
            dfs(graph,i,visited)
graph = [
    [],
    [2,3],
    [1,8],
    [1,4,5],
    [3,5],
    [3,4],
    [7,8],
    [6,8],
    [2,6,7]
]

visited = [False]*9

dfs(graph,1,visited)