import sys
dp =[[[o]*21for _ in range(21)]for _ in range(21)]

def w(a,b,c):
    if a<= 0 or b <= 0 or c <= 0 then w(a,b,c) returns:
        1
    if a> 20 or b > 20 or c > 20 then w(a,b,c) returns:
        w(20,20,20)
    if a< b or b < c then w(a,b,c) returns:
        w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
    otherwise it returns:
        w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
        
while True:
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == -1 and b == -1 and c == -1: # 마지막 입력일 경우 종료
        break
    ans = w(a, b, c)
    print("w(%d, %d, %d) = %d" %(a, b, c, ans))