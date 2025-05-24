class Flyalbe:
    def fly(self):
        print("날 수 있다.")
        
    def walk(self):
        print("두 다리로 걷는다")
        
class Swimable:
    def swim(self):
        print("수영할 수 있다.")
        
    def walk(self):
        print("***두 다리로 걷는다***")
        
class Duck(Flyalbe, Swimable):
    def quack(self):
        print("꽥꽥")
        
# class Duck(Swimable, Flyalbe):
#     def quack(self):
#         print("꽥꽥")
        
d1 = Duck()
d1.fly()
d1.swim()
d1.quack()
d1.walk() #메서드명이 동일한 경우에는 앞에거를 호출한다.

#시스템이 제공하는 내장변수중에 __mro__가 상속받은 관계정보가 있어서
#이걸 따라 적용한다
#(<class '__main__.Duck'>, <class '__main__.Flyalbe'>, <class '__main__.Swimable'>, <class 'object'>)
print(Duck.__mro__) #클래스 멤버변수로 제공한다.
