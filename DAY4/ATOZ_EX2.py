s = input("문자를 입력해주세요: ")
a_list = [-1]*26
for i in range (len(s)):
    h = int(ord(s[i])) - int(ord('a'))
    a_list[h]=i
    
print(a_list)

a_dict = {}

for i in range(26):
    a_dict[int(ord('a'))+i]=-1
    
for j in range(len(s)):
    a_dict[int(ord(s[j]))]=j
    
print(a_dict.values())