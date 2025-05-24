#컴퓨터는 시간을 1970년 1월 1일을 기산점을 초당 1씩 카운드

import datetime
day1 = datetime.date(2021, 12, 14)
day2 = datetime.date(2023, 4, 5)
print(day1)
print(day2)
day3 = day2 - day1 #timedelta 객체로 바뀌고 날짜를 갖고 있다.
print(day3.days)

#말일까지 얼마나 남았는가?
day1 = datetime.date(2025, 5, 13)
day2 = datetime.date(2025, 5, 31)
print((day2-day1).days)

import calendar
from datetime import date
#오늘 날짜를 구한다.
today = date.today()
year = today.year
month = today.month
#tuple #해당월의 첫째날과 마지막날
last_day = calendar.monthrange(year,month)[1]
print(last_day)

day1 = datetime.date(year, month, last_day)
print((day1 - today).days)

#오늘은 무슨 요일인지
print(today.weekday()) #0이 월요일, 1이 화요일 ... 등

#문제 : 날짜를 입력받아서 그날이 무슨 요일인지를 반환
#김성재풀이
day = datetime.date(2025, 5, 11) #입력 : 날짜 : "2025-05-11"
day_yoil = day.weekday()

if day_yoil == 0: #계산 : 요일(숫자) -> 요일(문자)로 변환
    print("월")
elif day_yoil == 1:
    print("화")
elif day_yoil == 2:
    print("수")
elif day_yoil == 3:
    print("목")
elif day_yoil == 4:
    print("금")
elif day_yoil == 5:     
    print("토")
elif day_yoil == 6:
    print("일")
else:
    print("뭘까?")
    
#백현숙강사님 풀이 / 배열을 활용해서 풀어야하는데 나는 if문만 주구장창 돌렸다.
day1 = datetime.datetime.strptime("2025-05-11", "%Y-%m-%d")
print(day1.weekday())

def getWeekday(s):
    day1 = datetime.datetime.strptime(s, "%Y-%m-%d")
    weekday = day1.weekday()
    titles = ["월요일","화요일","수요일","목요일","금요일","토요일","일요일"]
    return titles[weekday]

print(getWeekday("2025-04-11"))

# #딥러닝때 shutil 사용함.
# shutil_copy.py
import shutil
shutil.copy("c:/doit/a.txt", "c:/temp/a.txt.bak")

#glob 모듈은 디렉터리 안의 파일들을 읽어서 리턴한다.
import glob 
glob.glob("c:/doit/mark*") #?는 1자리 문자열, *은 임의의 길이의 문자열을 의미한다.
['c:/doit\\marks1.py', 'c:/doit\\marks2.py', 'c:/doit\\marks3.py']

import os
print(os.environ) #os.environ은 현재 시스템의 환경 변숫값을 리턴.
print(os.environ["PATH"]) #PATH만 따로 부르는 법

print(os.getcwd()) #현재 자신의 디렉터리 위치를 리턴

#파이썬에서 os명령어를 쓰고 싶을 때는 아래와 같이 작성한다.
os.system("dir/w")