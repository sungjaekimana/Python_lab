#escape 문자 - \n(줄바꿈), \t(탭키 작동)
s = "I like star.\nred star.\nblue star."
print(s)

s = "apple\tpear\tcherry\tbanana"
print(s)

#escape 기능을 무력화 하고자 한다. 1)\\ 2)r문자열 : 문자열 앞에 r을 붙인다.

s = "c:\\test\\temp"
print(s)

s = r"c:\test\temp"
print(s)

#문장안에 ' 나 " 가 있을 때 처리방식
s = "'I like \ 'stepany\'"

s = "I like \"stepany\""
print(s)

#다른언어의 경우는 문자는 '' 문자열은 ""
#때로는 \를 직접 출력해야 하는 경우가 있다.
s = "역슬래시(\\)는 특별한 기능을 갖는 문자이다."
print(s)

#print 사용방법
print("red", "green", "blue")
print("yellow", "cyan", "magent", sep=",")
print("red", "green", "blue", sep="\t", end="\n")

print("*" * 20)

print("=" * 40)

#문자열 포매팅 - 문자, 숫자 섞어서 문장 만들 때 사용한다.
name = "홍길동"
age = 34.5
height = 185
# %s : string의 약자
# %d : decimmal의 약자
# %f : float의 약자
# %자릿수 형식 : %.출력하려는 자리수
s = "%s의 나이는 %d입니다. 그리고 키는 %.2f 입니다." %(name,age,height)
print(s)

a = 37
print("8진수 %o"%a)
print("16진수 %x"%a)

#퍼센트로 출력하는법
print("16진수 %x%%"%a)

print("%10s %10s"% ("hi","hello")) #10자리를 확보하고 오른쪽부터 채워온다.
print("%-10s %-10s"% ("hi","hello")) #10자리를 확보하고 왼쪽부터 채워온다.

a = 3.41592
print("%f"%a)
print("%.2f"%a)
print("%7.2f"%a)

print("이름 : {0} 나이 : {1}".format(name,age))
print("이름 : {} 나이 : {}".format(name,age))
print("이름 : {name} 나이 : {age}".format(name = "김성재",age = 27))

#f string : 문자열앞에 f를 쓰고 {변수명} : 문자와 숫자를 같이 출력할 때 쓰면 유용하다. 최신식이며 요즘 트렌드이니 꼭 숙지하기!
print(f"이름 : {name} 나이 : {age}") 

#왼쪽, 오른쪽, 가운데 정렬, 공백 채우기
print("{0:<10} {1:<10}".format("hi", "hello"))
print("{0:>10} {1:>10}".format("hi", "hello"))
print("{0:^10} {1:^10}".format("hi", "hello"))
print("{0:=^10} {1:*^10}".format("hi", "hello"))

print("{0:.4f}".format(3.141592))

x = int(input("x = "))
y = int(input("y = "))
print(f"{x} + {y} = {x + y}")


