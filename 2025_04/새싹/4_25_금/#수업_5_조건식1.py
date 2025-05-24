#정수를 하나를 입력받아서 양수일 경우에 본래의 값에 *5를 해서 출력해아
n = int(input("정수 : "))
if n>0:
    n=n*5
print(n)

#양수이면 양수라고 출력하고 음수나 0이면 양수아님 
if n>0:
    print("양수")
else:
    print("양수 아님")

#양수이면 양수 0  음수
if n>0:
    print("양수")
elif n==0:
    print("0")
else:
    print("음수") 


    


