dic_sum = dict()
k=input("과목 개수를 입력하싶시오: ")
for i in range(int (k)):
    g = input("과목 명을 입력하세요: ")
    score = input("점수를 입력하세요: ")
    dic_sum[g]=int(score)
    
val=sum(dic_sum.value())/len(dic_sum)
print("전체 과목의 평균 점수는: ",val)

##미완