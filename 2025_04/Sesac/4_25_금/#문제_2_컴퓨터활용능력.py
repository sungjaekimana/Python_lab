"""
컴퓨터활용능력시험
이름 필기(400) 워드(200) 스프레드시트(200) 프리젠테이션(200)

총점을 구하고 등급 800 이상이 A, 800미만 600이상이 B, 600미만 400이상이 C
400 미만은 D, 재시험 요망
"""

person = input("이름을 입력하세요 ")
writing = int(input("필기 점수를 입력하세요 "))
word = int(input("워드점수를 입력하세요 "))
sheet = int(input("스프레드시트 점수를 입력하세요 "))
ppt = int(input("프리젠테이션 점수를 입력하세요 "))

total_score = writing + word + sheet + ppt

# if total_score >= 800:
#     print("A")
# elif total_score > 800 and total_score >= 600 :
#     print("B")  
# elif total_score > 600 and total_score >= 400 :
#     print("C")
# else:
#     print("D","재시험요망")


#계산 - 교수님
if total_score > 800:
    grade = "A"
elif total >= 600:
    grade = "B"
elif total >= 400:
    grade = "C"
else:
    grade = "D, 재시험요망"
    
print(f"{person},{writing},{word},{sheet},{ppt},{grade}")