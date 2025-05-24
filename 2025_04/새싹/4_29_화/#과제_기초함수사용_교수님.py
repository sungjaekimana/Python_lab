#오늘의 과제 
words = ["assembly", "java", "rain", "notebook", "north", "south", "hospital", "programming", "house", "hour"]

#문제1. filter를 사용해서 글자수가 6글자 이상인 단어만 출력하기 (컴프리핸션X)

resultList = list(filter(lambda x : len(x) >= 6, words)) #iterable이 달려있으면 list 꼭 달기
print(resultList)
#x에 전달되는건 string타입이다. len(x) : 문자열 길이
#파이썬의 lambds는 한줄만 가능, 다른언어는 2줄 이상도 많음.

#문제2. map함수를 사용해서 글자를 대문자로 바꾸어서 출력하기  (컴프리핸션X)
resultList = list(map(lambda x : x.upper(), words))
print(resultList)

#문제3. sorted 함수를 사용하여 단어들의 길이순으로 오름차순 정렬하여 출력하기
sortedList1 = sorted(words, key = lambda x : len (x))
print(sortedList1)

#문제4. sorted 함수를 사용하여 알파벳 순으로 내림차순으로 정렬하여 출력하기
sortedList1 = sorted(words, reverse = True)
print(sortedList1)

#문제5. 단어중에 o가 포함되는 단어가 모두 몇개인지 카운트하기 (힌트,filter를 사용)
resultList = list(filter(lambda w:"o" in w, words))
print(len(resultList))

