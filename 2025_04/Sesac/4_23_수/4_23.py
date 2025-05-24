print("출력을 하고자 할때 사용한다")

print(5+6)

a = 10 #a라는 변수에 값 10을 저장(할당)하라
b = 20 #b라는 변수에 값 20을 저장하라
c = a+b #a의 값 10과 b의 값 20을 읽어와서 더한 뒤에 c에 넣어라
        #좌변에는 변수만 우변에는 아무거나 올 수 있다
print(a,b,c) #a,b,c변수의 값을 읽어서 화면에 출력하라

#값입력하기 - 입력함수가 동시에 출력도 가능
a = input("a = ")
b = input("b = ")
c = a+b #모든 입력은 unicode다 그래서 a도 b도 문자로 인식한다
print(a,b,c) #문자 + 문자 = 문자 덧붙이기
d = int(a) + int(b) #int는 문자를 숫자로 바꾼다
print(a,b,d)

#사각형의 면적 구하기(가로, 세로 입력받아서 면적을 구하고자 한다.)
#입력데이터 : 가로, 세로
#출력데이터 : 면적
#입력 -> 계산이나 출력을 생각하지 말자
width = input("가로 ; ")
height = input("세로 ; ")
#계산
surface = int(width) * int(height)
#출력
print( surface )

#주급 계산하기 시간당 급여액과 근무시간을 입력받아서 주급을 계산하기 - 개인적으로 만들었음
hourlywage = input("시간당급여액 ; ")
time = input("근무시간 ; ")
weeklywage = int(hourlywage) * int(time)
print(weeklywage)

#주급 계산하기 시간당 급여액과 근무시간을 입력받아서 주급을 계산하기
work_time = input("근무시간 ; ")
per_pay = input("시간당 급여액 ; ")
pay = int(work_time) * int(per_pay)
print("근무시간은",work_time, "시간당급여액",per_pay, "주급은", pay)

#이름하고 주소를 입력받아서 한 문장으로 출력하고 싶다
#각 변수는 특정타입만 저장하지 않는다
# a = 4
# print(a,type(a)) #type명령어는 변수 a의 타입이 아니라 a가 가리키는 값의 타입

# a = "test"
# print(a,type(a))

# a = 4.5
# print(a,type(a))

name = input("당신의 이름은? ")
address = input("주소는? ")
#python의 경우에 문자열 + 연산은 문자열 끼리만 가능하다
print( name + " 님의 주소는 " + address + " 입니다")