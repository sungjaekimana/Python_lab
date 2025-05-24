#내장함수 : 시스템에서 만들어준 함수.

print(abs(-4)) #abs : 절대값을 구함.
print(abs(4))

print(all([1,2,3])) #all : 지금 전달받은 요소중에 0이 하나라도 존재하면 False.
print(all([1,2,3,0])) #요소전체가 True이면 True

print(any([1,2,3])) #any : 지금 전달받은 요소중에 0이 아닌것이 하나라도 존재하면 True.
print(any([1,2,3,0])) #하나라도 True이면 True
                      #0 - False, "" - False
print(any(["a","b","c"])) #True
print(any(["a","b",""])) #True

#######################################
print(dir([1,2,3])) #dir : 객체가 지닌 변수나 함수를 보여줌.
print(dir(dict()))

mok, nmg = divmod(5,3) # divmod는 두개의 숫자를 입력받아 몫과 나머지를 튜플로 리턴
print(mok)
print(nmg)

for i, c in enumerate("Life is egg"): #enumerate 순서가 있는 데이터를 입력받아 인덱스값과 같이 리턴한다.
    print(i,c)

result = eval("1+10+3") #문자열로 구성된 표현식을 입력으로 받아 해당 문자열을 실행한 결과값을 리턴
print(result)

a = [3,4,-1,2,9,8,7,12,15,21]
#음수만 filter의 첫번째 매개변수는 함수여야 한다.
#두번째 매개변수로 전달된 요소 하나를 매개변수로 하고 반환은 True or False
def isPositive(x):
    if x > 0:
        return True
    return False

poList = list(filter(isPositive, a)) # filter : 리턴값이 참인 것만 걸러내서 리턴한다.
print(poList)

#한번 만들어서 쓰고 벌는 함수인 람다를 사용하자.
poList = list(filter(lambda x: x>0, a))
print(poList)

print(f"최대값 : {max(a)}, 최소값 : {min(a)}") #max()는 최대값, min() 최소값
print(pow(2,4))