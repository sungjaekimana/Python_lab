# 이름, 국어, 영어, 수학, 총점, 평균
# 평균에 대해서 수(90), 우(80), 미(70), 양(60), 가(60미만)
# 학생 3명

name_list = []
kor_list = []
eng_list = []
math_list = []
total_list = []
average_list = []
grade_list = []

for i in range(3): # for문 안에서만 돌린다.
    name = input("이름은? ")
    name_list.append(name)
    
    kor = int(input("국어 점수는? "))
    kor_list.append(kor)
    
    eng = int(input("영어 점수는? "))
    eng_list.append(eng)
    
    math = int(input("수학 점수는? "))
    math_list.append(math)

    total = kor + eng + math
    total_list.append(total)
    
    average = total // 3
    average_list.append(average)


for i in range(3):
    if average_list[i] >= 90:
        grade = "수"
    elif average_list[i] >= 80:
        grade = "우"
    elif average_list[i] >= 70:
        grade = "미"
    elif average_list[i] >= 60:
        grade = "양"
    else:
        grade = "가"
    grade_list.append(grade)

    
    
for i in range(3):
    print(f"{name_list[i]}님의 평균점수는 {average_list[i]} 등급은 {grade_list[i]} 입니다.")

    
    

    

