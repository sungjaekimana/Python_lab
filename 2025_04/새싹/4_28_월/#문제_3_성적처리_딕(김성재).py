# 이름, 국어, 영어, 수학, 총점, 평균
# 평균에 대해서 수(90), 우(80), 미(70), 양(60), 가(60미만)
# 학생 3명

student = {}
person_List = [{"name":"김성재","kor":85,"eng":70,"math":90},
               {"name":"김단추","kor":60,"eng":70,"math":80},
               {"name":"박서현","kor":10,"eng":15,"math":20}]

for student in person_List:
    student["total"] = student["kor"] + student["eng"] + student["math"]
    student["average"] = student["total"] / 3

for student in person_List:
    print(f"{student["name"]}님의 국어점수는 {student["kor"]} ,영어점수는 {student["eng"]} ,수학점수는 {student["math"]} ,합계는 {student["total"]}, 평균은 {student["average"]:0.2f}입니다.")