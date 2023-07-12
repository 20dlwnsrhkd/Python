import time
import os
import psutil



## n, k = map(int, input('두 수를 공백으로 분리하여 입력 : ').split()) # N, K을 공백을 기준으로 구분하여 입력 받기
n = 25
k = 4
process = psutil.Process(os.getpid()) # 공간 복잡도를 위한 프로세스 id 얻기
start_time = time.time() # 시간 측정 시작, 입력 직접 받으면 대기시간 만큼 시간 증가

result = 0
while True: # 반복 루프 시작
    target = (n // k) * k # K로 나누어 지는 수를 구함, 예) 25 나누기 4 곱하기 4 = 처음 24
    result += (n - target) # N이 K로 나누어 떨어지는 수가 될 때까지 빼기, 1
    n = target # 25를 24로 수정 
    if n < k: # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
        break
    result += 1 # 횟수 증가
    n //= k # K로 나누기, n = 6
result += (n - 1) # 마지막으로 남은 수에 대하여 1씩 빼기, 6, 5 --> 4일때까지 2번 추가 빼기, 마지막 1번 나누고

print("1이 될때까지 최소 횟수는:", result )

end_time = time.time() # 측정 종료
print("time:", format(end_time - start_time, '.10f')) # 정확도 소수 아래 10자리로 수행 시간 출력
print('MB bytes :', process.memory_info().rss / (1024.0 * 1024.0)) # 해당 프로세스 메모리 공간, 메가 바이트 단위 