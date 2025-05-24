try:
    x = 10
    y = 0
    z = x/y
    print(f"x = {x}, y = {y}, z = {z}")
except ZeroDivisionError as e:
    print(e) # 결과 division by zero


try:
    x = int(input("정수 : "))
    y = int(input("정수 : "))
    z = x/y
    print(f"x = {x}, y = {y}, z = {z}")
except ZeroDivisionError as e:
    # print(e)
    print("0으로 나눌 수 없습니다.")
    
    
try:
    x = int(input("정수 : "))
    y = int(input("정수 : "))
    z = x/y
    print(f"x = {x}, y = {y}, z = {z}")
except ZeroDivisionError as e:
    # print(e) # 결과 division by zero
    print("0으로 나눌 수 없습니다.")
#finally는 주로 파일, 데이터베이스, 네트워크 처리등에 많이 사용한다.
#파일, 데이터베이스, 네트워크 연결 ...등등 오류발생 close
finally: 
    print("이 부분은 반드시 실행된다.")