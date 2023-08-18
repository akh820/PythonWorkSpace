# 어떤 책에서도 나오는예제
# 1부터 10까지의 합을 구해보자

a = 0
sum = 0

while a <= 100:
    print("a =",a,"sum =",sum)
    sum = sum + a # =은 항상 마지막에 연산이 된다.
    a = a + 1 

print(f'1부터 10까지의 합은 {sum} 입니다')