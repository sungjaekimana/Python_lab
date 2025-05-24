# 과제
# 문제5 문자열 연습하기
#5-1 변수에 값 "홍길동,임꺽정,장길산,최영,윤관,강감찬,서희,이순신,남이"
names = ("홍길동,임꺽정,장길산,최영,윤관,강감찬,서희,이순신,남이")

#5-2 => list타입으로 전환해서
name_list = names.split(",")
print(name_list)

#5-3 => "서희"가 몇번째에 있는지
print(name_list.index("서희"),"번째에 있습니다.")

#5-4 "이순신", "장영실" 존재여부 확인
if "이순신" in name_list:
    print("이순신이 있습니다.")
else:
    print("이순신이 없습니다.")
    
if "장영실" in name_list:
    print("장영실이 있습니다.")
else:
    print("장영실이 없습니다.")
    
#5-5 추가할 사람 : "정도전", "정약용" "최치원"....
name_list.append("정도전")
name_list.append("정약용")
name_list.append("최치원")
print(name_list)

#5-6 "서희" => "김종서"로 바꾸기
name_list[6] = "김종서"
print(name_list)

#5-7 장길산 => 김길산으로 첫글자만 바꾸기
name_list[2] = "김길산"
print(name_list)
