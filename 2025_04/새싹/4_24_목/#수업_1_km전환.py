#문제1) m를 km과 m로 전환하기
#2,300미터는 2km와 300미터입니다.
#미터를 입력받아서 각각 km와 m로 전환해서 출력하세요
#힌트) 몫구하는 연산자 //, 나머지 구하는 연산자 %

question = 2300
kilo_meter = question// 1000
meter = question % 1000
print(str(kilo_meter) + "km와 " + str(meter) + "m 입니다.")