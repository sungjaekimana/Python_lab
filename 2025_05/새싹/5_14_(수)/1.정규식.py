#정규식 - 주민번호
data = """
park 800905-1049118 park@hanmail.com
kim  700905-1059119 kim@naver.com
Life is egg
kim 700906 - 1059118 kim9999@naver.com
"""

result = [] #결과를 담을 빈 리스트 행성

for line in data.split("\n"): 
    word_result = [] 
    for word in line.split(" "):
        print(word)
        #len(word) - 문자열의 길이가 14자
        #앞의 6자리가 숫자여야 한다. word[0:6] 0~5번방까지 전체 숫자로만 구성되어 있냐
        #뒤의 7자리가 숫자여야 한다. word[7:] 7번부터 마지막까지 전체 숫자로만 구성되어 있냐
        #word[6] == "-" 조건을 추가할수도 있다.
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            #주민번호 패턴이 맞다면
            #앞자리 6자리 + "-" + "*******"
            word = word[:6] + "-" + "*******" 
        word_result.append(word) #같은 라인에 여러개의 주민 번호가 있을 수 있음.
    result.append(" ".join(word_result))  #같은 라인 주민번호를 공백으로 연결시켜 리스트에 더함.
print("\n".join(result))

import re

pat = re.compile("(\d{6})[-]\d{7}") # \d{6} 숫자여섯자리, [-], \d{7} 숫자7자리 
print(pat.sub("\g<1>-*******", data))