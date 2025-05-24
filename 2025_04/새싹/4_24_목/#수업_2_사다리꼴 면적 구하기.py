#문제2) 사다리꼴 면적 구하기
#사다리꼴 면적 : (윗변+아랫변) * 높이 /2
above = int(input("윗변의 길이를 입력하세요"))
below = int(input("아랫변의 길이를 입력하세요"))
height = int(input("높이를 입력하세요"))
area = (above + below) * height / 2
print("사다리꼴의 넓이는 " + str(area) + " 입니다")