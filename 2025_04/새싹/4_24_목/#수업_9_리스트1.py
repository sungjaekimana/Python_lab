#성적처리 3명이면 name1, name2, name3
#list 타입이면 -> 배열
words = ["red", "green", "blue"] #list타입, 인덱싱과 슬라이싱을 지원한다.
print(words[0]) #indexing
print(words[1])
print(words[2])
print(words) #한번에 출력 가능

#새로운 단어 추가하기 : append
words.append("black")
words.append("cyan")
print(words)
print("내가 찾는 단어 개수", len(words))
print("내가 찾는 단어 개수", words.count("red"))

#단어 위치 찾기 : index
if words.count("yellow") :
    print("단어 위치 찾기", words.index("yellow"))
else:
    print("yellow는 없다")

#in연산자 "내용" in list타입 있으면 True 없으면 False를 반환한다.
if "yellow" in words:
    print("yellow 위치", words.index("yellow"))
else :
    print("yellow는 없다.")

#인덱싱 - list타입의 경우에는 인덱싱을 통해 값 변경가능, 문자열은 인덱싱을 통한 값 변경 불가
words[0] = "white"
print(words)


#extend 함수 : 리스트와 리스트를 합친다.
words.extend(["brown", "violet", "purple", "magenta"])
print(words)

#list -> str로 변경할 때 join을 사용한다.
s = ",".join(words)
print(s)

#str -> list로 변경할 때 split을 사용한다.
words2 = s.split(",")
print(words2)

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[0])
print(numbers[0::2])
print(numbers[::-1])
print(numbers[1::2])

#리스트 만들기
names = []
names.append("홍길동")
names.append("임꺽정")
names.append("장길산")
names.append("홍경래")
print(names)

names = list()
names.append("모란")
names.append("작약")
names.append("불두화")
names.append("목련")
print(names)


