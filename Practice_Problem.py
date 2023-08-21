# 일단 for 문 사용하지 않고

# 문1. "안녕하세요"를 5번 출력 하자

x = 1
while x <= 5:
    print("안녕하세요")
    x = x + 1

# 문2.for 문을 이용해서 ---> while로 해보자고
# 1부터 76까지의 합을 구하는 코드를 작성하자.

print("문2==="*20)
sum = 0
for i in range(1,77) :
    sum = sum + i
    i += 1
print("1~76까지더함", sum)

# a = 1
# sum = 0
# while a <= 76:
#     sum = sum + a
#     a = a + 1

print(sum)


# 문3. 구구단을 출력해보자

print("문3==="*20)

a = 1
while a <= 9:

    b = 1 # 변수를 밖에다가 두었을때 b값이 초기화가 안되서 한번만 출력
    
    while b <= 9:
        result = a * b
        print(f'{a} X {b} = {result}')
        b = b + 1

    a = a + 1

# 문4. 구구단을 출력을 하되 7단과 6단을 제외하고 출력하자.

print("문4==="*20)

a = 1

while a <= 9:
    if a == 6 or a == 7:
        a = a + 1
        continue
    b = 1

    while b <= 9:
        result = a * b
        print(f'{a} X {b} = {result}')
        b = b + 1

    a = a + 1

# 문5.1부터 200까지의 정수 중에서 2 또는 3의 배수가 아닌 수의 총합을 구하시오.

print("문5==="*20)

x = 1
sum = 0

while x <= 200: # 1 5 7 11 = 24

    if not (x % 2 == 0 or x % 3 == 0):
        sum = sum + x
    x = x + 1

print(sum)

# 문6. 1+(-2)+3+(-4)+... 과 같은 식으로 계속 더해나갔을 때, 몇까지 더해야 총합이 100이상이 되는지 구하시오.

print("문6==="*20) # 풀이 1

a = 0
sum = 0
i = -1
while sum < 100:
    i = (i*-1)
    a = a + 1 
    result = i * a
    sum = sum + result

print(a)
print(sum)

print("문6==="*20) # 풀이 2

x = 1
sum = 0

while True:
    if x % 2 == 1:
        sum = sum + x
    else :
        sum = sum - x
    # x = 1 일떄 sum = 1
    if sum >= 100:
        break
    x = x + 1

print(x)
print(sum)

# 1부터 10까지를 곱해서 그 결과를 출력하는 프로그램을 작성하자.

print("==="*20)

a = 1
sum = 1
while a <= 10: # 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10
    sum = sum * a
    a = a + 1 

print(sum) # 3628800 나와야함
print(1*2*3*4*5*6*7*8*9*10) # ?

# Q. for 문을 이용해서 ---> while 로 해보자~
# 1부터 1000까지의 합을 구하는 코드를 작성하되
# 3의 배수만 더하는 코드를 작성하자

print("==="*20)

a = 1 
sum = 0

while a <= 12: # 3 + 6 + 9 + 12 = 30
    if a % 3 == 0:
        sum = sum + a
    a = a + 1

print(sum)

# Q.1부터 100까지 출력을 하고 난 다음에 , 
# 다시 거꾸로 100에서부터 1까지 출력을 하는 프로그램을 작성해 보자.

print("==="*20)

a = 1
while a < 100:
    print(a)
    a = a + 1
 # 여기서 a = 100
while a <= 100:
    print(a)
    a = a - 1
    if a == 0:
        break

# Q. 자연수 1부터 시작해서 모든 홀수와 3의 배수인 짝수를 더해 나간다. 
# 그 합이 언제(몇을 더했을 때) 1000을 넘어서는지 , 그리고 1000을 넘어선 값은 얼마가 되는지 계산하여 출력하는 프로그램을 작성해 보자.

print("==="*20)

a = 1
sum = 0
while True: # 1 + <3> + 5 + <6> + 7 + <9> + 11 + <12> = 8번째, 13더하면 55가됨? 
    if ( a % 2 == 1 or a % 3 == 0) : # 1번째 싸이클 : 1 % 2 == 1 성립
        sum = sum + a # 1번째 싸이클 : sum = 0 + 1, sum = 1 이됨 
    # print(f'{a}더해서 {sum}됌')
    a = a + 1 
    if sum >= 1000:
        break

print(a-1) # 1이 한번더 더해지니까 a - 1 로 숫자를 맞춰줌
print(sum) # 만약에 홀수 랑 3의배수인 짝수를 더하라 그러면 너무 어렵당 -- 정확하지 않음 2번나옴 <<<<<<<<<나중에 다시>>>>>>>>>

# 1+(1+2)+(1+2+3)+(1+2+3+4)+...+(1+2+3+...+10)의 결과를 계산하시오.

print("풀이 1 ==="*20)

a = 1
sum = 0
while a <= 10:
    # sum = sum + a # 여기서의 sum을 전부 더해야 한다 10번 , 1회차 싸이클 : sum = 0 + 1
    # print(f'sum a안에서 = {sum}') # 1회차 싸이클 : 1출력 
    b = 1
    while b <= a: # 1회차 싸이클 : 0 <= 1 조건문실행
        sum = sum + b # 1회차 싸이클 : 1 = 1 + 0
        print(f'sum b안에서 = {sum}')
        b = b + 1
    
    a = a + 1
    
print("sum 최종값 =", sum)

print("풀이 2 ==="*20) # 변수의 적절한 활용 대충 봤음 흘겨보고 만듦

x = 1
sum = 0
TempSum =0 
while x <= 10:
    TempSum = TempSum + x
    print(f'TempSum = {TempSum}')
    sum = sum + TempSum
    print(f'sum = {sum}')
    x = x + 1
print(sum)

#  Q.구구단의 짝수 단(2, 4, 6, 8단)만 출력하는 프로그램을 작성하되, 
# 2단은 2X2까지, 4단은 4X4까지, 6단은 6X6까지 8단은 8X8까지만 출력하도록 구현하자.

print("==="*20)

a = 2

while a <= 8:
    b = 1
    while b <= a:
        result = a * b
        print(f'{a} X {b} = {result}')
        b = b + 1
    a = a + 2

# 피보나치(Fibonnaci) 수열(數列)은 앞을 두 수를 더해서 
# 다음 수를 만들어 나가는 수열이다. 
# 예를 들어 앞의 두 수가 1과 1이라면 그 다음 수는 2가 되고 
# 그 다음 수는 1과 2를 더해서 3이 되어서 
# 1,1,2,3,5,8,13,21,... 과 같은 식으로 진행된다. 
# 1과 1부터 시작하는 피보나치수열의 10번째 수는 무엇인지 
# 계산하는 프로그램을 완성하시오.

print("==="*20)
a = 1
left = 1
right = 1
next = left + right

while a <= 10:
    left = right
    right = next
    next = left + right
    print(f'피보나치{a+1}번째 수 : {left}')
    a = a + 1

# Q.863은 소수 인가? 제가 어떻게 아나요?
# (소수는 1과 자신이외의 정수로 나누어지지 않는 수)

print("==="*20)

# 863은 소수인가?
value = 2
a = 2
isPrime = True # 한번이라도 걸리면 False로 스위칭?
while a < value: # 2로 나누는 이유는 속도를 빠르게 어차피 몫이 1이상이나옴 

    if value % a == 0: # 나눴을때 목이 0 이여야 발동 , %는 나머지 구하는거.
        isPrime = False 
        break

    a = a + 1

if isPrime == True:
    print("소수입니다")
else :
    print("소수가 아닙니다")

# Q.2~100사이의 소수를 구해보자

print("==="*20)

num = 2
while num <= 100:
    count = 0  # 약수의 개수를 세어줄 변수
    i = 1  # 1~num까지 증가할 변수
    while i <= num:
        if num % i == 0:  # 나누어지면 약수
            count += 1
        i += 1  # 1증가
    if count == 2:  # 약수의 개수가 2개면 출력
        print(f'{num}의 약수가 {count}개이므로 "소수"입니다.')

    num += 1  # 100까지 증가

# Q.방정식 2x+4y=10의 모든 해를 구하시오. 
# 단, x와 y는 정수이고 각각의 범위는 0<=x<=10, 0<=y<=10 이다.
# 실행 결과)
# x=1, y=2
# x=3, y=1
# x=5, y=0

# print("==="*20)

# x = 0

# while x <= 10:
    
#     y = 0
#     # print(f'현재 X의 값 : {x}')
#     while y <= 10:
#         result = (2*x) + (4*y)
#         # print(f'현재 y의 값 : {y}')
#         # print(f'result 의 값 : {result}')
#         if result == 10:
#             print(f'x={x}, y={y}')
#         y = y + 1
#     x = x + 1

# Q.# int타입의 변수 num 이 있을 때, 각 자리의 합을 더한 결과를 출력하는 코드를 완성하라. 
# 만일 변수 num의 값이 12345라면, ‘1+2+3+4+5’의 결과인 15를 출력하라. 
# [주의] 문자열로 변환하지 말고 숫자로만 처리해야 한다.
# (API를 사용하지 않는다. 알고리즘으로만 처리)

# print("==="*20)

# 1~10000사이에 8이 몇번 나오는가?
# 정답 ) 4000
# 힌트 ) 8838 = 3개...

    

