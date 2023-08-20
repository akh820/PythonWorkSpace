print("==="*20)
print(r'1. "안녕하세요"를 5번 출력 하자"')
print("답)")
i = 1

while i <= 5:
    print("안녕하세요")
    i += 1
print("==="*20)

print(r'2. for 문을 이용해서  1부터 76까지의 합을 구하는 코드를 작성하자.')
print("답)")

i = 1
sum = 0
for i in range(1,77):
    sum += i
    i += 1
print(sum)
print("==="*20)
print(r'3.구구단을 출력해보자')
print("답)")

a = 1
while a <= 9:
    print(f'{a}단')
    b = 1
    while b <= 9:
        result = a * b
        print(f'{a} X {b} = {result}')
        b += 1
    a += 1

print("==="*20)
print(r'4. 구구단을 출력을 하되 6단과 7단을 제외하고 출력하자.')
print("답)")
a = 1
while a <= 9:
    b = 1
    while b <= 9:
        if not ( a == 6 or a == 7):
            result = a * b
            print(f'{a} X {b} = {result}')
        b += 1
    a += 1

print("==="*20)
print(r'5. 1부터 200까지의 정수 중에서 2 또는 3의 배수가 아닌 수의 총합을 구하시오.')
print("답)")
i = 1
sum = 0
while i <= 10: # 1, 2, 3, 4, 5, 6, 7, 8, 9 ,10 -> 1+5+7 = 13
    if not (i % 2 == 0 or i % 3 == 0):
        sum += i
    i += 1
print(sum)
print("==="*20)

print(r'6. 1+(-2)+3+(-4)+... 과 같은 식으로 계속 더해나갔을 때, 몇까지 더해야 총합이 100이상이 되는지 구하시오.')
print("답)")
x = 1
i = -1
sum = 0 
while True: # 4항까지 의 합 = -2
    i = i*(-1)
    result = x * i
    # print(f'{x}번째 항의 값 :', result)
    sum = sum + result
    # print(f'{x}번쨰 항까지의 합', sum)
    if sum >= 100:
        print(f'{x}번 째 항에서 합의값은 100이상이 됩니다. 합의값 : {sum}')
        break
    x += 1

# Q.
# 1부터 10까지를 곱해서 그 결과를 출력하는 프로그램을 작성하자.

# Q. 
# for 문을 이용해서 
# 1부터 1000까지의 합을 구하는 코드를 작성하되
# 3의 배수만 더하는 코드를 작성하자

# Q.
# 1부터 100까지 출력을 하고 난 다음에 , 
# 다시 거꾸로 100에서부터 1까지 출력을 하는 프로그램을 작성해 보자.

# Q.
# 자연수 1부터 시작해서 모든 홀수와 3의 배수인 짝수를 더해 나간다. 
# 그 합이 언제(몇을 더했을 때) 1000을 넘어서는지 , 그리고 1000을 넘어선 값은 얼마가 되는지 계산하여 출력하는 프로그램을 작성해 보자.

# Q.
# 1+(1+2)+(1+2+3)+(1+2+3+4)+...+(1+2+3+...+10)의 결과를 계산하시오.

# Q.
# 구구단의 짝수 단(2, 4, 6, 8단)만 출력하는 프로그램을 작성하되, 
# 2단은 2X2까지, 4단은 4X4까지, 6단은 6X6까지 8단은 8X8까지만 출력하도록 구현하자.

# Q.
# 피보나치(Fibonnaci) 수열(數列)은 앞을 두 수를 더해서 
# 다음 수를 만들어 나가는 수열이다. 
# 예를 들어 앞의 두 수가 1과 1이라면 그 다음 수는 2가 되고 
# 그 다음 수는 1과 2를 더해서 3이 되어서 
# 1,1,2,3,5,8,13,21,... 과 같은 식으로 진행된다. 
# 1과 1부터 시작하는 피보나치수열의 10번째 수는 무엇인지 
# 계산하는 프로그램을 완성하시오.

# Q.
# 863은 소수 인가?
# (소수는 1과 자신이외의 정수로 나누어지지 않는 수)

# Q.
# 2~100사이의 소수를 구해보자

# Q.
# 방정식 2x+4y=10의 모든 해를 구하시오. 
# 단, x와 y는 정수이고 각각의 범위는 0<=x<=10, 0<=y<=10 이다.
# 실행 결과)
# x=1, y=2
# x=3, y=1
# x=5, y=0
# [출처] 연습 문제|작성자 s001lec
