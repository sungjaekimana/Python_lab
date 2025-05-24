colors = {"red":"빨간색", "blue":"파란색", "green":"초록색"}
#키 값은 주로 문자열을 사용한다. 만일에 같은 키 값을 두번 쓰면 두번째꺼로 업데이트 한다.
#딕셔너리는 "인덱싱, 슬라이싱" 불가
print(colors["red"])
print(colors["blue"])
print(colors["green"])

print(colors.keys()) #.keys() - 키값들의 목록을 보여준다.

#추가
colors["black"] = "검은색"
print(colors["black"])
colors["red"] = "붉은색"
print(colors)

#없는 키 값에 대해서는 어떻게 동작하는지?
# print(colors["pink"]) #KeyError가 뜬다.

if "pink" in colors.keys():
    print(colors["pink"])
else:
    print("pink is not exist")
    
print(colors.items(),type(colors))

print(colors.values())

#colors.clear() # 전체 삭제
#print(colors)

#특정키 삭제 - pop(키값)
colors.pop("red")
print(colors)




















