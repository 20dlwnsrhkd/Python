s = input("문자열을 입력해 주세요: ")
mo = ['a','e','i','o','u']
result=[]
for i in range(len(s)):
    if (s[i] in mo and s[i+1] =='g')or(s[i]=='g'and s[i-1]in mo) :
        continue
    else:
        result.append(s[i])
        
print(''.join(result))
        
    
    
##샘플 코드
date = input("암호화된 문장을 입력")
value = ['a','e','i','o','u']
number = 0

while number< ( len(date)):
    print(date[number],end='')
    if date[number]in value:
        number +=2
    number+=1