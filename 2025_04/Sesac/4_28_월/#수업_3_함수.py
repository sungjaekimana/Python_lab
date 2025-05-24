#함수 : 특정 기능끼리 묶어놓은 코드
#모듈 : 일을 작게 나누어서 처리하자
#모듈은 프로시저와 함수로 나눈다.
#프로시저는 일이 끝나고 값을 반환하지 않는다.
#함수는 일이 끝나고 값을 반환한다.
#c언어가 프로시저와 함수를 합쳐서 함수라고 부른다.
#파이썬의 경우는 def 키워드로 시작
#def 함수이름(매개변수들)
#   .......
#   return #원칙이 값 하나만 리턴한다.
           #만일 여러개 보내면 tuple타입으로 묶어서 전달한다.
#장점 : 유지보수가 편해진다. 
#       반복적인 일을 처리할 때 함수를 만들면 훨씬 간결하게 처리할 수 있다.
#       구조적 프로그래밍, 객제치향 프로그램에서 필수다.
# 함수는 15줄 넘어가면 안된다. A4용지 한장 넘어가면 안된다.

# def print_line(): #함수를 정의한다.
#     #pass #파이썬은 함수가 됐던 아니면 for, if나 등등등 코드가 없이 if 조건식{}
#     print("-"*30)
    
# print_line() # 함수를 호출한다.
# print_line()
# print_line()
# print_line()

# print(print_line())

# # 1부터 N까지의 합계를 구하는 함수 만들기
# def Sigma():
#     sum = 0
#     for i in range(1,11):
#         sum += i
#     return sum
# print(Sigma())
# 매개변수 : 함수 외부에서 내부로 값을 전달하기 위한 목적

def Sigma(limit):
    sum = 0
    for i in range(1,limit+1):
        sum += i
    return sum

print(Sigma(10))
print(Sigma(100))
print(Sigma(200))
print(Sigma(300))
print(Sigma(400))
