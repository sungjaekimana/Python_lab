f = open("새파일.txt", "w") #open("만들파일명", "파일열기모드")
f.close() #close()를 통해 파일 생성

# r : 읽기모드
# w : 쓰기모드
# a : 추가모드 : 파일의 마지막에 새로운 내용을 추가할 때 사용한다.

f = open("doit/새파일.txt", "w") #doit/을 통해 경로를 지정
f.close()

f = open("새파일.txt", "w") #새파일.txt라는 쓰기전용 파일 생성
for i in range(1,11):
        data = "%d번째 줄입니다\n" % i
        f.write(data)
f.close()
"""
새파일.txt에 다음과 같이 저장된다.
1번째 줄입니다.
2번째 줄입니다.
.
.
.
.
.
10번째 줄입니다.
"""
#한글이 안깨지게 하려면 encoding = "UTF-8"을 추가한다.
f = open("doit/새파일.txt", "w", encoding = "UTF-8") 
f.close()

f = open("새파일.txt", "w")
for i in range(1,11):
        data = "%d번째 줄입니다\n" % i
        f.write(data)
f.close()

# readline() 사용
f = open("새파일.txt", "r")
line = f.readline()
print(line)
f.close()
#결과 : 1번째 줄입니다.

# readline_all.py
f = open("C:/doit/새파일.txt", 'r')
while True:
    line = f.readline() #f.readline()을 통해 while이 끝날때까지 line에 넣고
    if not line: # 다음문장이 없어 빈문자열이 나와 False가 된다. False의 not = True
        break
    print(line) #line을 출력한다.
f.close()
"""
새파일.txt에 다음과 같이 저장된다.
1번째 줄입니다.

2번째 줄입니다.

.

.

10번째 줄입니다.
"""
while True:
    data = input()
    if not data: #True인데 not을 만나 False가 된다.
        break
    print(data)

# readlines.py
f = open("C:/doit/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    # line = line.strip() #줄 끝의 줄 바꿈 문자르 제거한다.
    # line = line.replace("n","") #줄 끝의 줄 바꿈 문자르 제거한다.
    print(line)
f.close()

# read.py : 통째로 출력하기
f = open("C:/doit/새파일.txt", 'r')
data = f.read()
print(data)
f.close()

# read_for.py : readlines()를 한 것 같은 효과
f = open("C:/doit/새파일.txt", 'r')
for line in f:
    print(line)
f.close()

# add_data.py : a - 추가모드 : 파일의 마지막에 새로운 내용을 추가할 때 사용한다.
f = open("C:/doit/새파일.txt",'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# with문과 함께 사용하기
f = open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()

# file_with.py : f를 지역변수로 만든다.
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")
    
# sys1.py : sys모듈 활용하기
import sys

args = sys.argv[1:] 
for i in args:
    print(i)
