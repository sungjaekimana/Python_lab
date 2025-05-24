# 이름, 국어, 영어, 수학, 총점, 평균, 학점이 나오는 객체지향을 만들어라
# 입력 : 이름, 국어, 영어, 수학
# 계산 : 총점 = 국어 + 영어 + 수학, 평균 = 총점 / 3, 학점은 기준에 따라 분류
# 출력 : 이름, 국어, 영어, 수학, 총점, 평균, 학점(탭 사용)

class GradeProcessing:
    def __init__(self):
        self.studentList = []
        
    def input(self): #입력
        name = input("이름 : ")
        while True:
            kor = int(input("국어 : "))
            if kor > 100 or kor < 0:
                print("0~100사이의 숫자로 입력하세요")
                continue
            eng = int(input("영어 : "))
            if eng > 100 or eng < 0:
                print("0~100사이의 숫자로 입력하세요")
                continue
            math = int(input("수학 : "))
            if math > 100 or math < 0:
                print("0~100사이의 숫자로 입력하세요")
                continue
            break
        return {"name" : name, "kor" : kor, "eng" : eng, "math" : math}
        
    def cal_total(self, student): #총점계산
        total = student["kor"] + student["eng"] + student["math"]
        return total
    
    def cal_avg(self, total):
        avg = total / 3
        return avg
        
    def grade_check(self, avg): #등급체크
        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "C"
        else:
            grade = "D, 재시험요망"
        return grade
    
    def processStart(self):
        print("성적처리 프로그램을 실행합니다.")
        
        while True:
            student = self.input()
            total = self.cal_total(student)
            avg = self.cal_avg(total)
            grade = self.grade_check(avg)
            
            student["total"] = total
            student["avg"] = avg
            student["grade"] = grade
            
            self.studentList.append(student)
            
            print(f"이름 : {student['name']}, 총점 : {student['total']}, 평균 : {student['avg']}, 학점 : {student['grade']}")
            
            keepGoing = input("계속하시려면 y, 종료하시려면 n을 눌러주세요. ").lower()
            if keepGoing == "y":
                continue
            else:
                keepGoing == "n"
                break
        
        print("전체학생의 성적은 아래와 같습니다.")
        for stu in self.studentList:
            print(f"이름 : {stu["name"]}", end = "\t")
            print(f"국어 : {stu["kor"]}", end = "\t")
            print(f"영어 : {stu["eng"]}", end = "\t")
            print(f"수학 : {stu["math"]}", end = "\t")
            print(f"총점 : {stu["total"]}", end = "\t")
            print(f"평균 : {stu["avg"]}", end = "\t")
            print(f"학점 : {stu["grade"]}")
            
        print("시험보느라 고생했습니다.")
        
g = GradeProcessing()
g.processStart()

        
    