#객체를 하나만 만들 수 있는 클래스(싱글톤패턴)
#디비커넥션풀을 만들어 사용할 때 디비가 연결/읽거나쓰기/연결끊기의 과정을 거치는데
#여기서 읽거나쓰기보다 연결과 연결끊기가 더 많은 시간을 소요한다.
#이런 기법을 Pool 기법이라고 한다. 이 Pool은 객체 하나만 만들게 해야한다.
#이런 디자인 패턴을 싱글턴 패턴이라고 한다.

class Singleton:
    #객체를 하나만 만들어야 한다.
    __instance = None #객체를 만들라고 하면 None이 아닐때만 객체를 만들고
                      #None이면 있던 객체를 반환한다.
    @classmethod
    @classmethod
    def getInstance(cls):
        if cls.__instance==None:
            cls.__instance= cls.__new__(cls) #클래스를 이용해 인스턴스 만들기   
        return cls.__instance 

    def display(self):
        print("*************")
        
    def __init__(self): #편법
        #이미 객체가 존재하면 강제 에러를 발생시킨다.
        if Singleton.__instance is not None:
            raise Exception("이 클래스는 반드시 getInstance로만 객체 생성이 가능합니다.")
        
s1 = Singleton.getInstance()
s1.display()

#클래스외부에서 객체를 만드는것들은 파이썬이 막을 방법이 없다.
#다른 언어들은 생성자한테도 접근권한이 있어서 이걸 private로 만들면 외부에서 객체 생성을 못한다. 
#파이썬 생성자에 이미 붙어있어서 별도로 접근권한을 건드릴 수 없다.
#편법을 써야 한다. 데이터말고 일을 하는 클래스들을 만들 때 좋다.
#쓸데없이 객체가 만들어졌다 없어졌다 하는걸 방지할 수 있다.
s2 = Singleton() 
s2.display()