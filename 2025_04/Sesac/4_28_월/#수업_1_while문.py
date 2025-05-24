#while 문은 조건에 의해서 특정 조건을 만족할 때만 수행을 한다.
#때로는 단 한번도 수행이 안될 가능성이 있을 때 사용하면 좋다. for문 대신에 쓸 수 있다.
#while 조건식: - 조건식의 결과가 True일 수행한다.

# i = 1
# while i <= 10:
#     print(i)
#     i += 1 #while문의 마지막 문장은 조건이 False가 되는 상황을 만들게 하는 것이 좋다.
    
# num = (input("숫자를 입력하세요(0~9) : "))

# while ord(num)<48 or ord(num)>57:
#     print("문자 말고 숫자쓰세요. 마지막 기회입니다. ")
#     num = input("숫자로 입력하세요(0~9): ")

i = 1
sum = 0

while sum < 1000:
    sum = sum + i
    i = i + 1
    
print(f"1000은 {i}번째에 넘습니다.")
    


