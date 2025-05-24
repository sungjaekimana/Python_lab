#문제 - 주급 계산
#이름, 근무시간, 시간당급여액 - 5명에 대한
#홍길동  40        10000
#임꺽정  30        20000
#장길산  20        20000
#홍경래  10        15000
#이징옥  20        30000



# 풀이1
# worker = {}
# person_List = [{"name":"홍길동", "work_time":40, "per_pay":10000},
#               {"name":"임꺽정", "work_time":30, "per_pay":20000},
#               {"name":"장길산", "work_time":20, "per_pay":30000}
# ]
# for worker in person_List:
#     worker["pay"] = worker["work_time"] * worker["per_pay"] 
    
# for worker in person_List:
#     print(f"{worker["name"]} {worker["work_time"]} {worker["per_pay"]}")

# # 풀이2
# worker_list = []

# for i in range(0,2):
#     name = input("이름 : ")
#     worktime = int(input("근무시간 : "))
#     hourpay = int(input("시급 : "))
                  
#     worker= {}
#     worker["name"] = name
#     worker["worktime"] = worktime
#     worker["hourpay"] = hourpay
#     worker_list.append(worker)

# for worker in worker_list:
#     worker["total"] = worker["worktime"] * worker["hourpay"]
    
    
# for worker in worker_list:
#     print(f"{worker["name"]}{worker["total"]}")
        



