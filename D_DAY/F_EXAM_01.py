def dfs(graph, v, visited):
    visited[v]= True
    global result
    for i in graph[v]:
        if not visited[i]:
            result+=1
            dfs(graph,i,visited)


bung = int(input("병동의 개수: "))
num = int(input("연결된 병동의 개수: "))
nect = [[] for _ in range(bung + 1)]
for i in range(num):
    x, y = map(int, input().split())
    nect[x].append(y)
    nect[y].append(x)
    
visited = [False]*(bung+1)

result=0
dfs(nect,1,visited)
print("감염된 병동은",result,"입니다.")