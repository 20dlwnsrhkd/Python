fr,sc = input("주민번호를 입력하세요:").split('-')
if(len(fr)!=6)or(len(sc)!=7):##주민번호의 자리수가 이상을 감지
    print("주민번호의 길이가 잘못되었습니다.")
elif(int(fr[:2])>23)and((int(sc[0])<3)or(int(sc[0])>4)and(int(sc[0])<7)):
    print("생년월일이 잘못되었습니다.")# 2000이후 때어난 사람의 출생년도가 23보다 큰지 감지
elif(int(fr[2:4])>12):#태어난 달이 12보다 큰지 감지
    print("생년월일이 잘못되었습니다.")
elif(int(fr[4:])>31):#태어난 날이 31보다 큰지 감지
    print("생년월일이 잘못되었습니다.")    
else:
    print("올바른 주민번호입니다.")
    if(int(sc[0])>2and int(sc[0])<5)or int((sr[0])>7): #2000이후 때어난 사람 감지
        print(20,fr[:2],'년',fr[2:4],'월',fr[4:],'일')
    else:
        print(19,fr[:2],'년',fr[2:4],'월',fr[4:],'일')
        
    if(int(sc[0])%2==1): # 성별 감지
        print("성별: 남성")
    else:
        print("성별: 여성")
        
    if(int(sc[1:3])<9): # 지역번호
        print("거주지: 서울")
    elif(int(sc[1:3])<13):
        print("거주지: 부산")
    elif(int(sc[1:3])<16):
        print("거주지: 인천")
    elif(int(sc[1:3])<26):
        print("거주지: 경기도")
    elif(int(sc[1:3])<35):
        print("거주지: 강원도")
    elif(int(sc[1:3])<40):
        print("거주지: 충청북도")
    elif(int(sc[1:3])<42):
        print("거주지: 대전")
    elif(int(sc[1:3])==44)or(int(sc[1:3])==96):
        print("거주지: 세종시")
    elif(int(sc[1:3])<48):
        print("거주지: 충청남도")
    elif(int(sc[1:3])<55):
        print("거주지: 전라북도")
    elif(int(sc[1:3])<67):
        print("거주지: 광주시")
    elif(int(sc[1:3])<70):
        print("거주지: 대구시")
    elif(int(sc[1:3])<82):
        print("거주지: 경상북도")
    elif(int(sc[1:3])==85)or(int(sc[1:3])==90):
        print("거주지: 울산시")
    elif(int(sc[1:3])<92):
        print("거주지: 경상남도")
    elif(int(sc[1:3])<96):
        print("거주지: 제주도")

        