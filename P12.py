# 어떤 책에서도 나오는예제
# 1부터 10까지의 합을 구해보자

value1 = input("첫번째값을 입력하세요 : ") # input() = API
value2 = input("두번째값을 입력하세요 : ") # input()입력값은 무조건 문자이다
value1 = int(value1)
value2 = int(value2)

a = value1
k = value2

sum = 0

# 짝수의 합만 구하고 싶다면?

while a <= k:
    if a % 2 == 0 : #짝수계산
        sum = sum + a # =은 항상 마지막에 연산이 된다.
        print("a =",a,"sum =",sum)
    a = a + 1

print(f'{a}가 {k}를 넘었으니까 실행을 종료합니다')     

print(f'{value1} 부터 {value2} 까지의 합은 {sum} 입니다')

# CTRL + SHIFT + L 로 단어 한번에, 
# 선택된 부분 아래로 ctrl + d로 하나씩 선택