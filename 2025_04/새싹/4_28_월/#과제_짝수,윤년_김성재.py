# # 과제1 : 정수를 받아가서 짝수이면 True 짝수가 아니면 False를 반환하는 함수를 만들어라.

# num = int(input("정수를 입력하세요"))

# def check_even(num):
#     if num % 2 == 0: #짝수인 경우
#         return True
#     else:
#         return False
    
# result = check_even(num)
# print(result)

# # 과제2 : 윤년 - 4년마다 옴, 100년에 1번씩 윤년이 아님, 400년에 한번씩 윤년임.

# year = int(input("연도를 입력하세요"))
# def check_yoonyear(year):
#     if year % 400 == 0:
#         year = True
#     elif year % 100 == 0:
#         year = False
#     elif year % 4 == 0:
#         year = True
#     else:
#         year = False
#     return year
# print(check_yoonyear(year))

# # 안수현님 풀이
# def is_leapYear(year):
#     if year % 4 == 0:
#         if year % 100 == 0 and year % 400 != 0:
#             return False
#         else:
#             return True
#     else:
#         return False

# year = int(input("년도를 입력하세요: "))
# print(is_leapYear(year))




def greet(name="친구"):
    print(f"{name}님, 안녕하세요!")

greet()
greet("지민")