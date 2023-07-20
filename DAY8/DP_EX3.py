# 정수 N을 입력 받기
n = int(input("정수를 입력해 주세요"))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블  1000 + 1 초기화
d=[1001]*(n+1)

# 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
d[1] = 1 # n이 1인 경우 경우의 수
d[2] = 3 # n이 2인 경우 경우의 수
for i in range(3, n + 1): # n이 3부터 경우의 수 처리
    d[i] = d[i-1] + d[i-2]*2# 점화식 적용, dp테이블 저장


# 계산된 결과 출력
print(d[n])