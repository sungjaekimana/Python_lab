#자판기 = 객체지향
import pickle 
    
class ProductVending:
    def __init__(self, name, price, count): # 생성자 
        self.name = name
        self.price = price
        self.count = count
        self.payMoney = 0
        self.change = 0

    def process(self): # 거스름돈 = 넣은돈 - 상품가격
        print("\n===계산시작===")
        while True:
            self.payMoney = int(input("돈을 넣으세요 : "))
            self.change = self.payMoney - self.price
            if self.change >= 0:
                return
            else:
                self.change < 0
                print("돈을 다시 넣어주세요")
                
    def printInfoManager(self):
        print(f"상품명 : {self.name}", end = "\t")
        print(f"상품가격 : {self.price}", end = "\t")
        print(f"상품재고 : {self.count}")

    def printInfoBuyer(self):
        print(f"상품명 : {self.name}", end = "\t")
        print(f"상품가격 : {self.price}")
    
    def printCalBuyer(self): # 계산출력 
        print(f"상품명 : {self.name}", end = "\t")
        print(f"상품가격 : {self.price}", end = "\t")
        print(f"넣은돈 : {self.payMoney}", end = "\t")
        print(f"거스름돈 : {self.change}")
        print("===계산완료===")
        
class ProductVendingManager(): #관리자 모드..?
    def __init__(self, productList):
        self.productList = productList
    
    def append(self): #상품추가
        name = input("추가할 상품명 : ")
        price = int(input("추가할 상품가격 : "))
        count = int(input("추가할 상품개수 : "))
        product = ProductVending(name,price,count)
        self.productList.append(product)
    
    def search(self): #상품 검색, 이름으로
        name = input("검색할 상품명 : ")
        resultList = list(filter(lambda x: name in x.name, self.productList))
        
        if len(resultList) == 0:
            print("검색한 상품이 없습니다.")
            
        for index, name in enumerate(resultList):
            print(f"번호 : {index}", end = "\t")
            name.printInfoManager()
            
    def remove(self): #상품 삭제
        name = input("검색할 상품명 : ")
        resultList = list(filter(lambda x: name in x.name, self.productList))
        
        if len(resultList) == 0:
            print("검색한 상품이 없습니다.")
            
        for index, name in enumerate(resultList):
            print(f"번호 : {index}", end = "\t")
            name.printInfoManager()
        
        sel = int(input("삭제할 상품의 번호를 입력해주세요 : "))
        self.productList.remove(resultList[sel])
    
    def modify(self): #상품 수정
        name = input("검색할 상품명 : ")
        resultList = list(filter(lambda x: name in x.name, self.productList))
        
        if len(resultList) == 0:
            print("검색한 상품이 없습니다.")
            
        for index, name in enumerate(resultList):
            print(f"번호 : {index}", end = "\t")
            name.printInfoManager()
        
        sel = int(input("수정할 상품의 번호를 입력해주세요 : "))
        item = resultList[sel]
        item.name = input("상품명 : ")
        item.price = int(input("가격 : "))
        item.count = int(input("재고 : "))
        print("===수정완료===")
        
    def save(self): # 저장
        with open("product1", "wb") as f:
            pickle.dump(self.productList, f)
        print("===저장완료===")
    
    def load(self): # 불러
        with open("product1", "rb") as f:
            self.productList = pickle.load(f)
            self.printInfoManager()
        print("===불러오기완료===")
            
    def printAll(self): # 전체상품출력
        for p in self.productList:
            p.printInfoManager()
            
        if len(self.productList) == 0:
            print("등록된 상품이 없습니다.")
        print("===전체상품출력완료===")
    
class ProductVendingBuyer: #구매자 모드..?
    def __init__(self, productList):
        self.productList = productList
        
    def printAll(self): # 전체상품출력
        
        if len(self.productList) == 0:
            print("상품이 없습니다.")
            return
        
        for p in self.productList:
            p.printInfoBuyer()
            
        print("\n===전체상품출력완료===\n")
            
    def choice(self):#:상품 선택 및 계산 및 출력...? 이렇게 해도 되나
        while True:
            name = input("구매할 상품명 : ")
            resultList = list(filter(lambda x: name in x.name, self.productList))

            if len(resultList) == 0:
                print("상품이 없습니다. 다시 시도해주세요.")
                return

            for index, item in enumerate(resultList):
                print(f"번호 : {index}", end="\t")
                item.printInfoBuyer()

            try:
                sel = int(input("구매할 상품의 번호를 입력해주세요 : "))
                if sel < 0 or sel >= len(resultList):
                    print("잘못된 번호입니다.")
                    return
            except ValueError:
                print("숫자를 입력해주세요.")
                return

            item = resultList[sel]

            if item.count <= 0:
                print("해당 상품은 품절입니다.")
                return

            item.process()
            item.printCalBuyer()
            item.count -= 1
            return
            
def main():
    product_list = [
        ProductVending("콜라", 2000, 5),
        ProductVending("사이다", 1800, 3),
        ProductVending("물", 1000, 10)
    ]
    admin = ProductVendingManager(product_list)
    buyer = ProductVendingBuyer(product_list)

    while True:
        print("=== 자판기 메인 메뉴 ===")
        print("1. 구매자 모드")
        print("2. 관리자 모드")
        print("0. 종료")  
        sel = input("번호 선택: ")

        if sel == "1":
            while True:
                print("\n===구매자 메뉴===")
                print("1. 상품 보기")
                print("2. 상품 구매")
                print("0. 돌아가기")
                b_sel = input("번호 선택: ")
                if b_sel == "1":
                    buyer.printAll()
                elif b_sel == "2":
                    buyer.choice()
                elif b_sel == "0":
                    break
                else:
                    print("잘못된 입력입니다.")

        elif sel == "2":
            pwcount = 3
            success = False
            while pwcount > 0:
                pw = input("비밀번호를 입력하세요 : ")
                if pw == "admin":
                    print("로그인 성공")
                    success = True
                    break
                else:
                    pwcount -= 1
                    print(f"비밀번호가 틀립니다. 남은 기회는 {pwcount}번 입니다.")
            if not success:
                print("로그인 실패. 메인 메뉴로 돌아갑니다.")
                continue

            while True:
                print("\n===관리자 메뉴===")
                print("1. 상품 목록 보기")
                print("2. 상품 추가")
                print("3. 상품 수정")
                print("4. 상품 삭제")
                print("5. 저장")
                print("6. 불러오기")
                print("0. 돌아가기")
                sel2 = input("번호 선택: ")
                if sel2 == "1":
                    admin.printAll()
                elif sel2 == "2":
                    admin.append()
                elif sel2 == "3":
                    admin.modify()
                elif sel2 == "4":
                    admin.remove()
                elif sel2 == "5":
                    admin.save()
                elif sel2 == "6":
                    admin.load()
                elif sel2 == "0":
                    break
                else:
                    print("잘못된 입력입니다.")

        elif sel == "0":
            print("자판기를 종료합니다.")
            break

        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    main()