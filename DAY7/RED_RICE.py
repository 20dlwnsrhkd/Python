n,m = list(map(int,input("떡의 개수와 떡의 길이를 공백으로 구별하여 입력해주세요:").split()))

array = list(map(int,input("떡의 높이를 입력하세요").split()))

start = 0
end = max(array)

result = 0
while(start<=end):
    total = 0
    mid = (start+end)//2
    for x in array:
        
        if x > mid:
            total += x -mid
        
    if total < m:
        end=mid-1
    else:
        result = mid
        start = mid +1
        
print(result)