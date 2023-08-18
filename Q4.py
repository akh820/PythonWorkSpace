# 1+(1+2)+(1+2+3)+(1+2+3+4)+...+(1+2+3+...+10)의 결과를 계산하시오.

# 첫번째 방법 - 문제풀이 그대로 이중 while문(like구구단)

x = 1
sum = 0
while x <= 10:
    

    y = 1
    while y <= x:
        sum = sum + y


        y = y + 1

    x = x + 1

print(sum)

print("===" * 20)

# 두번째 방법 - 변수의 적절한 활용 방법

x = 1
sum = 0
TempSum = 0 
while x <= 10: # 한바퀴 돌때 마다 메모리의 변화를 알아야함

    TempSum = TempSum + x
    sum = sum + TempSum
    x = x + 1

print(sum)

print("===" * 20)


# 마지막 방법 - 문제의 재구성(아이디어 측면, 정답으로써는 의미 X)

x = 1
sum = 0 
while x <= 10:

    sum = sum + (x * (11-x))
    x = x + 1

print(sum)