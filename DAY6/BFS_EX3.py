def BFS(x,y,L):

    for i in range(4): # 상하좌우 검사
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<n and 0<=ny<n and arr[nx][ny]==1: # 새로운 집 발견
            arr[nx][ny]=0
            cnt_arr[L]+=1 # 다음 좌표 설정
            BFS(nx,ny,L) # DFS 재귀 호출
from collections import deque
            
n = int(input('단지의 크기 N를 입력 : '))
arr = [list(map(int,input('단지 지도 세부 정보를 입력 : '))) for _ in range(n)]
total_cnt = 0 # 단지의 숫자 
cnt_arr=list() # 단지안에 속하는 집의 수 

dx = [-1, 0, 1, 0] # 4가지 방향 정의
dy = [0, 1, 0, -1]

q = deque()

for i in range(n): # 반복문 시작
    for j in range(n):
        if arr[i][j]==1:
            q.append((i, j)) # 초기 방문 노드 큐에 추가
            arr[i][j]=0
            cnt=1
            while q: # 큐가 존재하는 동안 루프 동작
                x,y=q.popleft() # 큐의 현재 노드를 꺼내고
                for z in range(4):
                    nx = x+dx[z] # 4방향 검사
                    ny = y+dy[z]
                    if 0<=nx<n and 0<=ny<n and arr[nx][ny]==1: # 집 발견하는 경우
                        arr[nx][ny] = 0
                        cnt+=1 # 집의 개수를 증가
                        q.append((nx,ny)) # 큐에 노드 추가
            cnt_arr.append(1)

print('총 단지수 :', len(cnt_arr))
cnt_arr.sort() 
for i in cnt_arr:
    print('각 집의 개수 :', i)