# 입력 : 이름, 시급, 근무시간
# 출력 : 이름, 시급, 근무시간, 급여


workerList = []

def append():
    worker = {}
    worker["name"] = input("이름 : ")
    worker["perpay"] = int(input("시급 : "))
    worker["worktime"] = int(input("근무시간 : "))
    cal_money(worker)
    workerList.append(worker)
    
def cal_money(worker):
    worker["money"] = worker["perpay"] * worker["worktime"]
    
def output(workerList):
    for worker in workerList:
        print(f"{worker['name']}님의 총 급여는 {worker['money']}입니다.")
    
def start():
    while True:
        sel = int(input("1:추가, 2:출력, 3:종료"))
        if sel == 1:
            append()
        elif sel == 2:
            output(workerList)
        elif sel == 3:
            print("프로그램을 종료합니다.")
            return

start()