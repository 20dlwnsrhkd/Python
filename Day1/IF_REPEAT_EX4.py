s = int(input("1~100사이 정수를 입력해 주십시오. 그 수까지의 짝수의 합을 출력합니다"))
k=0

while True:
    if s%2==0:
        k=k+s
    if (s == 0): # 0인 경우
        break # 현재 반복문을 중단
    s= s-1
print(k)

while True:
    a=input('q가 입력될 때까지 무한 반복 : ')
    a=str(a)
    if (a == 'q'): # 0인 경우
        break # 현재 반복문을 중단
    else:
        print(a) # 출력 반복