import time
import os
import psutil



s = input("문자열을 입력해 주세요: ")
process = psutil.Process(os.getpid()) # 공간 복잡도를 위한 프로세스 id 얻기
start_time = time.time() # 시간 측정 시작, 입력 직접 받으면 대기시간 만큼 시간 증가

mo = ['a','e','i','o','u']
result=[]
for i in range(len(s)):
    if (s[i] in mo and s[i+1] =='g')or(s[i]=='g'and s[i-1]in mo) :
        continue
    else:
        result.append(s[i])
        
print(''.join(result))

end_time = time.time() # 측정 종료
print("time:", format(end_time - start_time, '.10f')) # 정확도 소수 아래 10자리로 수행 시간 출력
print('MB bytes :', process.memory_info().rss / (1024.0 * 1024.0)) # 해당 프로세스 메모리 공간, 메가 바이트 단위 