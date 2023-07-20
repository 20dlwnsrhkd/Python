import math
def is_prime_number(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

while True: 
    
    s = input("숫자열을 입력해 주세요: ")
    if s =='0':
        print("종료")
        break
    s_list = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            s_list.append(int(s[i:j]))

    # 리스트 내 소수를 판별하여 새로운 리스트 생성
    prime_list = [x for x in s_list if is_prime_number(x)]

    if not prime_list:
        print("없음")
    else:
        result = max(prime_list)
        print(result)
