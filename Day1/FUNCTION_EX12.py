from itertools import permutations
data = [1, 2, 3,4,5] # 데이터 준비
result = list(permutations(data, 3)) # 모든 순열 구하기
print('모든 순열을 출력 :', result)