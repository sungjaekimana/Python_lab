
workerList = []


def append(): #데이터 추가 함수
        worker = {} #dict type 객체 생성
        worker["name"] = input("이름: ")
        worker["work_time"] = int(input("근무시간 : "))
        worker["per_pay"] = int(input("시급 : "))
        worker["pay"] = 0
        
        workerList.append(worker)
        
def process(worker): #dict 가져와서 반환하는 방법, 매개변수로 값을 받아오면 외부로 전달은 안된다.
    worker["pay"] = worker["work_time"] * worker["per_pay"]
    
def process_main():
    for w in workerList:
        process(w)
        

def output(): #데이터 출력 함수
    for worker in workerList:
        print(f"{worker["name"]}", end = "\t")
        print(f"{worker["work_time"]}", end = "\t")
        print(f"{worker["per_pay"]}", end = "\t")
        print(f"{worker["pay"]}", end = "\t")
        print() #줄바꿈 코드

append() # 함수호출
output() # 함수호출

def main(): #return : 함수를 종료하면서 함수의 작업 내용을 함수 외부로 전달한다. #return 값을 안주면 그냥 함수 종료의 의미이다.
    while(True): #무한루프 - 종료를 하지 않는다. break나 return 구문을 써야한다.
        print("1.추가")
        print("2.출력")
        print("3.계산")
        print("0.종료")
        sel = input("선택:") #select
        if sel == "1": # 사용자가 1을 입력했을 때
            append() # 추가함수 호출하기
        elif sel == "2":
            output() # 출력함수
        elif sel == "3":
            process_main()
        elif sel == "0":
            print("프로그램을 종료합니다.")
            return # 함수 자체를 종료시킨다.
        else:
            print("잘못 선택하셨습니다.")
            
main()