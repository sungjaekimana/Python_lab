## mpg.csv파일 가져와서 실린더개수 8 4 2 종류별 카운트 하기
f = open("mpg.csv", "r")
lines = f.readlines()
f.close()

print(lines[:4])
#print(lines[:4])
cylinder_count = {}
for line in lines:
    line = line[:len(line)-1] #마지막에 있는 \n 지우기
    values = line.split(",")
    if values[1] in cylinder_count.keys():
        cylinder_count[values[1]] += 1
    else:
        cylinder_count[values[1]] = 1
        
print(cylinder_count)