n, m = map(int, input("행과 열을 입력해 주세요: ").split())

array = [[0] * m for _ in range(n)]  # N X M 크기의 2차원 
result = min(array[0])
for i in range (n):
    array[i] = map(int, (input("행의 카드의 수를 입력해주세요: ").split()))
    mini = min(array[i])
    if mini>result:
        result = mini
        
print(result)
## 미완