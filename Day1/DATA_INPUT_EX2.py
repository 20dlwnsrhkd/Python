s = input("주민등록 번호를 입력해 주세요. \'-\'로 구분됩니다. ").split('-')
print(''.join(s))

#최적화 - 함수를 여러개 사용해서 최적화한다고 한다.
print(''.join(input("주민등록 번호를 입력해 주세요. \'-\'로 구분됩니다. ").split('-')))