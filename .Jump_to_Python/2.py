#숫자형
a = 123
print(a)

a = 123
print(type(a))

a = 1.2
print(type(a))

a = 4.24E10
print((a))

a = 4.24E10
print(type(a))

a = 0o10
print(a)

a = 0x10
print(a)

a = 0x8bb
print(a)

a = 3
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b) #몫을 구하려면 //
print(a ** b) #a의 b제곱
print(a % b) #나머지를 구하려면 %

#문자열
a = "Life is too short, You need Python"
b = "a"
c = "123"
print(type(a)) # a의 문자열을 확인
print(type(c)) # b의 문자열을 확인

a = "Life' is too short, You need Python"
print(a)

a = "Life \" is too short, You need Python" #\를 통해 따옴표 보존
print(a)

a = 'i\'m hungry'
print(a)

a = "Life is too short, \nYou need Python" #이스케이프 코드 \n, """~""": 줄바꿈
b = """Life is too short,
You need Python"""
print(a)
print(b)

a = "Life is too short, \tYou need Python" #이스케이프 코드 \t : 탭만큼 간격 띄우기
print(a)

head = "Python"
tail = " is fun!"
a = (head + tail)
print(a) #문자열 더해서 연결하기
print(a * 3) #문자열 곱하기(문자열*숫자형만 가능)

print("=" * 50) #문자열 곱하기 응용
print("my program")
print("=" * 50)

a = "Life is too short"
print(len(a)) #len을 통한 a의 길이 구하기

a = "Life is too short, You need Python"
print(a[3]) #a의 3번째 인덱스를 출력, #인덱스는 0번부터 시작, 역순은 -1부터
print(a[0])
print(a[2])
print(a[6])
print(a[-34])

a = "Life is too short, You need Python"
b = a[0] + a[2] + a[5] # 슬라이싱 때 참고 a[시점:종점:간격]
print(b)

a = "20230331Rainy" #슬라이싱으로 날짜와 날씨를 나눔
date = a[0:8]
weather = a[8:]
print(date)
print(weather)

a = "I ate %d apples" %3 #문자열 포매팅 %d을 이용
print(a)

a = "I ate %s apples" %"five" #문자열 포매팅 %s을 이용
print(a)

number = 10
day = "three"
a = "I ate %d apple. so I was sick for %s days." %(number,day)
print(a)

a = "I have %d%% apples" %3 # %를 쓰고 싶으면 %%로 작성
print(a)

a = "%.4f"%3.4213423 #소수점 4째자리까지 출력
print(a)

a = "%10.4f"%3.4213423
print(a)

a = "I eat {0} apples".format("five") #.format을 활용하여 문자열과 숫자열 모두 포매팅 가능
print(a)

a = "I eat {0} apples".format(5) #.format을 활용하여 문자열과 숫자열 모두 포매팅 가능
print(a)

number = 10
day = "three"
a = "I ate {0} apples. so I was sick for {1} days.".format(number,day)
print(a) #숫자를 인덱스에 맞게 적어줘야한다 또는 아래같이 변수의 값을 직접 지정한다다
a = "I ate {number} apples. so I was sick for {day} days.".format(number = 10,day = "three")
print(a)

a = "{0:<10}".format("hi") #10칸을 만들고 왼쪽 정렬
print(a)

a = "{0:>10}".format("hi") #10칸을 만들고 왼쪽 정렬
print(a)

a = "{0:^10}".format("hi") #10칸을 만들고 가운데 정렬
print(a)

a = "{0:*^10}".format("hi") #10칸을 만들고 가운데 정렬, 빈칸은 *로 채움
print(a)

name = "홍길동" # 제일 최신버전이며 문자열 포매팅은 이것만 알아도 괜찮음
age = 30
a = f"나의 이름은 {name} 입니다. 나이는 {age} 입니다."
print(a)

age = 30 #위 문자열 포매팅 응용
a = f"나는 내년에 {age+1}살이 된다."
print(a)

a = f'{"hi":<10}' #f'의 정렬은 이런식으로 함
print(a)

y = 3.42134234 #f'의 소수점 표현현
a = f'{y:.4f}'
print(a)

a = "hobby" #문자열 개수 세기
print(a.count("b"))

a = "hobby" #인덱스 찾기, 없을 시 -1이 나옴
print(a.find("b"))
# a = "hobby"
# print(a.index("x")) #인덱스 찾기, 없을 시 ValueError

a = ",".join("abcd")
print(a)

a = "hi" #a.upper() - 대문자로 변경, .lower() - 소문자로 변경
print(a.upper())

a = " hi " #a.lstrip() - 왼쪽 공백을 제거, .rstrip - 오른쪽 공백을 제거
print(a.lstrip())

a = "Life is too short" #.replace("1","2") - 1을 2로 변경
print(a.replace("Life", "Your leg"))

a = "Life is too short" #.split() - 띄어쓰기를 기준으로 리스트로 변경
print(a.split()) 

a = "a:b:c:d" #a.split(":") - :를 기준으로 리스트로 변경
print(a.split(":"))

#리스트 - 여러가지 변수에 담을 값이 있을 때 각각 담는것이 아닌 하나의 변수에 담음

odd = [1,3,5,7,9]
print(type(odd))

e = [1, 2, "life", "is"] #파이썬에서는 문자와 숫자 상관없이 리스트로 묶을 수 있음

a = [1, 2, 3] #리스트 a에서 1번 인덱스를 출력하라
print(a[1])
print(a[-1])

a = [1, 2, 3, ["a", "b", "c"]] #안에 대괄호는 하나의 인덱스로 설정됨
print(a[3][2])

a = [1, 2, 3, 4, 5] #리스트의 슬라이싱, 스트링과 같다
print(a[::2])

a = [1, 2, 3] 
b = [4, 5, 6]
print(a + b) #리스트의 더하기
print(a * 2) #리스트의 곱하기
print(len(a)) #리스트의 길이
print(str(a[2]) + "hi") #리스트를 문자열로 바꿔서 문자열과 더하기, 파이썬에서는 같은 형태의 자료형끼리만 연산이 가능함

a = [1, 2, 3]
a[2] = 4 #a의 2번 인덱스 값을 4로 바꿈
print(a)

a = [1, 2, 3]
del a[1] #a의 1번 인덱스 값을 제거함
print(a)

a = [1, 2, 3, 4, 5]
del a[2:] #a의 2번 인덱스 값부터 끝까지 제거함
print(a)

a = [1, 2, 3]
a.append(4) #a에 4를 추가함
print(a)

a = [1, 4, 3]
a.sort() #a를 오름차순으로 정렬함
print(a)

b = ["a", "c", "b"]
b.sort()
print(b)

a = ["a", "c", "b"]
a.reverse() #a의 순서를 거꾸로 뒤집음음
print(a)

a = ["a", "c", "b"]
a.sort() #a를 오름차순으로 정렬하고
a.reverse() #내림차순으로 정렬함
print(a)

a = [1, 2, 3]
print(a.index(2)) #.index(n) - n번째 인덱스의 값을 찾음

a = [1, 2, 3]
a.insert(0, 3) #.insert(n,m) - n번째 인덱스 위치에 m값을 추가함
print(a)

a = [1, 2, 3, 1, 2, 3]
a.remove(3) #.remove(n) - 앞쪽인 인덱스의 n값을 지움
print(a)

a = [1, 2, 3]
a.pop() #.pop(n) - 리스트의 n번째 요소를 뱉어내고 그 요소는 삭제함, 괄호 비어있으면 제일 마지막 요소에 적용
print(a)

a = [1, 2, 3, 1]
print(a.count(1)) #.count(n) - n이 몇개 있는지 셈

a = [1, 2, 3]
a.extend([4,5]) #.extend([]) - 이어서 더함
print(a)

#튜플 : 값의 변경이 불가능하다. 변경이 안되는 리스트
#리스트는 대괄호, 튜플은 소괄호로 만든다.
#하나의 요소를 넣을 때는 쉼표(,) 반드시 넣어야 한다.
t1 = (1,2,3)
print(type(t1))

# t1 = (1,2,"a","b")
# del t1[1] TypeError: 'tuple' object doesn't support item deletion

t1 = (1,2,"a","b")
print(t1[0]) #튜플도 인덱싱이 가능함.

t1 = (1,2,"a","b")
print(t1[1:]) #튜플도 슬라이싱이 가능함. 그러나 실제 값이 바뀌는 것은 아님.

t1 = (1,2,"a","b")
t2 = (3,4)
t3 = t1 + t2 #t3라는 새로운 튜플을 만들어서 출력. t1,t2는 변형되지 않음.
print(t3)

t2 = (3,4)
t3 = t2 * 3 #곱셈도 가능함.
print(t3)

t1 = (1,2,"a","b")
print(len(t1))
#튜플은 sort, insert, remove, pop은 사용 불가함.

#딕셔너리 - key:value로 이루어진 형태, 중괄호를 사용

dic = { "name":"pey", "phone":"010-2400-3187", "birth":"0120"}
# value에 리스트를 넣을 수도 있음

a = {1:"a"}
a[2] = "b" #딕셔너리에 값을 추가함.
print(a)

del a[1] #딕셔너리는 삭제할 키값을 적어서 삭제가능.
print(a)

grade = {'pey': 10, 'julliet': 99}
print(grade["pey"]) #key를 통해서 value 값을 찾을 수 있음.
print(grade["julliet"])

dic = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}

print(dic["name"])
print(dic["phone"])
print(dic["birth"])

#딕셔너리에서 키는 중복되면 안됨, 키가 변형되도 안됨.

a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
print(a.keys()) #딕셔너리의 key값을 리스트로 변경
print(a.values()) #딕셔너리의 key값을 리스트로 변경
print(a.items()) #딕셔너리의 key:vale값을 리스트로 변경

a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
a.clear() #값을 싹 다 날림.
print(a)

a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
print(a.get("name")) #print(a[key값])이랑 같음
print(a.get("sex","값이 없습니다"))































