n = int( input("회원의 수를 입력해 주세요"))

array = []
for i in range(n):

    input_data = input("이름과 나이를 입력해 주세요").split()
    # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    
    array.append((input_data[0], int(input_data[1])))
    
array = sorted(array, key=lambda student: student[1]) # 람다식, 키 기준 정렬


for student in array:
    print(student[0],student[1])