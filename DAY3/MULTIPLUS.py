S = input("수를 입력하세요:")

result = int(S[0])

for i in range(1, len(S)):
    num = int(S[i])
    if num <= 1 or result <=1:
        result += num
    else:
        result *=num
        
print("최종 연삽 결과 합산된 수의 크기는: ",result)