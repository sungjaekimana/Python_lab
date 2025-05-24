a = [1,2,3,4]
b = [5,6,7,8]

#리스트를 결합하는 방법
c = a + b # 원본을 안바꾸고 더해진 새로운 list를 반환함
print(c)

a.extend(b) #원본에 추가함
print(a)

del c[0] #요소삭제
print(c)

del c[4:] #요소삭제, 슬라이싱 사용
print(c)

a = [1,3,5,6,2,4,5,7]
a.sort() #오름차순 정렬
print(a)

a.reverse() #순서뒤집기
print(a)

a.insert(0,100) #0번째 값에 100 넣기
print(a)
a.insert(5,77) #5번째 값에 77 넣기
print(a)
a.insert(len(a),88) #append 함수와 동일한 역할을 한다.
print(a)

a.remove(77) # 값이 여러개일때 첫번째로 나오는 값을 찾아서 삭제한다.
print(a)

a=[]
a.append("A")
a.append("B")
a.append("C")
a.append("D")
a.append("E")
print(a)






























