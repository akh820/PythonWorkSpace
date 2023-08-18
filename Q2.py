# 구구단을 출력하되 6단과 7단을 제외하고 출력하자.

a = 2 # if not()

while a <= 9 :
    if a == 6 or a ==7:
        a = a + 1
        continue # 예외처리하겠다

    b = 1
    while b <= 9:        # break 가장 가까이에서 돌고있는 while문을 탈출한다
        result = a * b
        print(f'{a} X {b} = {result}')
        b = b + 1

    a = a + 1

# 드래그 하고 Tab으로 밀기, Shift + Tap으로 끌어오기