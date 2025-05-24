a=10
b=20
print(a+b)

print("Hello")

a = 10
b = 3
print( f"{a} + {b} = {a+b}")
print( f"{a} - {b} = {a-b}")
print( f"{a} * {b} = {a*b}")
print( f"{a} / {b} = {a/b}")
print( f"{a} // {b} = {a//b}")
print( f"{a} % {b} = {a%b}")
print( f"{a} ** {b} = {a**b}")

s ="Life is too short, You need Python"
#파이썬의 문자열은 read only이다.
print(s) #인덱싱과 슬라이싱 - 0부터 시작을 한다
print(s[:4]) #0번부터 1,2,3 까지만 출력, 슬라이싱을 지원 다른언어 substring
print(s[8:11])
print(s[0]) #문자열은 인덱싱은 데이터 수정이 불가능하다.
print(s[1])
s = s.replace("short", "long") #바꾼 데이터를 리턴한다.
print(s)

data = """
홍길동,90,90,80
임꺽정,80,80,80
장길산,100,100,90
"""
lines = data.split("\n")
lines = lines[1:len(lines)-1]
print(lines)

dataList=[]
for line in lines:
    words = line.split(",")
    w = {"name":words[0], "kor":words[1], "eng":words[2], "mat":words[2]}
    dataList.append(w)
    #print(words)

print(dataList)

name="홍길동"
age=23
phone="010-0000-0001"
kor = 90
eng = 90
mat = 80
total = kor+eng+mat
avg = total/3
print("%s %d %s %d %d" % (name, age, phone, kor, eng) )
print("{} {} {} {} {}".format(name, age, phone, kor, eng))
print(f"{name} {age} {phone} {kor} {eng}") #3.6 부터 사용 가능  

#배열 - 프로그램 수행전에 반드시 메모리를 확보해야함
#index를 통해 읽고 쓴다. 수행도중에 크기 변화 불가
#연속된 메모리 공간 => 파이썬의 list 는 배열구조가 아님
#인덱싱과 슬라이싱을 써서 접근한다는 부분만 배열구조와 일치한다.

list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1[0])
print(list1[3])
print(list1[4])
print(list1[:4])
print(list1[2:3])
#list1[1:6]=8
print( list1)
list1.append(11)
list1.append(12)
list1.extend([10,20,30,40])
print(list1)
list1.clear() #전체 삭제
list1.insert(0, 10)
list1.insert(1, 10)

#리스트에 5의 배수를 10개 채우기
a = list(range(5, 5*10+1, 5))
print(a)

#리스트에 100부터 90, 80, 70 ... 역순으로 10까지 채워서 출력하기
a = list(range(100, 0, -10))
print(a)

#중복된 값이 포함된 리스트 a = [1, 2, 3, 2, 4, 3, 5, 1]가 있습니다.
#중복을 제거하고 정렬된 리스트를 출력해 보세요.
a = [1, 2, 3, 2, 4, 3, 5, 1]
b =[]
for i in a:
  if i not in b:
    b.append(i)
print(b)

#scores = [80, 95, 70, 100, 85]
#평균 점수보다 높은 점수만 골라 새로운 리스트로 만들고 출력해 보세요.

#이차원 : 본래의미의 배열이 아니다
#list of list로 표현해야 한다.
a = [ [1,2,3], [4,5,6], [7,8,9]]
for i in a:
  print(i)

print(a[0])
print( a[0][0])

#10 by 10 100개 1~100까지 채워서 출력하기

a = []
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
a.append(6)
a.append(7)
a.append(8)
a.append(9)
a.append(10)  #a.append(i)
print( a)

totalList=[]
for k in range(0,10):
  a = []
  for i in range(k*10+1, (k+1)*10+1):
    a.append(i)
  totalList.append(a)

for i in range(0, 10):
  for j in range(0, 10):
    print("%4d" % totalList[i][j], end="" )
  print()


# 1 0 0  0 0 0 0 0 0 0
# 2 3 0  0 0 0 0 0 0 0
# 4 5 6  0 0 0 0 0 0 0
# 7 8 9 10 0 0 0 0 0 0
#  ...............

totalList=[]
kk=1
for k in range(0,10):
  a = []
  for i in range(0, 10):
    if i < (k+1):
      a.append(kk)
      kk+=1
    else:
      a.append(0)
  totalList.append(a)

for i in range(0, 10):
  for j in range(0, 10):
    print("%4d" % totalList[i][j], end="" )
  print()
  
  #함수, 최대값과 최대값 위치를 반환하는 함수
# a = [5,4,1,7,8,3,6]
# 1. 첫번째 방의 데이터가 젤 크다고 가정을 한다
#   max 라는 변수에 첫번째 방의 데이터를 저장해 놓는다
# 2. 두번째 방의 데이터를 비교해서 두번째 방의 값이 더 크면 값을 max의 값을 변경한다
# 3. 세번째 방의 데이터를 비교해서 두번째 방의 값이 더 크면 값을 max의 값을 변경한다
# ....... 마지막 방까지 가고 나면 max저장된 값이 제일 크다
a = [5,4,1,7,8,3,6]
def getMax(a):
  max = a[0]
  pos = 0
  for i in range(1, len(a)):
    if max < a[i]:
      max = a[i]
      pos = i
  return max, pos
  # 다른언어는 에러발생, 파이썬은 시스템이 알아서 tuple로 만들어서 던진다

m, p = getMax(a)
print(m,p)
max = a[0]
pos = 0
# if max < a[1]:
#   max = a[1]
# if max < a[2]:
#   max = a[2]
for i in range(1, len(a)):
  if max < a[i]:
    max = a[i]
    pos = i
print(max, pos)


def add(x,y,z): #매개변수는 값을 읽어가기 위한 용도이다. 외부로 값전달을 하지 않는다
  print("Call me")
  return x*2, y*2, z*2

a = add(3,4,5)
print( type(a) )
print( a[0] )
print( a[1] )
print( a[2] )
print( add(6,7,8)[0] ) #함수를 호출해서 결과를 변수에 받아 놓고 쓰자
print( add(6,7,8)[1] ) #함수가 3번이나 호출되고 있다
print( add(6,7,8)[2] )

person = dict()
person["name"] = "홍길동"
person["age"] = 23
person["phone"] = "010-0000-0001"
print(person)

person2 = {"name":"장길산", "age":21, "phone":"010-0000-0002"}
print(person2)

for key in person.keys():
  print(key, person[key])

for key in person2.keys():
  print(key, person2[key])

for value in person2.values():
  print(value)

for key,value in person2.items():
  print(key, value)

#index와 key
for i, key in enumerate(person2.keys()):
  print(i, key)

#파이썬의 경우 연산자 중복 기능   s1 == "hello" : 완전히 새로운 데이터타입을 만들
#거나 아니면 우리가 새로운 언어 번역기를 만들때 필요하다 그밖에는 필요없다.
#java의 경우 문자열 비교   s1.equals("hello")

mydic = {}  #mydic = dict()
mydic["color"]="색"
mydic["red"]="빨간색"
mydic["green"]="초록색"
mydic["blue"]="파란색"
mydic["cyan"]="청녹색"
mydic["black"]="검정색"

color = input("알고싶은색 ? ")
if color in mydic.keys():
  print(mydic[color])
else:
  print("없는색")

s1 = set([1,2,3,4,5,3,4])#중복제거를 한다
print(type(s1), s1 )

s2 = list(s1) #형전환
print( type(s2), s2)

s3 = tuple(s1)
print( type(s3), s3)

s2 = set( [3,4,5,6,7,8])

s3 = s1.intersection(s2) #교집합
print( s3 )

s3 = s1.union(s2)  #합집합
print( s3 )

s3 = s1.difference(s2)  #차집합
print( s3 )