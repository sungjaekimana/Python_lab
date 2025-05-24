"""
1세대 - 기계어와 어셈블리어(기계쪽에 가까움) 
2세대 - 고급언어(사람의 말과 유사한), 코볼, 포트란, 범용언어(다목적용 언어를 못만들음)
        코볼 - 데이터 처리 전문(시장은 끝나다), 포트란-과학기술계산용(물리학과, 원자력발전소)
        스파케티 코드 - 대충 의식의 흐름대로 프로그램을 함 
        goto문 - 아무데로나 막 점프한다. 현재는 시스템프로그램 분야 외에는 거의 안쓰는걸로 
3세대 - C, algol, pascal등등 ........... 
       스파게티 코드에 대한 반성, 구조적프로그래밍
       구조적 프로그래밍의 특징 
       1. top - down 설계방식  기본부터-> 아래로 내려가는 방식
       2. 설계라는 개념을 처음 시도를 한다. 
       3. 순서도
       4. 모듈화(함수와 프로시저로 프로그램을 작은 단위로 나누어서 프로그램을 한다 )
       5. 주석을 열심히 ........
       6. 소프트웨어 공학

4세대 - 객체지향프로그래밍, 3세대의 반성 
       1. bottom-up    : 3세대의 경험을 바탕으로 부품화(부품들을 모으면 하나의 제품이 되더라)
       2. 객체지향 
            1)추상화 : 내부의 상세한 내용을 구체적으로 몰라도 사용에 아무 제한사항이 없는  
                      성격을 말함, list타입, tuple타입, dict타입등 
                      사용자는 내부 구조 몰라도 된다. 
                      추상화가 될수록 사용자가 편하다 
            2) 은닉성 : 데이터를 감춘다. 
                      컴퓨터의 case 가 없으면 오염으로 부터 취약하다.
                      데이터를 보호하자. 
                      접근권한을 만들어서 외부로 접근을 막는다. 
                      최근에는 이 성격이 약화되고 있다.
                      특히 파이썬의 경우 전부 사용가능하다.
            3) 상속성 : 코드의 재활용도를 높인다. 프레임워크 
                    코드를 처음부터 짜는게 아니라 이미 만들어놓은 클래스들중에서 
                    유사한거 골라서 상속받아서 만든다.
            4)다형성 : 이름은 같은데 형태가 여러개 
                    overloading(자바), 매개변수기본값(파이썬) 
                    overriding(상속) - 상속받아서 다시 정의할때 


def 함수이름():
    ....
    ....

함수이름 규칙은 변수 규칙과 동일하다. 
  1. 영문자로 시작하고 _  가능 
  2. 대소문자 구분 
  3. 예약어 안됨 
  묵시적
  4. 소문자로 시작한다.
  5. 카멜표기법이나 스네이크표기법을 사용한다.

전역변수 
함수안에서 변수를 사용하면 값을 읽는게 아니고 값을 할당하면, 외부에 있는 전역변수를 가려버린다. 

"""
global_x = 10 #함수외부에 변수를 선언함 
def myfunc1():
    #함수내부에서 변수에 값을 할당하는 순간 별도의 변수가 만들어진다.
    #예외적으로 외부 변수를 같이 사용하고 싶다면 global 을 앞에 붙인다. 
    global global_x
    global_x = 30 #global_x 는 지역변수 
                  #함수 내부에서만 존재하는 변수이다. 
    y = 20
    print( global_x, y) 

global_x=100
myfunc1()
print( global_x) # 30이 출력되길 원함 

#함수의 매개변수 기본값 
##dict로 받을때도 호출하는 방식은 유사하다 

def myfunc2(name="홍길동", age=21, phone="010-0000-0001"):
    print(name)
    print(age)
    print(phone) 
    
myfunc2()
myfunc2("임꺽정", 33)#필드 지정을 안하면 차례대로 값이 부여된다.
myfunc2(name="둘리")
myfunc2(age=23) 
myfunc2(phone="8-4833")
#함수를 동적으로 결정된다. 함수를 미리 만들어놓고 호출하면 정적으로 결정할수있는데 
#실행할때 함수가 결정되는 방식을 동적결정 
#컴파일러 언어들의 경우에는 컴파일 시간과 실행시간으로 나뉜다. 
#컴파일시간에 결정되면 정적할당 실행시간에 결정되면 동적할당이라고 한다 
#자바는 컴파일러임에도 불구하고 동적할당, 파이썬은 모든것이 실행시간에 결정된다. 
# 
# 제너레이터(개념만)- 우리가 막 만들어 써야 하는것은 아니고 용어 자체가 중요함 
# 값을 하나씩 생성해서 순회할 수 있는 함수나 객체, range 나 filter 가 해당된다. 
print(range(1, 6)) #range라는 함수는 for문안에서 호출하면 데이터 한개씩 만들어서 던져준다다
for i in range(1,6):
    print(i) 

#함수안에서 값을 반환하려면 return 과 yield 가 있다. 
#return은 값을 반환하면서 함수를 종료한다 
#yield는 값을 반환하는데 함수를 종료하지 않아요 대기상태 

def myrange(start=1, end=5):
    i=start
    while i<=end:
        yield i #이 구문을 만나는 순간 값을 하나 반환하고 멈춘다.
        i = i + 1

gen = myrange(end=1000) #함수 호출해서 저장해놓고 next를 통해서 호출한다. 
#이때 제너레이터 객체가 따로 만들어진다. 내부적으로 파이썬이 일반함수를 제너레이터 객체로 
#만들어서 객체 참조를 gen한테 전달  myrange(함수)=> 제너레이터로 변환 
#next 나 for문으로 
print( next( gen ))
print( next( gen ))
print( next( gen ))
print( next( gen ))
print( next( gen ))

for i in myrange(1, 10):
    print(i)

"""
1. 데이터가 너무 커서 한번에 생성할 수 없을때 
2. 무한한 작업이 필요할때 
3. 파일을 계속 읽어서 처리하고자 할때때
"""
# 문제 1
# 입력화면 : 1. 원의면적  2. 사각형면적  3.사다리꼴 면적 0. 종료 

def circle():
    radius = int(input("반지름을 입력하세요 : "))
    circle_area = radius * radius * 3.14
    print(f"\n원의 넓이는 {circle_area} 입니다.\n")

def square():
    width = int(input("가로를 입력하세요 : "))
    length = int(input("세로를 입력하세요 : "))
    square_area = width * length
    print(f"\n사각형의 넓이는 {square_area} 입니다.\n")

def trapezoid():
    upper = int(input("윗변을 입력하세요 : "))
    lower = int(input("아랫변을 입력하세요 : "))
    height = int(input("높이를 입력하세요 : "))
    trapezoid_area = (upper+lower) * height / 2
    print(f"\n사다리꼴의 넓이는 {trapezoid_area} 입니다.\n")
        
def main():
    while True:
            print("1.원의 면적", end = "\t")
            print("2.사각형 면적", end = "\t")
            print("3.사다리꼴 면적", end = "\t")
            print("0.종료")
            choice = int(input("0~3 중 선택하세요 : "))
            if choice == 1:
                circle()
            elif choice == 2:
                square()
            elif choice == 3:
                trapezoid()
            elif choice == 0:
                print("프로그램을 종료합니다.")
                return
            else:
                print("\n잘 고르자. 0~3 사이인데 그걸 못고르냐 친구야")
                print("기회 함 더줄테니까 잘 적자잉\n")
            
# main()

def main2():
    myfunctions = {"1":circle, "2":square, "3":trapezoid} #위에 문제를 dict를 활용해서 풀기
    while True:
            print("1.원의 면적", end = "\t")
            print("2.사각형 면적", end = "\t")
            print("3.사다리꼴 면적", end = "\t")
            print("0.종료")
            choice = (input("0~3 중 선택하세요 : "))
            if choice in myfunctions.keys():
                myfunctions[choice]()
            else:
                return print("프로그램을 종료합니다.")
            
            
# main2()

# 문제 2. 리스트를 받아가서 리스트안에 중복된 데이터를 제거하고 중복되지 않은 데이터 리스트만 반환하기

# 김성재풀이
def append(): #리스트입력
    list1 = []
    while True:
        s = input("입력하세요(중지하려면 '끝' 입력) : ")
        if s == "끝":
            break
        list1.append(s)
    return list1

def remove(list1): #중복제거
    removelist = list(set(list1))
    return removelist

def main():
    data = []
    while True:
        print("1. 리스트 입력")
        print("2. 중복값 제거한 리스트 반환 ")
        print("3. 종료")
        sel = int(input("1 ~ 3중에 선택하세요 : "))
        if sel == 1:
            data = append()
            print(f"\n원본데이터는 {data}입니다.\n")
        elif sel == 2:
            result = remove(data)
            print(f"\n중복제거한 리스트는 {result}입니다.\n")
        elif sel == 3:
            return print("\n프로그램을 종료합니다.")
            
main()

# 백현숙강사님 풀이

def duplicate_remove(aList):
    temp = []
    for i in aList:
        if i not in temp: #temp안에 존재안할때
            temp.append(i)
    return temp

a = [4,3,5,8,1,2,56,4,1,2,8]
b = duplicate_remove(a)
print(b)


# 문제 3. myint 함수 : 문자열을 받아가서 정수로 바꾸어서 반환하기. cf. "123"을 넣었을 경우는 123을 반환하고 "123A'등 잘못된 입력은 같은 경우는 -1 반환
def myint(s):
    sum = 0
    for c in s:
        if ord(c) < ord("0") or ord(c) > ord("9"):
            return -1
        sum = sum * 10 + ord(c) - ord("0")
    return sum

print(myint("123") + myint("345"))

# 문제 4. 문장을 받아가서 문자열 뒤집어서 보내는 함수 reverse

def reverse(): # 김성재 풀이
    sen = input("문장을 입력하세요 : ")
    result = sen[::-1]
    print(result)

reverse()

def reverse(s): # 백현숙 강사님 풀이
    result = ""
    for i in range(len(s)-1, -1, -1):
        result += s[i]
    return result