from itertools import combinations

s = input("2자리 이상의 정수를 입력하세요: ")
x = int (input("제거할 1이상의 자연수 x를 입력하세요"))
value = list(combinations(s, len(s)-x)) 
# s에서 s의 길이에서 x개만큼 뺀 수를 뽑는 모든 조합 구하기
print(value)
print("제거후 가장 큰 수는",''.join(max(value)))
#문자열이어도 높은 수의 값이 max함수에 적용되기 때문에 가장 높은수가 출력된다
    


