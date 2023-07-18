from bisect import bisect_left, bisect_right

def count_by_value(array,x):
    left_index = bisect_left(array, x)
    right_index = bisect_right(array, x)
    if not right_index - left_index:
        return -1
    return right_index - left_index  # 특정 값의 개수 반환

n,x = list(map(int,input("원소의 개수와 개수를 찾으려는 원소를 입력하세요: ").split()))
array=[]
for i in range(n):
    array.append(int(input("원소를 입력하세요: ")))

count = count_by_value(array, x)
print("특정 값의 개수는 {}입니다.".format(count))