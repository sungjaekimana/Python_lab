# 계산기 만들기
# 입력 : 두개의 숫자
# 출력 : 더하기, 빼기, 곱하기, 나누기

class Fourcal():
     def __init__(self, num1, num2):
          self.result = 0
          self.num1 = num1
          self.num2 = num2
     
     def cal_plus(self): #덧셈
          self.result = self.num1 + self.num2
          return print("덧셈결과는", self.result)
     
     def cal_subtract(self) : #뺄셈
          self.result = self.num1 - self.num2
          return print("뺄셈결과는", self.result)
     
     def cal_multiple(self): #곱셈
          self.result = self.num1 * self.num2
          return print("곱셈결과는", self.result)
     
     def cal_divide(self): #나눗셈
          self.result = self.num1 / self.num2
          return print("나눗셈결과는", self.result)
     
cal1 = Fourcal(10,5)
cal1.cal_plus()
cal1.cal_subtract()
cal1.cal_multiple()
cal1.cal_divide()
          
     
