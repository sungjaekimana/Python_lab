class Book:
    title = "채식주의자"
    def __init__(self, title = "쌍갑포차", price = 10000):
        self.title = title
        self.price = price
        self.count = 10
        
    def process(self):
        self.total_price = self.price * self.count
        
    def output(self):
        print(self.title, self.price, self.count, self.total_price)
        

b = Book() # 객체가 만들어진다.
#title이라는 클래스 내부 변수에 접근하려면 접근연산자로 .(도트)를 사용한다.
print(b.title)

b2 = Book("아 지갑놓고 나왔다")
print(b2.title)

b3 = Book("뽀짜툰", 30000)
print(b3.title, b3.price)