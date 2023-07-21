'''k = int(input("준비된 가래떡 K의 개수: "))
n = int(input("만들 가래떡 N의 개수: "))
array=[]
for i in range(k):
    array.append(int(input("떡의 높이를 입력하세요")))

start = 0
end = max(array)

result = 0
while(start<=end):
    total = 0
    for i in range(n):
        for j in range(k):
            
    mid = (start+end)//2
    for x in array:
        
        if x > mid:
            total += x -mid
        
    if total < n:
        end=mid-1
    else:
        result = mid
        start = mid +1
        
print(result)'''

def get_max_length(rice_cakes, target_count):
    start, end = 1, max(rice_cakes)
    result = 0

    while start <= end:
        total_count = 0
        mid = (start + end) // 2

        for rice_cake in rice_cakes:
            total_count += rice_cake // mid

        if total_count >= target_count:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result


K = int(input("준비된 가래떡 개수: "))
N = int(input("만들 가래떡 개수: "))

rice_cakes = []
for i in range(K):
    rice_cake_length = int(input(f"가래떡의 길이 {i+1}: "))
    rice_cakes.append(rice_cake_length)

result = get_max_length(rice_cakes, N)
print(f"최대 떡볶이 길이는 {result}입니다.")

