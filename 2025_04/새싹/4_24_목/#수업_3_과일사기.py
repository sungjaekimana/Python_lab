#문제3) 철수가 식료품점에 가서 과일을 샀다. 사과와 배를 샀는데 사과는 5,000원 배는 10,000원이다.
#각각 사과와 배의 개수를 입력받아 총 금액을 구하는 프로그램을 작성하시오.

apple = 5000
pear = 10000
apple_num = int(input("사과 갯수를 입력하세요"))
pear_num = int(input("배의 갯수를 입력하세요"))
apple_cost = apple * apple_num
pear_cost = pear * pear_num
total_cost = apple_cost + pear_cost
print("총 금액은 " + str(total_cost) + " 원 입니다.")