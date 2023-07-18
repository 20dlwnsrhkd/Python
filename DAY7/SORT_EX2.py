n = int( input("수의 개수를 입력해 주세요"))
k= []
for i in range(n):
    k.append( int(input("수를 입력해 주세요")))

print(sorted(k, reverse=True))