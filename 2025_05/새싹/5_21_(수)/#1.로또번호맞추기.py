# 문제 1. 로또 번호 맞추기 게임
# 1부터 45까지의 숫자 중에서 중복 없이 6개의 번호를 컴퓨터가 랜덤으로 선택한다.
# 사용자가 6개의 번호를 입력하면, 컴퓨터 번호와 비교해 일치하는 번호 개수를 출력하는 프로그램을 작성하시오.
import random

# 컴퓨터 6개 숫자 중복없이 랜덤 뽑기
def com():
    com_nums = random.sample(range(1,46),6)
    return com_nums

# 사람 6개 번호 입력
def append():
    user_num_list = []
    while len(user_num_list) < 6:
        user_nums = int(input("1 ~ 45중 숫자를 입력하세요 : "))
        if user_nums < 1 or user_nums > 45:
            print("1에서 45 사이의 숫자를 입력하세요")
        elif user_nums in user_num_list:
            print("중복된 숫자입니다.")
        else:
            user_num_list.append(user_nums)
    return user_num_list
    
# 숫자 비교
def compare(user_nums, com_nums):
    correct_count = 0
    ggaby_count = 0
    error_count = 0
    
    for i in range(0,6):
        if user_nums[i] == com_nums[i]:
            correct_count += 1
        elif user_nums[i] in com_nums:
            ggaby_count += 1
        else:
            error_count += 1
    print(f"스트라이크 : {correct_count}, 위치틀림 : {ggaby_count}, 다틀림 : {error_count}")
    return correct_count
    

# 메인함수            
def main():
    print("=======================")
    print("6자리 숫자를 맞춰보세요!")
    print("=======================")
    
    com_nums = com()
    attempt = 0
    
    while True:
        attempt += 1
        user_nums = append()
        correct_count = compare(user_nums, com_nums)
    
        if correct_count == 6:
            print("정답입니다.")
            print(f"총 시도횟수 {attempt}번")
            print(f"정답 : {com_nums}")
    
main()