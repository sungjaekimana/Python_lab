#지방 노동청에 신고가 들어옴. 회사가 성별간 임금차별이 있다.
#직원 전체 10명이고, 성별과 연봉을 입력받아서 남자평균, 여자평균 구하기

workerlist = []
wagelist = []

for i in range(3):
    sex = input("성별을 입력하세요 : 남 or 여 ")
    wage = int(input("연봉을 입력하세요 : "))
    workerlist.append({"sex" : sex, "wage" : wage})
    
male_count = 0
female_count = 0
male_sum = 0
female_sum = 0

for i in workerlist:
    if i["sex"] == "남":
        male_count = male_count + 1
        male_sum = male_sum + i["wage"]
    else:
        female_count = female_count + 1
        female_sum = female_sum + i["wage"]
        
male_ave = male_sum / male_count
female_ave = male_sum / male_count

print(male_ave)
print(female_ave)