def avg(*args):
    arr = []
    for i in args:
        arr.append(i)
        
    temp = 0
    for j in arr:
        temp += j
    
    return temp / len(arr)

m = input("입력할 정수의 길이를 말하세요")
k=[]
for i in range(int(m)):
    k.append(input("정수를 입력하세요"))
print("입력한 정수의 평균을 출력: ",avg(k) )
                
#미완