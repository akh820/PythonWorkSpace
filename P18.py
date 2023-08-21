# 클래스 ... ( 설계 ...)
# 객체지향 프로그램 (Object Orineted Programm)

# 속성 + 기능(메소드) 사실상 문법은 Func랑 같다

# 클래스 선언 -> 인스턴스 생성
# 함수 선언 -> 함수 호출
class Car: # 클래스는 글자 맨앞 대문자 사용
    def __init__(uzae, name, fuel, speed, distance): # init 초기화, 생성자, uzae는 자기자신의 메모리 주석값
        # 생성자 - 속성 정의
        uzae.name = name
        uzae.fuel = fuel
        uzae.speed = speed
        uzae.distance = distance
# 메소드(기능) : 쉽게 생각하면 클래스 안에 선언된 함수, self가 핵심
    def showStatus(self): #self를 무조건 써줘야한다, Parameter를 받지않음
        print(f'{self.name} = 연료 : {self.fuel}, 속도 : {self.speed}, 현재거리 : {self.distance}')
    def run(self, count):
        x = 0
        while x <= count:
            self.fuel -= 1
            self.distance += self.speed
            # print(f'연료가 {self.fuel} 남았습니다.')
            if self.fuel <= 0:
                print(f'{self.name}가 연료부족!!!.')
                break
            x += 1


# 인스턴스 생성 , 메모리가 묶여서 생성된다.
c1 = Car("1번 자동차", 20, 5, 0)
c2 = Car("2번 자동차", 30, 15, 0)

c1.showStatus()
# c1.__init__(1,2,3,4) # 일단 클래스를 통해서 생성을 해야 그후에가능
c2.showStatus() #변수를 생성해야지만 하는구먼
c1.run(10)
c2.run(50)

c1.showStatus()
c2.showStatus





# fuel1 = 30
# fuel2 = 20

# speed1 = 5
# speed2 = 10

# distance1 = 0
# distance2 = 0


# x = 0
# while x < 10:
#     fuel1 = fuel1 - 1 #한바퀴 돌때마다 기름 1 떨어지고 
#     distance1 = distance1 + speed1 #거리는 speed1 만큼 이동
#     x += 1

# print(f"1번 자동차는 기름이 {fuel1} 남았고, {distance1} 만큼 이동했습니다.")

