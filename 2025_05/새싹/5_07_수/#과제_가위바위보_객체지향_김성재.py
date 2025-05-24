import random

class ScissorsRockPaper:
    def __init__(self): #생성자를 통한 변수 만들기
        self.choice = [1, 2, 3] #1. 가위, 2.바위, 3.보
        self.drawcount = 0
        self.userwincount = 0
        self.comwincount = 0
         
    def com(self): #컴퓨터 pick
        com_choice = random.randint(1,3)
        return com_choice
    
    def user(self): #사람 pick
        while True:
            user_choice = int(input("\n1.가위, 2.바위, 3.보 (숫자로 선택) : "))
            if user_choice not in self.choice:
                print("다시 입력하세요!!! " )
                continue
            else :
                return user_choice
            
    def whoisWinner(self, user_choice, com_choice): #승패
        if user_choice == com_choice: #무승부
            result = 1
            return result 
        elif (user_choice == 1 and com_choice == 3) or (user_choice == 2 and com_choice == 1) or (user_choice == 3 and com_choice == 2):
            result = 2 #유저가 이기는 경우
            return result
        else:
            result = 3
            return result
        
    def start(self): #게임시작멘트
        print("게임을 시작합니다! 과연 승자는!! ")
        
    def output(self): #결과출력
        self.start()
        for i in range(0,10):
            user_choice = self.user()
            com_choice = self.com()
            result = self.whoisWinner(user_choice, com_choice)
            if result == 1:
                print("무승부")
                self.drawcount += 1
            elif result == 2:
                print("사람 승!")
                self.userwincount += 1
            else :
                result == 3
                print("컴퓨터 승 ㅠㅠ")
                self.comwincount += 1
                
        print("\n게임종료")
        print(f"사람 승 : {self.userwincount}, 컴퓨터 승 : {self.comwincount}, 무승부 {self.drawcount}")
        print(f"사람 승률 : {self.userwincount / 10:.2f}, 컴퓨터 승률 : {self.comwincount / 10:.2f}")
        
game1 = ScissorsRockPaper()
game1.output()