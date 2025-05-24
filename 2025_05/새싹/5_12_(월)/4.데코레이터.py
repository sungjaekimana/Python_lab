# @staticmethod처럼 @시작한다. 
# 함수의 전후 동작을 감싸서 함수 가로채기를해서 뭔가 작업을 
# 처리하고 원래함수를 호출한다.

#데코레이터는 함수안에 또 함수를 만든다.(중첩함수)
#매개변수로 받아가서 중첩함수안에서 받아간 함수를 호출한다.
#파이썬에서는 주로 웹에서 많이 사용한다.
#반드시 로그인을 해야 접근이 가능한 함수를 만들고 싶다.
#함수를 중간에 가로채서 실행시간 체크를 할 수 있다.
def decorator1(func): #매개변수는 중첩함수안에서 호출될 함수.
    def wrapper():
        print("함수호출 전")
        func()
        print("함수호출 후")
    return wrapper #중첩함수의 참조를 반환해야한다.

@decorator1
def hello():
    print("Hello")
    
hello() #decorator1에게 납치당함. -> wrapper -> func()를 통해 함수 호출

import time
def time_decorator(callback):
    def innerfunction():
        callback()
        start = time.time()
        callback()
        end = time.time()
        print(f"{callback.__name__} 실행시간 : {end-start}초")
    return innerfunction
        
# @time_decorator
# def sigma():
#     s = 1
#     for i in range(1,1000000):
#         s += i
#         print("합계 : ", s)
        
# sigma()

#매개변수있고 반환값 있는 경우의 데코레이터 만들기
#callback - 뒤에서 호출한다.
#보통 호출자가 시스템이다.
#직접 호출을 못하고 데코레이터한테 사용자함수를 전달한다.
def mydecorator(callback):
    #호출될 함수가 어떤 매개변수를 가질지 알 수 없을경우에
    #tuple타입, dict타입
    def wrapper(*args, **kwargs):
        result = callback(*args, **kwargs)
        return result
    return wrapper

@mydecorator
def add(x, y):
    return x + y

print(add(5,7))

#문제 : 데코레이터 만들기 - 로그내보내기
#@mylog
#함수를 sigma 매개변수 s = sigma2(10)
"""
[Log] 함수이름 : sigma2
[Log] 입력값 : args = (10), kwargs = {}
[Log] 반환값 : 55
"""

def mylog(callback):
    def wrapper(*args, **kwargs):
        result = callback(*args, **kwargs)
        print(f"[LOG] 함수이름 : {callback.__name__}")
        print(f"[LOG] 입력값 : args {args} kwargs{kwargs}")
        print(f"[LOG] 반환값 : {result}")
        return result
    return wrapper

@mylog
def sigma2(limit=10):
    s = 0
    for i in range(1, limit+1):
        s += i
    return s
print(sigma2(100) )
print(sigma2(10))

@mylog #mylog를 가져다가 계속 써도 된다.
def sub(a, b):
    return a - b
print(sub(3,4))