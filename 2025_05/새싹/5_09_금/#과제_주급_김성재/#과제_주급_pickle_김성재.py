import pickle

class Worker:
    def __init__(self, name, worktime, perpay):
        self.name = name
        self.worktime = worktime
        self.perpay = perpay
        self.weekpay = 0
        self.pluspay = 0
        self.totalpay = 0
        
    def calweekpay(self): #기본급 계산법 
        self.weekpay = self.worktime * self.perpay
        return self.weekpay
        
    def calpluspay(self): #추가수당 계산법 
        if self.worktime > 20:
            self.pluspay = (self.perpay * 0.5) * (self.worktime - 20)
        else:
            self.pluspay = 0
        return self.pluspay
    
    def caltotalpay(self): #총급여 계산법 
        self.totalpay = self.weekpay + self.pluspay
        return self.totalpay
    
    def calAll(self):#급여계산
        self.calweekpay()
        self.calpluspay()
        self.caltotalpay()
        
    def print_info(self): #출력
        print(f"이름 : {self.name}", end = "\t")
        print(f"근무시간 : {self.worktime}", end = "\t")
        print(f"시급 : {self.perpay}", end = "\t")
        print(f"기본급 : {self.weekpay:.0f}", end = "\t")
        print(f"추가수당 : {self.pluspay:.0f}", end = "\t")
        print(f"총급여 : {self.totalpay:.0f}")
    
class WorkerManager:
    def __init__(self):
        self.workerList = [
    # Worker("김성재", 40, 15000),
    # Worker("이지은", 18, 12000),
    # Worker("박지성", 25, 20000)
]
        
    def append(self): # 1.추가
        name = input("이름 : ")
        worktime = int(input("근무시간 : "))
        perpay = int(input("시급 : "))
        worker = Worker(name, worktime, perpay)
        self.workerList.append(worker)
        print("===추가완료===")
        
    def printAll(self): # 2.출력 
        for w in self.workerList:
            w.print_info()
        
    def calAllWorker(self): # 3.계산
        for w in self.workerList:
            w.calAll()
        print("===계산완료===")
        
    def save(self): # 4.저장
        with open("workers1", "wb") as f:
            pickle.dump(self.workerList, f)
        print("===저장완료===")
        
    def load(self): # 5.불러
        with open("workers1", "rb") as f:
            self.workerList = pickle.load(f)
            self.printAll()
        print("===불러완료===")

    def main(self):
        funcList = [None, self.append,self.printAll, self.calAllWorker, self.save, self.load]
        while True:
            print("1.추가 : ")
            print("2.출력 : ")
            print("3.계산 : ")
            print("4.저장 : ")
            print("5.불러 : ")
            print("0.종료 : ")
            sel = int(input("번호를 선택하세요 : "))
            if sel > 0 and sel < 6:
                funcList[sel]()
            elif sel == 0:
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 번호입니다. 다시 입력하세요.")
            
            
if __name__ == "__main__":
    w1 = WorkerManager()
    w1.main()