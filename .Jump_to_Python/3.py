#제어문 - 조건문, 반복문

#조건문 if
money = True
if money:
     print("택시를 타고 가라")
else:
     print("니 힘으로 알아서 걸어가라")

money = 3000
card = True
if money>=3000 or card:
     print("택시타고 편하게 가라")
else:
     print("뭔 택시냐 걸어가라")

#x or y - 둘 중 하나만 참이어도 참이다.
#x and y - 둘 다 참이어야 참이다.
#not x - x가 거짓이면 참이다.

money = 2000
card = True
if money>=3000 and card:
     print("택시타고 편하게 가라")
else:
     print("뭔 택시냐 걸어가라. 근데 돈있어도 택시타는게 맞냐? 아껴써라")

a = (1,2,3)
print(type(a))
if 1 in a:
     print("있으면 나 줘.")
else:
     print("없으면 가서 찾아와.")

money = 3000
pocket = ["paper", "cellphone", "money"]
if "money" in pocket and money>5000:
     print("택시 타고 가라! 개 졸부네")
else:
     print("돈도 없는게 택시를?")
     
pocket = ["paper", "cellphone", "money"]
if "money" in pocket:
     print("택시를 타고가라")
elif "card" in pocket:
     print("택시를 타고 가라")
else:
     print("걸어가라")
     
sj = ["열정", "꾸준함","부지런함"]
if "열정" and "꾸준함" and "부지런함" in sj:
     print("너 재능있어. 그대로만 해")
else:
     print("너 재능없어. 때려쳐라!. - 랄로가")
     
pocket = ["paper", "cellphone"]
if "money" in pocket:
     pass
else:
     print("카드 꺼내라 뭐하냐. 기다리시잖아. 이래서 MZ는 안된다니까")

#반복문 while, for문
#while문 - 조건문이 참인동안 while문에 속한 문장들이 반복되는 구조
#어떤 조건을 계속 반복할 때 쓰인다.

treehit = 0
while treehit<10:
     treehit = treehit +1
     print("나무를 %d번 찍었습니다." %treehit)
     if treehit == 10:
          print("나무가 쓰러집니다")
          
number = 0
while number <= 4:
     number = number + 1
     print("4와 같습니다.")
     
     
coffee = 10 # Jump to Python 응용해서 직접 만들었음음 ㅎㅎㅎㅎㅎㅎ
money = 50
while money:
     print("커피를 추출합니다.")
     coffee = coffee - 1
     money = money - 10
     print(f"남은 돈은 {money}원, 커피는 {coffee}개입니다.")
     if coffee == 0:
          print("커피가 없습니다.")
     elif money == 0:
          print("돈이 없습니다.")
          break
     
# coffee.py

# coffee = 10
# while True:
#     money = int(input("돈을 넣어 주세요: "))
#     if money == 300:
#         print("커피를 줍니다.")
#         coffee = coffee -1
#     elif money > 300:
#         print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
#         coffee = coffee -1
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#         print("남은 커피의 양은 %d개 입니다." % coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
#         break

#while문의 맨 처음으로 돌아가는 방법

a = 0
while a < 10:
     a = a + 1
     if a % 2 == 0:
          continue 
     else:
          print(a)
          

#for문 - for 변수 in 리스트(튜플, 문자열)
#여러개의 자료가 담긴 것을 하나씩 뽑아올 때 쓰인다.
#ex_리스트나 튜플이나 문자열의 값을 하나씩 써야 할때??
test_list = ["one", "two", "three"]
for i in test_list:
     print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
     print(first + last)

marks = [90,25,67,45,80]
student = 0
for mark in marks:
     if mark >= 60:
          print(f"{student}학생은 합격입니다")
     else:
          print(f"{student}학생은 불합격입니다.")
     student = student + 1
     
# marks2.py
marks = [90, 25, 67, 45, 80]

number = 0 
for mark in marks: 
    number = number +1 
    if mark < 60:
        continue 
    print(f"{number}번 학생 축하합니다. 합격입니다.")
    
marks = [90, 25, 67, 45, 80]
stu = 0
for mark in marks:
     if mark >= 60:
          print(f"{stu}학생은 합격입니다. 축하합니다!!")
     else:
          print(f"{stu}학생은 불합격입니다. 다음에 또 봐요!")
     stu = stu + 1

add = 0
for i in range(1,11):
     add = add+1
     print(add)

for i in range(2,10):
     for j in range(1,10):
          print(i*j, end=" ")
     print("")
     

     






          



     




     
          

          











     
     


     

     

