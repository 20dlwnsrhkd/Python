array=[]
while(True):
    a = input("문자열을 입력해주세요: ")
    array.append(a)
    if(a==''):
        tuple_b=tuple(array)
        print(tuple_b,end='')
        break