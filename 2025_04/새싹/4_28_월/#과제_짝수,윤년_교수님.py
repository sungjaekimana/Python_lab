# 과제1 : 정수를 받아가서 짝수이면 True 짝수가 아니면 False를 반환하는 함수를 만들어라.

def isEven(n):
    if n % 2 == 0:
        return True
    return False

print(isEven(int(input("숫자를 입력하세요"))))


# 과제2 : 윤년 - 4년마다 옴, 100년에 1번씩 윤년이 아님, 400년에 한번씩 윤년임.

def isLeap(year):
    if (year % 4 ==0 and year % 100 != 0) or year % 400 ==0:
        return True 
    return False

print(isLeap(int(input("년도를 입력하세요"))))
    
    
    









