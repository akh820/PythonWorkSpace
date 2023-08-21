# 설계 문법 - 함수, 클래스 (좋은 코드를 만드는 기법, 정답이 없다)

# 함수 선언 -> !!! 코드를 읽을때 def로 가고 불러오는 식으로 이해를해야한다.
# 코드의 흐름을 놓치지 말자
def gugudan(start, end):        
    x = start
    while x <= end:
        y = 1
        while y <= 9:
            print(f'{x} X {y} = {x * y}')
            y += 1
        x += 1

gugudan(1,4)