n,m = map(int,input("정수의 갯수와 합을 입력해 주세요: ").split()) # 데이터의 개수 N
data=[]
for i in range(n): # 전체 수열
    data.append(int(input("정수")))

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
         # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
        print(m,"부터",n,'까지')
    interval_sum -= data[start]

print(count)