s = "hobby"
print(s.count("b")) #b가 몇 개 있는가?
print(s.count("h")) #h가 몇 개 있는가?

#문자의 위치 값
print(s.find("b")) #첫번째 문자 위치 값을 반환
print(s.find("k")) #문자가 없으면 -1을 반환

s = "I like star, red star, blue star, I like star."
print(s.count("star"))
print(s.find("star"))

pos1 = s.find("star") #0번째 방부터 찾기
print(pos1)

pos2 = s.find("star, pos1+1")
print(pos2)

pos1 = s.index("like")
print(pos1)

#pos1 = s.index("love") #단어가 없으면 예외가 발생한다. 오류남
#print(pos1)

s = ",".join("abcd")
print(s)

#[] : 리스트 타입임임
#[]에 전달된 단어들을 처음 "," 이 안에 있는 기호로 묶어서 문장으로 만들어주는 역할을을 한다.
s = ",".join(["cherry", "banana", "pear", "grape"])
print(s)
#위와 반대역할 문장을 -> list 타입으로 변환
words = s.split(",") #하나의 문장을 쪼갠다. -> list 타입으로 변환한다.
print(words)

print("hi".upper())
print("HI".lower())

s = "   hi  "
print("*" + s + "*",)
print("*" + s.lstrip() + "*")
print("*" + s.rstrip() + "*")
print("*" + s.strip() + "*")

#True와 False는 무조건 이대로 써야함(대소문자 변경금지)
print("python".isalpha())
print("python1".isalpha())

print("python".isdigit())
print("123".isdigit())

s = "hello" #upper 바뀐 값을 반환, 원래 값은 안바뀜
print(s.upper(), s)
s = s.upper()
print(s)