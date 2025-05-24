# 과제
# 문제5 문자열 연습하기

#5-1 변수에 값 "홍길동,임꺽정,장길산,최영,윤관,강감찬,서희,이순신,남이"
names = "홍길동,임꺽정,장길산,최영,윤관,강감찬,서희,이순신,남이"
print(names,type(names))

#5-2 => list타입으로 전환하기
nameList = names.split(",") #전달된 값으로 문자열을 쪼개서 list타입으로 반환한다.
print(nameList, len(nameList)) #list, 배열의 길이

#5-3 => "서희"가 몇번째에 있는지
print("서희의 위치는", nameList.index("서희"), "입니다")


#5-4 "이순신", "장영실" 존재여부 확인
if nameList.count("이순신") >0: #if 조건식의 결과가 0이 아닌 모든것 True, 나머지 False
    print("이순신이 존재한다")
else:
    print("이순신이 존재하지 않는다.")
    
if nameList.count("장영실") >0:
    print("장영실이 존재한다")
else:
    print("장영실이 존재하지 않는다.")
    
#5-5 추가할 사람 : "정도전", "정약용" "최치원"....
nameList.append("정도전")
nameList.append("정약용")
nameList.append("최치원") #또는 nameList.extend(["정도전","정약용","최치원원"])

#5-6 "서희" => "김종서"로 바꾸기
pos = nameList.index("서희")
nameList[pos] = "김종서"

#5-7 장길산 => 김길산으로 첫글자만 바꾸기
pos = nameList.index("장길산")
nameList[pos] = (nameList[pos].replace("장","김"))
print(nameList)
