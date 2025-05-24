# def 함수_이름(매개변수): cf.매개변수 : 값을 입력받는 변수, 함수에서 정의되어 사용되는 변수수

def add(a,b): #a,b라는 두개의 매개변수
     return a + b # 출력값
print(add(1,2)) #함수를 실행
# 위 함수의 이름은 add이고 두개의 매개변수를 입력받아서 a+b의 값을 출력한다.

a = 3
b = 4
c = add(a,b)

print(c)

#입력값이 없는 함수
def say():
     return "Hi"

a = say()
print(a)

#리턴값이 없는 함수
def add(a, b): 
     print("%d, %d의 합은 %d입니다." % (a, b, a+b)) #print값이 출력된다.
     
a = add(1,2)

print(a) #함수에 return값이 없기 때문에 None을 출력한다.

def say():
     print("Hi") #print값이 출력된다.
     
a = say()
print(a) # 함수에 return값이 없기 때문에 None을 출력한다.

#매개변수를 지정하여 호출하기
def sub(a,b):
     return a - b

a = sub(3,1)
print(a) #2가 출력된다.

def sub(a,b):
     return a - b

result = sub(a=7, b=3) #a에 7, b에 3을 전달
print(result) #4가 출력된다.

#입력값이 몇 개가 될지 모를 때는 어떻게 하는가?
def add_many(*args): #여러개의 argument(변수)를 받는다.
     result = 0
     for i in args: 
          result = result + i   # *args에 입력받은 모든 값을 더한다.
     return result 

print(add_many(1,2,3,4)) #args 값을 출력할 때 다양하게 지정할 수 있다.
print(add_many(1,2,3,4,5)) #args 값을 출력할 때 다양하게 지정할 수 있다.


def add_mul(choice, *args): 
     if choice == "add":   # 매개변수 choice에 "add"를 입력받았을 때
          result = 0 
          for i in args: 
               result = result + i 
     elif choice == "mul":   # 매개변수 choice에 "mul"을 입력받았을 때
          result = 1
          for i in args: 
               result = result * i 
     return result

print(add_mul("add",1,2,4,4))
print(add_mul("mul",1,2,4,4))

#키워드 매개변수 kwargs
def print_kwargs(**kwargs):
     print(kwargs)
     #print(kwargs["a"]) a만 출력
     #print(kwargs["b"]) b만 출력
print_kwargs(a=1,b=2)

#함수의 출력값은 하나(return값은 하나)이다.
def add_and_mul(a,b):
     return a+b, a*b

print(add_and_mul(3,4)) # tuple 형식으로 출력

#함수는 return문을 만나는 순간 결괏값을 돌려준 다음 함수를 빠져나간다.
def say_nick(nick):
     if nick == "바보": 
          return 
     print("나의 별명은 %s 입니다." % nick)
     
say_nick("맛스타님")
say_nick("조코딩님")
say_nick("바보") # 함수를 빠져나가는 용도로 사용

#매개변수에 초기값 미리 설정하기
def say_myself(name, old , man = True):
     print("나의 이름은 %s 입니다." %name)
     print("나이는 %d살입니다." %old)
     if man:
          print("남자입니다.")
     else:
          print("여자입니다.")
          
say_myself("장예은", 26, False)

#기본값이 지정된 매개변수는 제일 마지막에 적는다.
def say_myself(name, old, man = True):
     print("나의 이름은 %s 입니다." %name)
     print("나이는 %d살입니다." %old)
     if man:
          print("남자입니다.")
     else:
          print("여자입니다.")
          
say_myself("이빠진퍄노", 20, False)

#함수 안에서 선언한 변수의 효력 범위
a = 1 #합수 밖에 들어있는 변수는 전역변수
def vartest(a): 
     a = a + 1 #함수안에 들어있는 변수는 지역변수, 함수가 끝나면 없어진다.
     
vartest(a)
print(a)

def vartest(hello):
     hello = hello + 1

#함수안에서 함수 밖의 변수를 변경하는 방법
a = 1
def vartest(a):
     a = a + 1
     return a

a = vartest(a)
print(a)

a = [1,2,3,4]











