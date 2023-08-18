# 구구단을 출력해보자.

a = 2

while a <= 9:

    b = 1

    while b <= 9:
        result = a * b
        print(f'{a} X {b} = {result}')
        b = b + 1

    a = a + 1 