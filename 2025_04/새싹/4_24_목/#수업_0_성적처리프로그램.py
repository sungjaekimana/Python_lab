#성적처리 프로그램
#이름, 국어, 영어, 수학 성적을 입력받아 총점과 평균을 구하라.
#입력 : 이름(문자열), 국어, 영어, 수학
#출력 : 총점, 평균

#입력
stu_name = input("당신의 이름은?")
stu_kor = int(input("국어?"))
stu_eng = int(input("영어?"))
stu_math = int(input("수학?"))

#계산 수식 - 수학의 경우는 좌변과 우변을 바꿀 수 있다. 프로그램의 경우는 좌변은 언제나 변수만 가능하다.
stu_total = stu_kor + stu_eng + stu_math
stu_average = stu_total//3
print(stu_name, stu_total, stu_average)