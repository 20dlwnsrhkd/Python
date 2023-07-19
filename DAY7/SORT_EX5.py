import sys, bisect

si = sys.stdin.readline
n = int(si())
store=sorted(map(int, si().split()))
m = int(si())
wish=list(map(int, si().split()))

for x in wish:
    idx = bisect.bisect_left(store,x)
    
    if store[idx] == x:
        print('yes',end=' ')
    else:
        print('no',end=' ')



'''from bisect import bisect_left, bisect_right

def count_by_value(array,k):
    left_index = bisect_left(array, x)
    right_index = bisect_right(array, x)
    if not right_index - left_index:
        return "N0"
    return "YES"  # 특정 값의 개수 반환


n = int(input("부품의 종류 수를 입력해 주세요: "))
jong=[]
k = []
for i in range(n):
    jong.append(int(input("부품의 종류를 입력해 주세요")))
jong.sort()
m = int(input("찾으시는 부품의 종류 수를 입력해 주세요: "))
for i in range(m):
    k = (int(input("찾으시는 부품의 종류를 입력해 주세요")))
    
for i in range(m): 
    count = count_by_value(jong, k[i])
    print(count,end='') '''
