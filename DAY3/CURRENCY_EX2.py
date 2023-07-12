import random, time, os, psutil

n, k = map(int, input("동전의 종류와 가격을 입력해 주세요 공백으로 구분합니다: ").split())
array = []
for i in range(n):
    array.append(int (input("동전의 금액을 저장합니다: ")))
    
process = psutil.Process(os.getpid()) # 공간 복잡도를 위한 프로세스 id 얻기
start_time = time.time() # 시간 측정 시작, 입력 직접 받으면 대기시간 만큼 시간 증가

array.sort(reverse=True)
result = 0
for coin in array:
    if (coin >= k):
        continue
    result += k//coin
    k %= coin
    if (k <= 0):
            break

print(result)

end_time = time.time() # 측정 종료
print("time:", format(end_time - start_time, '.10f')) # 정확도 소수 아래 10자리로 수행 시간 출력
print('MB bytes :', process.memory_info().rss / (1024.0 * 1024.0)) # 해당 프로세스 메모리 공간, 메가 바이트 단위 