# #문제1. 주급계산 :이름, 근무시간, 시간당급여액, 추가수당 : 근무시간이 20시간을 초과하면 
# #               시간당급여액에 50%를 가산한다
# #   이름 근무시간 시간당급여   기본금액  수당   총액  
# #  홍길동  30     10000     300000  50000  350000

# name = input("이름은?")
# time = int(input("근무시간은?"))
# pay = int(input("시간당급여는"))

# basic_pay = int(time * pay)
# over_pay = 0

# if time > 20:
#     over_pay = (pay * 0.5) * (time-20)
#     total_pay = basic_pay + over_pay
    
# print(f"{name},{time},{pay},{basic_pay},{over_pay},{total_pay}")

"""
컴퓨터활용능력시험
이름 필기(400) 워드(200) 스프레드시트(200) 프리젠테이션(200)
총점을 구하고 등급 800 이상이 A, 800미만 600이상이 B, 600미만 400이상이 C
400 미만은 D, 재시험 요망
"""

# name = input("이름은?")
# write = int(input("필기점수는?"))
# word = int(input("워드점수는?"))
# spread = int(input("스프레드시트점수는?"))
# ppt = int(input("프리젠테이션점수는?"))

# score = write + word + spread + ppt

# if score >= 800:
#     print("A")
# elif score >= 600:
#     print("B")
# elif score >= 400:
#     print("C")
# else:
#     print("D","재시험요망")

