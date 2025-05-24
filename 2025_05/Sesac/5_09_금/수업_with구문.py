# f = open("mpg.csv", "r")
# line = f.readlines()
# print(line[:3])

# f = open("mpg.csv", "r")
# line = f.readlines()
# print(line[:3])
# 위처럼 파이썬 버전이 낮을경우 거듭해서 파일을 여는것은 안된다.

with open("mpg.csv", "r") as f:
    lines = f.readlines()
    print(lines[:3])