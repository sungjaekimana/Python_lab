# 이름, 국어, 영어, 수학, 총점, 평균
# 평균에 대해서 수(90), 우(80), 미(70), 양(60), 가(60미만)
# 학생 3명

#입력
namelist = []
korlist = []
englist = []
mathlist = []
totallist = []
avelist = []
gradelist = []

for i in range(3):
    name = input("이름을 입력: ")
    kor = int(input("국어점수는 :"))
    eng = int(input("영어점수는 :"))
    math = int(input("수학점수는 :"))
    
    namelist.append(name)
    korlist.append(kor)
    englist.append(eng)
    mathlist.append(math)

for i in range(len(namelist)):
    total = kor + eng + math
    totallist.append(total)
    
    ave = total / len(namelist)
    avelist.append(ave)
    
for i in range(len(namelist)):
    if avelist[i] > 90:
        grade = "수"
    elif avelist[i] > 80:
        grade = "우"
    elif avelist[i] > 70:
        grade = "미"
    elif avelist[i] > 60:
        grade = "양"
    else: grade = "가"
    gradelist.append(grade)
    
for i in range(len(namelist)):
    print(namelist[i], korlist[i], englist[i], mathlist[i])


