import random
row_hole=[] 
col_hole=[] 
for i in range(6): #함정 생성
        row_hole.append(random.randint(1,9))
        col_hole.append(random.randint(1,9))    
print(row_hole,col_hole)
input_data = input('나이트의 위치 a~h, 1~8 입력 하기 : ') # 현재 나이트의 위치 입력받기, a1
row = int(input_data[1]) # 정수형 입력 받음, 1
column = int(ord(input_data[0])) - int(ord('a')) + 1 # 아스키 코드로 변환, 인덱스 값 계산을 위해 a를 뺀다. 이후 더하기 1
print(int(ord(input_data[0])) - int(ord('a'))+1)
# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)] # 시뮬레이션 문제와 같이 좌표 이동 정의

result = 0 # 이동 횟수 초기화
count = 0 #회피 횟수 초기화
for step in steps: # steps 8가지 방향을 순서대로 수행
    next_row = row + step[0] #  steps 요소 더하기
    next_column = column + step[1] # steps 요소 더하기
    for j in range(6):
        if(next_column==col_hole[j])and(next_row==row_hole[j]): #함정일 경우 회피 회수 추가
            count+=1
    print(next_row, next_column) # 내부 좌표 디버깅
    
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8: # 둘다 1이상 8이하이면

        result += 1 # 해당 위치로 이동이 가능하다면 카운트 증가

print(result-count,"번 이동할 수 있습니다.(함정",count,"회 회피!)") #이동 횟수에서 함정인 경우를 빼서 사용