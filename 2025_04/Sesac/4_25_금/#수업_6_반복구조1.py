#반복문
#for문 : 정해진 횟수만큼 반복한다.
#while문 : 반복을 하긴 하는데 몇번할지 모른다. , 특정조건을 만족할 때만 반복하며 한번도 수행을 안할수도 있다.

for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)

#range(시작,종료,증감치) : 시작값부터 시작해서 종료값-1까지 증감치를 가지고 생성해낸다.
print(range(1,11))
for i in range(1,11):
    print(i)    
    
a = list(range(1,11))
print(a)

for i in range(2,100,2):
    print(i,end = " ")
print()

for i in range(100,1,-2):
    print(i,end = " ")
print()

#문제1. 1 2 3 4 5 6 7 8 9 10
#       11 12 13 14 15 16 17
for i in range(1,101,1):
    print(i, end = "")
    if i%10 == 0:
        print()
        
#문자의 unicode -> ord
print(ord("A")) #65
print(ord("B")) #66
print(ord("a")) #97
print(ord("0")) #48
print(ord("1")) 
#코드값 => 문자로 chr(코드값)
print(chr(49))
print(chr(65))

#for문을 써서 알파벳 A~Z까지 출력하기
for i in range(ord("A"), ord("Z")+1):
    print(chr(i), end="")
    
#키보드로부터 문장을 입력받아서 각 문자의 개수(대소문자 구분하지 않고)
# A ===> 5
# B ===> 0

sentence = input("문장을 입력하세요")
for i in sentence:
    if ord(i)