def toDouble(x): #x라는 매개변수를 이용해서 a의 값을 전달함.
    x = x * 2 #x는 값이 2배가 됨.
    
a = 10 #a라는 변수와 함수의 매개변수인 x는 서로 다른 공간입니다.
toDouble(a) #x라는 변수에 값을 복사해가고, 함수를 수행하면서 복사된 x값은 수정된다. 그러나 a와는 관계가 없다.
print(a)    #call by value 함수를 값 복사로 호출한다.
            #dick 타입이나 list타입의 경우에는 함수내부에서 값 변환이 가능함.
            #함수에 dict나 list는 주소를 전달하는 방식이다.
            
def toDouble2(mydic):
    mydic["x"] *=2
    mydic["y"] *=2
    
mydic = {"x":1, "y":1}
toDouble2(mydic)
print(mydic)

#파이썬의 경우는 오버로딩을 지원하지 않음.
#오버로딩은 동일한 이름의 함수를 여러개를 만드는 것이다.
#변수에 타입이 없다. 그냥 막 쓰니까 매개변수의 개수나 타입으로 호출할 함수가 뭔지를 알 길이 없다.
#대신 매개변수에 기본값을 줄 수 있다. 그래서 마치 오버로딩같은 효과를 가져올 수 있다.

def myadd(x=0,y=0,z=0):
    return x+y+z

result = myadd(1,2,3)
print(result)

result = myadd()
print(result)

result = myadd()
print(result)
print(myadd())
print(myadd(1))
print(myadd(1,2))
print(myadd(1,2,3))

#모든 매개변수에 기본값을 줘야 하는 것은 아니고, 기본값을 주기 시작했으면 나머지 매개변수도 다 줘야 한다.
def myfunction(a,b,c = 0, d=0, e=0):
    print(f"a={a} b={b} c={c} d={d} e={e}")
    return a+b+c+d+e

print(myfunction(4,5))

def Sigma(limit=10):
    s = 0
    for i in range(1,limit+1):
        s += i
    return s

print(Sigma())
print(Sigma(5))
print(Sigma(100))