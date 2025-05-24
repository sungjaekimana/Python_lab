import random

def computer_numbers():
    com_numbers = []
    while len(com_numbers) < 3:
        num = random.randint(1,9)
        if num not in com_numbers:
            com_numbers.append(num)
    return com_numbers
            
def user_numbers():
    while True:
        user_number = input("서로 다른 숫자 3개를 입력하세요 : ")
        if len(user_number) != 3:
            print("3자리 숫자를 입력해주세요")
            continue
        
        user_number_list = [int(n) for n in user_number]
        if len(set(user_number_list)) != "3" or "0" in user_number_list:
            print("서로 다른 1~9 사이의 숫자를 입력해주세요.")
        return user_number_list
    
def compare(user_number, com_number):
    strike = 0
    ball = 0
    for i in range(3):
        if user_number[i] == com_number[i]:
            strike += 1
        elif user_number[i] in com_number:
            ball += 1
    return strike, ball

def start():
    print("숫자 야구 시작")
    com_number = computer_numbers()
    attempts = 0
    while True:
        user = user_numbers()
        attempts += 1
        strike, ball = compare(user, com_number)
        print(f"{strike} 스트라이크, {ball} 볼")
        
        if strike == 3:
            print(f"{attempts}번 만에 정답을 맞췄습니다! 축하해요!! ")
            break
        
start()