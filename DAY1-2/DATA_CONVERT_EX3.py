a,b,c = map(int, input("3개의 정수를 입력하세요").split())
total=a+b+c # 변수에 합 저장
avg=total/3 # 변수에 평균 저장
print(total, format(avg, ".2f")) # 합산 결과와 평균(소수점 2자리) 출력
