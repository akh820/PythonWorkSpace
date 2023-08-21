# 클래스 생성 Car
# 구현해야할것 : 함수 showStatus(현재 상태 보여줌), run
# self, name, fuel ,speed, distance

class Car:
    def __init__(self, name, fuel, speed, distance):
        self.name = name
        self.fuel = fuel
        self.speed = speed
        self.distance = distance

    def showStatus(self):
        print(f'{self.name}, 남은 연료 : {self.fuel}, 속도 : {self.speed}, 이동거리 : {self.distance}')
    def run(self, count):
        x = 1
        while x <= count:
            self.fuel -= 1
            self.distance += self.speed
            if self.fuel <= 0:
                print(f'{self.name}가 연료부족!!!')
                break
            x += 1

c1 = Car("1번 자동차", 20, 5, 0)
c2 = Car("2번 자동차", 30, 15,0)

c1.showStatus()
c2.showStatus()

c1.run(10)
c2.run(50)

c1.showStatus()
c2.showStatus()
