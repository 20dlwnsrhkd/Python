import random, time, os, psutil

n, k = map(int, input("동전의 종류와 가격을 입력해 주세요 공백으로 구분합니다: ").split())
array = []
for i in range(n):
    array.append(int (input("동전의 금액을 저장합니다: ")))
    

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