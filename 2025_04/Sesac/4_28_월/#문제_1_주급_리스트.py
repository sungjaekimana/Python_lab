#문제 - 주급 계산
#이름, 근무시간, 시간당급여액 - 5명에 대한
#홍길동  40        10000
#임꺽정  30        20000
#장길산  20        20000
#홍경래  10        15000
#이징옥  20        30000

name_list = []
work_timeList = []
per_payList = []
payList = []


# 풀이 1
# for i in range(0,5):
#     name = input("이름 : ")
#     work_time = int(input("일한 시간 : "))
#     per_pay = int(input("시급 : "))
    
#     name_list.append(name)
#     work_timeList.append(work_time)
#     per_payList.append(per_pay)
    
# for i in range(0,5):
#     total = work_timeList[i] * per_payList[i]
#     payList.append(total)
    
# for i in range(0,5):
#     print(f"{name_list[i]} {work_timeList[i]} {per_payList[i]} {payList[i]}")


# 풀이 2
# for i in range(0,2):
#     name = input("이름을 입력: ")
#     work_time = int(input("근무 시간을 입력: "))
#     per_pay = int(input("시급을 입력 : "))
    
#     name_list.append(name)
#     work_timeList.append(work_time)
#     per_payList.append(per_pay)

# for i in range(0,len(name_list)):
#     total = work_timeList[i] * per_payList[i]
#     payList.append(total)
    
# for i in range(0,len(name_list)):
#     print((name_list[i]), int((work_timeList[i])), int((per_payList[i])))

