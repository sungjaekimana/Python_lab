"""
isEven(4) 짝수면 True, 홀수면 False 반환
toUpper("a") #대문자로 반환 -> ASTERISK
"""

def isEven(n):
    if n % 2 == 0:
        True
    return False
        
def toUpper(s):
    # A - 65, a - 97 두 알파벳사이에 32만큼 차이가 있음
    #                소문자 -> 대문자는 32를 더해주고
    #                대문자 -> 소문자는 32를 빼준다.
    # temp = ""
    # for c in s:
    #     if ord(c) >= ord("a") and ord(c) <= ord("z"):
    #         c = chr(ord(c)-32) # "a" : 97-62 = 65
    #     temp = temp + c
    # return temp
    return s.upper() #로 간편하게 할 수 있다.