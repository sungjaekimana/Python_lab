#주급 계산하기
#주급을 계산하기 위해서는 시급, 주 근무시간이 필요하다
per_pay = input("시간 당 급여액")
time = input("주 근무시간")
weekly_pay = int(per_pay) * int(time)
print(weekly_pay)

per_pay = int(input("시간 당 급여액 : "))
time = int(input("주 근무시간 : "))
weekly_pay = per_pay * time
print(weekly_pay)
print(type(weekly_pay))