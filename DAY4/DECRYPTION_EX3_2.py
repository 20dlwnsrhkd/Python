import time
import os
import psutil


##샘플 코드
date = input("암호화된 문장을 입력")
process = psutil.Process(os.getpid()) # 공간 복잡도를 위한 프로세스 id 얻기
start_time = time.time() # 시간 측정 시작, 입력 직접 받으면 대기시간 만큼 시간 증가

value = ['a','e','i','o','u']
number = 0

while number< ( len(date)):
    print(date[number],end='')
    if date[number]in value:
        number +=2
    number+=1
    
    
end_time = time.time() # 측정 종료
print("time:", format(end_time - start_time, '.10f')) # 정확도 소수 아래 10자리로 수행 시간 출력
print('MB bytes :', process.memory_info().rss / (1024.0 * 1024.0)) # 해당 프로세스 메모리 공간, 메가 바이트 단위 