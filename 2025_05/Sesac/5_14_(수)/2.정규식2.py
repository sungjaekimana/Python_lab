
#예제 - 비
import re
pattern = r"비" #문자열\ : 기본적으로 escape로 사용한다.
                #하지만 패턴에서는 \의 escape기능을 무력화 해야한다.
                #꼭 패턴 문자열앞에 r을 붙여야한다.
text = "하늘에 비가 오고 있습니다. 어제도 비가 왔고 오늘도 비가 오고 있습니다."

regex = re.compile(pattern)
result = regex.findall(text) #비가 몇번들어갔는지 확인
print(result)

# 예제 - 우편번호
import re
zipcode = input("우편번호를 입력하세요 : ")
pattern = r"\d{5}$" #5자리로 끝나는 정수
regex = re.compile(pattern) #match 시작단어에 매칭하는 값이 있어야한다.
result = regex.match(zipcode) #일치안하면 None반환 일치하면 match 객체 반환
if result != None: # 결과값이 None이 아니다 = 일치한다.
    print("형식이 일치합니다.")
else:
    print("잘못된 형식입니다.")
    
    
# 예제 - star - match()

import re

text1 = "I like star"
text2 = "starship is beautiful"

pattern = "star" #정규표현식 패턴으로 "star"를 찾겠다.
print(re.match(pattern,text1)) #"star"로 시작하는가? None
print(re.match(pattern,text2)) #"star"로 시작하는가? match객체가 반환

matchObj = re.match(pattern,text2) #
print(matchObj.group()) #group()은 매칭된 문자열 자체를 반환 : star
print(matchObj.start()) #start()는 매칭된 문자열 인덱스를 반환 : 0
print(matchObj.end()) #end()는 매칭된 문자열의 끝 인덱스를 반환 : 4

# star찾기 - search()
import re
text1 = "I like star, red star, yellow star"
text2 = "star is beautiful"

pattern = "star" # 패턴설정
print(re.search(pattern, text1)) #문자열전체에서 처음 나오는 매칭을 찾는다.
print(re.search(pattern, text2)) #문자열전체에서 처음 나오는 매칭을 찾는다.
                                 #위 print 둘다 객체를 반환
                                 
matchObj = re.search(pattern, text1)  #text1에서 star를 찾고 matchobj에 저장
print(matchObj.group()) #매칭된 실제 문자열 반환
print(matchObj.start()) #매칭된 부분의 시작 인덱스 반환
print(matchObj.end()) #매칭된 부분의 끝 인덱스 반환
print(matchObj.span()) #매칭된 부분의 (시작인덱스, 끝인덱스) 반환(tuple)

matchObj = re.search(pattern, text2)
print(matchObj.group())
print(matchObj.start())
print(matchObj.end())
print(matchObj.span())

# 전화번호만 추출하기 - findall()
import re

text = """
phone : 010-0000-0000 email:test1@nate.com
phone : 010-1111-1111 email:text2@naver.com
phone : 010-2222-2222 email:test3@gmail.com
"""
print() #줄바꿈
print("---전화번호 추출하기---")
phonepattern = r"\d{2,3}-\d{3,4}-\d{4}" #전화번호 패턴
                #숫자 2~3자리 - 숫자 3~4자리 - 숫자 4자리

matchObj = re.findall(phonepattern, text) #text안에서 phone을 찾아 리스트로 반환

for item in matchObj:
    print(item)

print("--- 이메일 추출하기 ---")
emailpattern = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b" #이메일 패턴

matchObj = re.findall(emailpattern, text) #text안에서 email을 찾아 리스트로 반환
for item in matchObj:
    print(item)
print()


# 전화번호 추출하기_finditer

import re

text = """
phone : 010-0000-0000 email:test1@nate.com
phone : 010-1111-1111 email:text2@naver.com
phone : 010-2222-2222 email:test3@gmail.com
"""
print() #줄바꿈
print("---전화번호 추출하기---")
phonepattern = r"\d{2,3}-\d{3,4}-\d{4}" #전화번호 패턴

matchObj = re.finditer(phonepattern, text) #text에서 phone을 찾아 객체로 반환
for item in matchObj:
    print(item.group()) #매칭된 문자열 그대로 반환
    print(item.span()) #매칭된 문자열의 (시작인덱스,종료인덱스) tuple로 반환
print()

import re

pattern = r"^abc" #문자열이 abc로 시작하는 것이 패턴
# Pattern = r"abc$" #문자열이 abc로 끝나는 것이 패턴
text = ["abc", "abcd", "abc15", "dabc","","s"]
repattern = re.compile(pattern)

for item in text:
    result = repattern.search(item) #문자열 전체를 검색해서 처음 일치하는 부분을 찾는다.
    if result:
        print(item, "--O") #검색결과가 있으면 O
    else:
        print(item, "--X") #검색결과가 없으면 X
        
import re
pattern = r"[pP]ython"
text = ["python", "Python", "PYTHON", "12python", "python3"]
repattern = re.compile(pattern) #정규식패턴을 미리 컴파일해서 효율적인 검색가능.

for item in text:
    result = repattern.search(item) #문자열 전체에서 python or Python이 포함됐는지 확인
    if result:
        print(item, "--O")
    else:
        print(item, "--X")

pattern = r"[A-Z]" #알파벳 대문자 하나라도 있는가
text = ["python", "Python", "PYTHON", "korea", "Korea", "KOREA"]
repattern = re.compile(pattern)
for item in text:
    result = repattern.search(item) #문자열 전체에 대문자가 하나라도 있는지
    #match함수는 첫 시작만을 보기 때문에 활용불가
    if result:
        print(item, "--O")
    else:
        print(item, "--X")
        
import re

#그룹핑
contents = """
문의사항이 있으면 010-1234-6789으로 연락주시기 바랍니다.
담당자 02-333-4444
국장 02-333-4445
"""
pattern = r"\b(\d{2,3})-(\d{3,4})-(\d{4})\b"
regex = re.compile(pattern)
result = regex.search(contents)
print()
if result != None:
    phone1 = result.group(1) #010
    phone2 = result.group(2) #1234
    phone3 = result.group(3) #6789
    print(phone1)
    print(phone2)
    print(phone3)
else:
    print("전화번호가 없습니다.")
    
# 사업자번호(연습문제)
# 사업자 번호의 의미 : 000-000-00000
# 앞 3자리 : 관할세무서 번호
# 가운데 자리 : 사업자의 성격을 나타냄(개인사업자 : 90~99)
# 마지막 5자리 : 사업자용 4자리 + 검증용 1자리
# 다음 데이터들로부터 사업자 번호들을 추출하고 그중에 개인면세자에 해당하는 사업자 번호만 출력

import re

content = """
우리커피숍 100-90-12345
영풍문고 101-91-12121
영미청과 102-92-23451
황금코인 103-89-13579
우리문구 104-91-24689
옆집회사 105-82-12345
"""
#문제풀이
pattern = r"\b(\d{3})-(\d{2})-(\d{5})\b"
matchObj = re.finditer(pattern,content)

for item in matchObj:
    print(item, end = "\t")
    if int(item.group(2)) >= 90 and int(item.group(2)) <= 99:
        print("개인면세자 입니다.")
    else:
        print("개인면세자가 아닙니다.")



