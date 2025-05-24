#가변매개변수 -> 함수는 매개변수 개수가 바뀌는 경우에
print(3,4,5,6,7)
print(1,2,3)

#가변매개변수 - 매개변수의 개수가 바뀐다.
#매개 변수 앞에 *을 붙인다.
#매개 변수에 기본값을 줄때는 변수 자체가 여러개 만들어진다.

def myadd(*args): #변수하나에 값을 여러개 전달한다.
    print(type(args))
    for a in args:
        print(a)

myadd(1,2)
myadd(1,2)

def myadd2(*data):
    s = 0
    for i in data:
        s += i
        return s

print(myadd2(1,3,5))
print(myadd2(1,3,5,7,9))
print(myadd2(1,3,5,7,10,12,13))

#일반인자와 tuple인자를 같이 써야 할때는 일반 인자가 먼저 와야 한다.
#나머지를 tuple로 받으니까

def myadd3(n,*data):
    print("n",n)
    for i in data:
        print(i)
        
myadd3(1,2,3,4,5)

#dict타입을 매개변수로 넘길 수도 있다. **
#매개변수 전달 방식이 달라진다.
def myfunc(d):
    print(d)
    
person = {"name":"홍길동", "age":12}
myfunc(person)

def myfunc2(**d):
    print(d)
    
myfunc2(name = "홍길동", age = 23)

def pickup_even(numList):
    even = []
    for n in numList:
        if n % 2 == 0:
            even.append(numList)
    return even
        
            
pickup_even([3, 4, 5, 6, 7, 8])
#일반인자랑 tuple인자랑 dict인자 셋 다 쓰고 싶으면 순서가 있다.
#순서 : 일반인자, tuple인자, dict인자


#일반인자, tuple타입, dict타입입
def profile(role, *skills, **details):
    print("Role",role)
    print("Skills",skills)
    print("details",details)
    
profile("programmer","python", "react", "deeplearnin",
        yearpay = 100000000, position = "개발자:")