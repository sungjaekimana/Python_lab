# static 메서드 - 본래 메서드도 
class Test:
    def __init__(self, number):
        self.number = number
        
    def output(self):
        print(self.number)
# output함수는 매개변수인 self가 객체를 만들어서 전달할때만 작동된다.
# 대부분의 클래스는 데이터와 함수의 결합이다.
# 데이터는 없고 공통의 기능만 갖는 클래스를 만들수도 있다.


#사칙연산을 하는 클래스
#공통의 데이터 공간을 두고
class Calculator:
    def __init__(self, x, y): #공통데이터공간
        self.x = x
        self.y = y
        
    def add(self): #덧셈
        return self.x + self.y
    
    def sub(self): #뺄셈
        return self.x - self.y
    
c1 = Calculator(4,5)
print(c1.add())
print(c1.sub())

class Calculator2:
    def add(self, x, y):
        return x + y
    
    def sub(self, x, y):
        return x - y
       
c2 = Calculator2()
print(c2.add(4,5))
print(c2.sub(4,5))


#staticmethod는 객체와 아무 관계없다.
#self도 매개변수로 갖지 못한다.
#staticmethod의 사용목적은 객체를 안만들고 특정메소드를 사용하는 것이다.
class Calculator3:
    @staticmethod #데코레이터
    def add(x,y):
        return x + y
    
    @staticmethod
    def sub(x,y):
        return x - y
    
    @staticmethod
    def mul(x,y):
        return x * y
    
print(Calculator3.add(4,5))
print(Calculator3.sub(4,5))
print(Calculator3.mul(4,5))

#Math가 수학함수들 갖고 있음(sin, cos, round 등 ....)
#웹 개발을 할 때 게시글 : <h1>Hi Hello</h1>
#디비에 접근해야하는 코드를 각각의 클래스가 소유할 경우 문제점
#: 1. 디비 아이피 바뀌었을 떄 or 아이디나 패스워드가 바뀌면
#     모든 클래스를 다 바꿔야하는 문제가 발생하며 보안에도 문제가 생긴다.
#     패스워드가 드러나게하면 안된다.
#staticmethod나 classmethod로 구성된 클래스를 만들어서 사용하는것이 바람직하다.
#staticmethod 단점이 클래스 변수를 못건드린다.
#classmethod를 사용한다.
#staticmethod는 함수들간에 기능적 유기성은 있지만 데이터가 필요없을 때 유용하다.