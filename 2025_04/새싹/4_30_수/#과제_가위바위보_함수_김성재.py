#가위바위보 게임 10판 했을 때 이긴횟수를 카운트하라

import random


# 사람이 내는 거
def userchoice():
    user = int(input("1. 가위, 2.바위, 3. 보 : "))
    if user in [1,2,3]:
        return user
    else:
        print("1~3중에서 선택하세요! ")
        return userchoice()

# 컴퓨터가 내는거
def computerchoice():
    return random.randrange(1,4)

# 누가 이겼는지
def whoiswinner(user,computer):
    if user == computer:
        return 1
    elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
        return 2
    else: return 3
    
def start():
    print("가위, 바위, 보를 시작합니다.")

def main():
    start()
    drawcount = 0
    userwincount = 0
    computerwincount = 0
    for i in range(0,10):
        user = userchoice()
        computer = computerchoice()
        result = whoiswinner(user, computer)

        if result == 1:
            print("무승부")
            drawcount += 1
        elif result == 2:
            print("사람승")
            userwincount += 1
        else:
            print("컴퓨터승")
            computerwincount += 1
            
    print("\n게임종료")
    print(f"사람 승 : {userwincount}, 컴퓨터 승 : {computerwincount}, 무승부 {drawcount}")
    print(f"사람 승률 : {userwincount / 10:.2f}, 컴퓨터 승률 : {computerwincount / 10:.2f}")
    
main()