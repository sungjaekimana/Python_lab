class A:
    def __init__(self):
        print("A 생성자 호출")
        
class B(A): #A를 상속받음
    def __init__(self):
        print(("B 생성자 호출"))
        super().__init__() #부모생성자 호출하기
        #A.__init__(self) - 파이썬 이전버전에서 문제 발생가능성 있음.
     
class C(A): #A를 상속받음
    def __init__(self):
        print(("C 생성자 호출"))
        super().__init__() #부모생성자 호출하기
        
class D(B,C): #B,C를 둘다 받으면서 결과적으로 A가 두번 상속된다.
    def __init__(self)
        print(("D 생성자 호출"))    
        super().__init__() #부모생성자 호출하기
        
d = D() #객체생성 - mro 규칙을 따라간다.

#isinstance(객체, 클래스) 이 객체가 클래스의 인스턴스인지 확인해준다.
print(isinstance(d, A)) #True
print(isinstance(d, B)) #True
print(isinstance(d, C)) #True
print(isinstance(d, object)) #True
print(isinstance(d, str)) #False

#object - 모든 클래스의 Base 클래스이다. 무조건 상속을 받는다.
a = object()
print(a.__class__)