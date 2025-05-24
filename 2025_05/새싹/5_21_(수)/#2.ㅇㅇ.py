# 🔢 문제 2. 숫자야구 게임
# 문제 설명
# 컴퓨터가 1부터 9 사이의 서로 다른 숫자 3개를 임의의 순서로 생성한다.
# 사용자는 3개의 숫자를 순서대로 입력한다.
# 입력한 숫자들을 컴퓨터의 숫자와 비교하여 다음 규칙에 따라 결과를 출력한다:

# 숫자와 위치가 모두 맞으면 👉 스트라이크 (Strike)
# 숫자만 맞고 위치는 다르면 👉 볼 (Ball)
# 숫자도 틀리고 위치도 틀리면 👉 아웃 (Out)

# 사용자가 3스트라이크를 맞힐 때까지 게임은 반복된다.
# 게임 종료 시 시도 횟수를 출력하시오.

import random

def com():
    com_nums = random.sample(range(1,10),3)
    return com_nums

def user():
    user_nums_list = []
    user_nums = int(input("서로 다른 숫자 세개를 입력하세요"))
    if user_nums < 1 or user_nums > 9:
        print("1~9사이의 숫자를 입력하세요")
    elif user_nums in user_nums_list:
        print("중복된 숫자입니다.")
    else:
        user_nums_list.append(user_nums)
    return user_nums_list

def compare(user_nums_list, com_nums):
    strike = 0
    ball = 0
    out = 0
    for i in len(user_nums_list):
        if user_nums_list[i] == com_nums[i]:
            strike += 1
        elif user_nums_list[i] in com_nums:
            ball += 1
        else:
            out += 1
    return strike, ball, out

def output():
    print
    
    
    
    
    
def main():
    


    