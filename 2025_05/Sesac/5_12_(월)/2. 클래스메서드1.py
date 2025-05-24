class MyClass:
    #클래스변수의 영역이다.
    #객체를 만들던 말던 한번만 만든다.
    #생성자에서 이 부분을 건드리면 안된다.
    count = 0 #객체가 만들어질때마다 몇개 만들어졌는지 확인용도
    @staticmethod
    def addCount(): #staticmethod 입장에서는 매개변수인 self를 못쓰기에 count변수가 접근을 못한다.
        count += 1
        
# print(MyClass.addCount()) # error 코드
    
    @classmethod
    def increase(cls): #cls는 class이다.
        cls.count += 1
        
MyClass.increase()
print(MyClass.count)

#객체를 만들때 객체의 개수를 카운트하거나
#제한하는 클래스를 만들고자 할때 classmethod를 쓴다.

class SelfCount:
    __count = 0 #클래스 변수를 선언
                #class 안의 변수가 보존할 가치가 있다면 __(언더바2개)
    def __init__(self):
        SelfCount.__count+=1 #생성자에서 값 증가하기
        print(SelfCount.__count)

    @classmethod
    def count_output(cls):
        print(cls.__count)

s1 = SelfCount()
SelfCount.count_output()
s1 = SelfCount()
SelfCount.count_output()
s1 = SelfCount()
SelfCount.count_output()
s1 = SelfCount()
SelfCount.count_output()
# print(SelfCount.__count) #"이 속성을 볼수 없다"라는 에러메시지가 뜬다.