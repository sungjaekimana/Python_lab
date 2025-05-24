#숫자를 10개 입력받아서 각각 짝수와 홀수의 합과 평균을 구하는 프로그램을 작성하기.

# for문, if문 사용, 짝수의 합, 홀수의 합, 짝수의 평균, 홀수의 평균

even_sum = 0
odd_sum = 0
even_cou = 0
odd_cou = 0

for i in range(1,11):
    num = int(input("숫자를 10개 입력하세요"))
    if i % 2 == 0:
        even_sum = even_sum + num
        even_cou = even_cou + 1
    else:
        odd_sum = odd_sum + num
        odd_cou = odd_cou + 1
        
even_ave = even_sum // even_cou
odd_ave = odd_sum // odd_cou

print(f"짝수의 개수는 {even_cou}개, 합은 {even_sum}이며 평균은 {even_ave} 입니다.")
print(f"홀수의 개수는 {odd_cou}개, 합은 {odd_sum}이며 평균은 {odd_ave} 입니다.")
