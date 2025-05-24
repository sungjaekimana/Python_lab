#for문 안에서 또 for문이 작동하는 경우다.
#외부의 루프가 m번 돌고, 내부 루프가 n번 돌면 m*n번 수행을 한다.
#가급적 이중 for문까지만 동작하게끔 한다.

# for i in range(1,6):
#     for j in range(1,6):
#         print(f"i = {i}, j = {j}")

#문제1. 이중 for문을 사용하여 1~100까지 출력 한줄에 10개씩 출력하기

#100번을 돌린다. 10개씩 출력한다.

# k = 1
# for i in range(0,10):
#     for j in range(0,10):
#         print(k, end = "\t")
#         k = k + 1
#     print()

#문제2. 이중 for문
# 1 = 1
# 1 + 2 = 3
# 1 + 2 + 3 = 6

# sum = 0
# for i in range(1,11):
#     for j in range(1,i+1):
#         if j<i:
#             print(j, end = "+")
#         else:
#             print(j, end = "=")
#         sum += j
#     print(sum)

# #문제3. 별그리기
# for i in range(0,10):
#     for j in range(0,i):
#         print("*", end = "")
#     print()

#문제 4. 다이아 그리기

# """
#    *    별 1 공백 3 , 별의 개수 : 2*라인수-1, 공백 : 4-라인수
#   ***   별 3 공백 2
#  *****  별 5 공백 1
# ******* 별 7 공백 0
#  *****  별 5 공백 1
#   ***   별 3 공백 2
#    *    별 1 공백 3
# """

# lines = 4
# for i in range(1, lines+1):
#     print(" " * (lines-i), end ="")
#     print(("*") * (2*i-1))
    
# for i in range(lines-1,0,-1):
#     print(" " * (lines-i), end ="")
#     print(("*") * (2*i-1))



