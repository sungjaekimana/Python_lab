#주급계산하기.ver2
#입력 - 이름, 시급, 근무시간
employee_name = input("이름 :")
work_time = int(input("일한시간 : "))
per_pay = int(input("시간당 급여액 :"))

pay = work_time * per_pay

#대부분의 언어는 문자열과 정수를 더하면 정수를 문자열로 바꿔서 문자와와 합산연산을 수행, 파이썬은 str을 사용하여 정수를 문자열로 바꿔줘야한다.
print(employee_name + " 님의 급여는 " + str(pay) + " 입니다.")
print(f"{employee_name}님의 급여는 {pay}입니다.") #f스트링을 활용해서도 사용가능