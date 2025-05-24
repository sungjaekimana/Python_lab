#튜플은 다른언어에 아직 없는 타입이었는데 최근에 추가되고 있다.
#튜플 => 우리가 점심 때 플리마켓에 놀러갔다. 이것저것 사다가 손에 다 못들면 비닐봉지 하나 얻어서 비닐봉지에 담는다.
#괄호를 사용한다. "인덱싱과 슬라이싱"을 지원한다. 그러나 "인덱싱이나 슬라이싱"을 통한 업데이트 불가
#read only list형, 속도가 빠르다. 값 변경불가
#"이름 %s 나이 %d" % ("홍길동", 45)

a = (1,2,3,4,5)
print(a,type(a))

a = 5
b = 7
c = 9

a,b,c = 5,7,9 #tuple 활용
print(a,b,c)

#함수 -> 코드를 묶어놓은 것, 함수는 값을 하나만 반환해야 한다.
#파이썬의 경우에는 우리가 여러개를 반환하면 알아서 tuple로 묶어서 하나로 보내준다.
def myfunc1():
    return 3,4
a = myfunc1()
print(type(a))

b,c = a
print(b,c)


a = 5
b = 7
#두개의 변수값을 서로 exchange, swap
c = a
a = b
b = c
print("A =",a, "B =",b)

b, a = a, b #tuple을 써서 값을 swap 할 수 있다.
print("A =",a, "B =",b)

#tuple은 read only이다. 삭제, 업데이트 안된다.
a = (1,2,3,4,5,6,7,8,9)
print(a[0])
print(a[1])
print(a[2])

# del a[2] #삭제 불가
# a[0] = 11 #업데이트 불가

print(a[:5])
print(a[2:5])
print(a[::-1])

b = a + a
print(b)

b = a * 3
print(b)

