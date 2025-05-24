#숫자를 10개 입력받아서 각각 짝수와 홀수의 합과 평균을 구하는 프로그램을 작성하기.

#입력 : num
#출력 : 짝수합(even_sum), 홀수합(odd_sum)
#숫자세기 : i로 지정(1~10까지 count)

even_sum = 0
odd_sum = 0

for i in range(0,10):
    num = int(input("정수"))
    if num % 2 ==0:
        even_sum += num
    else:
        odd_sum += num

print(f"짝수의 합계 : {even_sum}")
print(f"홀수의 합계 : {odd_sum}")