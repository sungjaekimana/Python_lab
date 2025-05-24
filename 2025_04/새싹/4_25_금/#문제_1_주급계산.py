#문제1. 주급계산 :이름, 근무시간, 시간당급여액, 추가수당 : 근무시간이 20시간을 초과하면 
#               시간당급여액에 50%를 가산한다
#   이름 근무시간 시간당급여   기본금액  수당   총액  
#  홍길동  30     10000     300000  50000  350000

work_time = int(input("근무시간을 입력하세요 "))
name = input("이름을 입력하세요 ")
time_pay = int(input("시간당 급여액을 입력하세요 "))

basic_pay = int(work_time * time_pay)
plus_pay = 0

if work_time > 20 :
    plus_pay = (time_pay * 0.5) * (work_time - 20)
total_pay = basic_pay + plus_pay

print(f"{name}, {work_time}, {time_pay}, {int(basic_pay)}, {int(plus_pay)}, {int(total_pay)}")

