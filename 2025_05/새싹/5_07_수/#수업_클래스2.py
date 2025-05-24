class Person:
    #이 공간은 클래스 공간이다. 클래스 정의할때 딱 한번 실행된다. 
    #객체 만들때마다 실행되지 않는다. 그래서 list타입이나 dict타입등을 함부로 여기에 
    #선언하면 안된다. 
    name="홍길동"
    age=12
    phone=[] #공통공간 

    #생성자에서 변수를 만들자. 
    def __init__(self):
        self.name = ""
        self.age=0
        self.phone=[]

    def append(self, name="임꺽정", age=13, phone="010-0000-0001"):
        self.name = name 
        self.age = age
        self.phone.append( phone ) 

    def output(self):
        print(self.name, self.age, self.phone)

p1 = Person()
p1.append("장길산", 11, "010-0000-0003")

p2 = Person()
p2.append("김종서", 13, "010-0000-0004")

p1.output()
p2.output()

# # 문제. 주급계산
# # 주급 : 이름, 시급, 근무시간 ==> 객체지향으로 한사람분만

# class Employee:
#     def __init__(self, name, hourly_wage, worktime):
#         self.name = name
#         self.hourly_wage = hourly_wage
#         self.worktime = worktime
        
#     def cal_weekly_pay(self):
#         return self.hourly_wage * self.worktime
    
#     def output(self):
#         print(f"이름: {self.name}")
#         print(f"시급: {self.hourly_wage}원")
#         print(f"근무 시간: {self.worktime}시간")
#         print(f"주급: {self.cal_weekly_pay()}원")
    
# def main():
#     name = input("이름을 입력하세요 : ")
#     hourly_wage = int(input("시급을 입력하세요 : "))
#     worktime = int(input("근무시간을 입력하세요 : "))
#     emp = Employee(name, hourly_wage, worktime)
#     emp.output()

# main()
        
class Weekpay: #백현숙강사님 풀이, 한명만 입력할 때
    def __init__(self, name = "", work_time = 20, per_pay = 10000):
        self.name = name
        self.work_time = work_time
        self.per_pay = per_pay
        self.process()
        
    def process(self):
        self.pay = self.work_time * self.per_pay
        
    def output(self):
        print(f"{self.name} {self.work_time}, {self.per_pay} {self.pay}")
        
# w1 = Weekpay("홍길동", 20 ,20000)
# w1.output()

# wList = [
#     Weekpay("홍길동", 20 ,20000),
#     Weekpay("고길동", 10 ,50000),
#     Weekpay("김길동", 30 ,40000),
#     Weekpay("이길동", 40 ,20000),
#     Weekpay("장길동", 20 ,20000),
# ]
# for w in wList:
#     w.output()

class WeekPayManager:
    
    def __init__(self):
        self.wList = [
            Weekpay("홍길동", 20 ,20000),
            Weekpay("고길동", 10 ,50000),
            Weekpay("김길동", 30 ,40000),
            Weekpay("이길동", 40 ,20000),
            Weekpay("장길동", 20 ,20000),
        ]
    
    def output(self):
        for w in self.wList:
            w.output()
                
mgr = WeekPayManager()
mgr.output()