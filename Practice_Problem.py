# # 일단 for 문 사용하지 않고

# # 문1. "안녕하세요"를 5번 출력 하자

# x = 1
# while x <= 5:
#     print("안녕하세요")
#     x = x + 1

# # 문2.for 문을 이용해서 ---> while로 해보자고
# # 1부터 76까지의 합을 구하는 코드를 작성하자.

# print("문2==="*20)
# sum = 0
# for i in range(1,77) :
#     sum = sum + i
#     i += 1
# print("1~76까지더함", sum)

# # a = 1
# # sum = 0
# # while a <= 76:
# #     sum = sum + a
# #     a = a + 1

# print(sum)


# # 문3. 구구단을 출력해보자

# print("문3==="*20)

# a = 1
# while a <= 9:

#     b = 1 # 변수를 밖에다가 두었을때 b값이 초기화가 안되서 한번만 출력
    
#     while b <= 9:
#         result = a * b
#         print(f'{a} X {b} = {result}')
#         b = b + 1

#     a = a + 1

# # 문4. 구구단을 출력을 하되 7단과 6단을 제외하고 출력하자.

# print("문4==="*20)

# a = 1

# while a <= 9:
#     if a == 6 or a == 7:
#         a = a + 1
#         continue
#     b = 1

#     while b <= 9:
#         result = a * b
#         print(f'{a} X {b} = {result}')
#         b = b + 1

#     a = a + 1

# # 문5.1부터 200까지의 정수 중에서 2 또는 3의 배수가 아닌 수의 총합을 구하시오.

# print("문5==="*20)

# x = 1
# sum = 0

# while x <= 200: # 1 5 7 11 = 24

#     if not (x % 2 == 0 or x % 3 == 0):
#         sum = sum + x
#     x = x + 1

# print(sum)

# # 문6. 1+(-2)+3+(-4)+... 과 같은 식으로 계속 더해나갔을 때, 몇까지 더해야 총합이 100이상이 되는지 구하시오.

# print("문6==="*20) # 풀이 1

# a = 0
# sum = 0
# i = -1
# while sum < 100:
#     i = (i*-1)
#     a = a + 1 
#     result = i * a
#     sum = sum + result

# print(a)
# print(sum)

# print("문6==="*20) # 풀이 2

# x = 1
# sum = 0

# while True:
#     if x % 2 == 1:
#         sum = sum + x
#     else :
#         sum = sum - x
#     # x = 1 일떄 sum = 1
#     if sum >= 100:
#         break
#     x = x + 1

# print(x)
# print(sum)

# # 1부터 10까지를 곱해서 그 결과를 출력하는 프로그램을 작성하자.

# print("==="*20)

# a = 1
# sum = 1
# while a <= 10: # 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10
#     sum = sum * a
#     a = a + 1 

# print(sum) # 3628800 나와야함
# print(1*2*3*4*5*6*7*8*9*10) # ?

# # Q. for 문을 이용해서 ---> while 로 해보자~
# # 1부터 1000까지의 합을 구하는 코드를 작성하되
# # 3의 배수만 더하는 코드를 작성하자

# print("==="*20)

# a = 1 
# sum = 0

# while a <= 12: # 3 + 6 + 9 + 12 = 30
#     if a % 3 == 0:
#         sum = sum + a
#     a = a + 1

# print(sum)

# # Q.1부터 100까지 출력을 하고 난 다음에 , 
# # 다시 거꾸로 100에서부터 1까지 출력을 하는 프로그램을 작성해 보자.

# print("==="*20)

# a = 1
# while a < 100:
#     print(a)
#     a = a + 1
#  # 여기서 a = 100
# while a <= 100:
#     print(a)
#     a = a - 1
#     if a == 0:
#         break

# # Q. 자연수 1부터 시작해서 모든 홀수와 3의 배수인 짝수를 더해 나간다. 
# # 그 합이 언제(몇을 더했을 때) 1000을 넘어서는지 , 그리고 1000을 넘어선 값은 얼마가 되는지 계산하여 출력하는 프로그램을 작성해 보자.

# print("==="*20)

# a = 1
# sum = 0
# while True: # 1 + <3> + 5 + <6> + 7 + <9> + 11 + <12> = 8번째, 13더하면 55가됨? 
#     if ( a % 2 == 1 or a % 3 == 0) : # 1번째 싸이클 : 1 % 2 == 1 성립
#         sum = sum + a # 1번째 싸이클 : sum = 0 + 1, sum = 1 이됨 
#     # print(f'{a}더해서 {sum}됌')
#     a = a + 1 
#     if sum >= 1000:
#         break

# print(a-1) # 1이 한번더 더해지니까 a - 1 로 숫자를 맞춰줌
# print(sum) # 만약에 홀수 랑 3의배수인 짝수를 더하라 그러면 너무 어렵당 -- 정확하지 않음 2번나옴 <<<<<<<<<나중에 다시>>>>>>>>>

# # 1+(1+2)+(1+2+3)+(1+2+3+4)+...+(1+2+3+...+10)의 결과를 계산하시오.

# print("풀이 1 ==="*20)

# a = 1
# sum = 0
# while a <= 10:
#     # sum = sum + a # 여기서의 sum을 전부 더해야 한다 10번 , 1회차 싸이클 : sum = 0 + 1
#     # print(f'sum a안에서 = {sum}') # 1회차 싸이클 : 1출력 
#     b = 1
#     while b <= a: # 1회차 싸이클 : 0 <= 1 조건문실행
#         sum = sum + b # 1회차 싸이클 : 1 = 1 + 0
#         print(f'sum b안에서 = {sum}')
#         b = b + 1
    
#     a = a + 1
    
# print("sum 최종값 =", sum)

# print("풀이 2 ==="*20) # 변수의 적절한 활용 대충 봤음 흘겨보고 만듦

# x = 1
# sum = 0
# TempSum =0 
# while x <= 10:
#     TempSum = TempSum + x
#     print(f'TempSum = {TempSum}')
#     sum = sum + TempSum
#     print(f'sum = {sum}')
#     x = x + 1
# print(sum)

# #  Q.구구단의 짝수 단(2, 4, 6, 8단)만 출력하는 프로그램을 작성하되, 
# # 2단은 2X2까지, 4단은 4X4까지, 6단은 6X6까지 8단은 8X8까지만 출력하도록 구현하자.

# print("==="*20)

# a = 2

# while a <= 8:
#     b = 1
#     while b <= a:
#         result = a * b
#         print(f'{a} X {b} = {result}')
#         b = b + 1
#     a = a + 2

# # 피보나치(Fibonnaci) 수열(數列)은 앞을 두 수를 더해서 
# # 다음 수를 만들어 나가는 수열이다. 
# # 예를 들어 앞의 두 수가 1과 1이라면 그 다음 수는 2가 되고 
# # 그 다음 수는 1과 2를 더해서 3이 되어서 
# # 1,1,2,3,5,8,13,21,... 과 같은 식으로 진행된다. 
# # 1과 1부터 시작하는 피보나치수열의 10번째 수는 무엇인지 
# # 계산하는 프로그램을 완성하시오.

# print("==="*20)
# a = 1
# left = 1
# right = 1
# next = left + right

# while a <= 10:
#     left = right
#     right = next
#     next = left + right
#     print(f'피보나치{a+1}번째 수 : {left}')
#     a = a + 1

# # Q.863은 소수 인가? 제가 어떻게 아나요?
# # (소수는 1과 자신이외의 정수로 나누어지지 않는 수)

# print("==="*20)

# # 863은 소수인가?
# value = 2
# a = 2
# isPrime = True # 한번이라도 걸리면 False로 스위칭?
# while a < value: # 2로 나누는 이유는 속도를 빠르게 어차피 몫이 1이상이나옴 

#     if value % a == 0: # 나눴을때 목이 0 이여야 발동 , %는 나머지 구하는거.
#         isPrime = False 
#         break

#     a = a + 1

# if isPrime == True:
#     print("소수입니다")
# else :
#     print("소수가 아닙니다")

# # Q.2~100사이의 소수를 구해보자

# print("==="*20)

# num = 2
# while num <= 100:
#     count = 0  # 약수의 개수를 세어줄 변수
#     i = 1  # 1~num까지 증가할 변수
#     while i <= num:
#         if num % i == 0:  # 나누어지면 약수 1과 자기자신 이 되면 count는 2가된다.
#             count += 1
#         i += 1  # 1증가
#     if count == 2:  # 약수의 개수가 2개면 출력
#         print(f'{num}의 약수가 {count}개이므로 "소수"입니다.')
#     num += 1  # 100까지 증가

# # Q.방정식 2x+4y=10의 모든 해를 구하시오. 
# # 단, x와 y는 정수이고 각각의 범위는 0<=x<=10, 0<=y<=10 이다.
# # 실행 결과)
# # x=1, y=2
# # x=3, y=1
# # x=5, y=0

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

# print("==="*20)

# # Q.# int타입의 변수 num 이 있을 때, 각 자리의 합을 더한 결과를 출력하는 코드를 완성하라. 
# # 만일 변수 num의 값이 12345라면, ‘1+2+3+4+5’의 결과인 15를 출력하라. 
# # [주의] 문자열로 변환하지 말고 숫자로만 처리해야 한다.
# # (API를 사용하지 않는다. 알고리즘으로만 처리)

# num = 234
# c = 0
# while (True): ## 변수값을 어케 저장하지?
#     a = num % 10 # a = 4 / a = 3 / a = 1
#     b = num // 10 # b = 13 / b = 1 / b = 0
#     num = b # num = 13 / num = 1 / num = 0
#     c = c + a # c = 4 / c = 7 / c = 8
#     # a값을 저장해서 출력하고 싶은데
#     if ( num <= 0):
#         break
# print(f'입력하신 각 자릿수의 합은 {c} 입니다.')

# print("==="*20)

# # 1~10000사이에 8이 몇번 나오는가?
# # 정답 ) 4000
# # 힌트 ) 8838 = 3개...d

# start = 1
# end = 10000
# count = 0
# var = 0

# while start <= end: # 8,18,28,38,48,58,68,78,98, + 80,81,82,83,84,85,86,87,88,89
#     var = start
#     while True:
#         if var % 10 == 8:
#             count += 1
#         var = var // 10
#         if var <= 0:
#             break
#     start += 1

# print(count)

# 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에 출력해보자. 1부터 시작하며 99까지만 한다. 

# 실행 결과 예)           
# 3 박수한번
# 6 박수 한번
# 9 박수 한번 
# .
# .
# .
# 33 박수 두번
# .
# 98 박수 한번
# 99 박수 두번

# i = 1
# # count = 1
#  #       if not ((i % 10 == 3 or i % 10 ==6 or i % 10 == 9) and (i // 10 == 3 or i // 10 == 6 or i // 10 == 9)):    
# while (True):
#     if ((i % 10 == 3 or i % 10 ==6 or i % 10 == 9)): # 10의로 나눴을때 나머지가 3인수를 전부 출력 + 30 ~ 39 까지 33,36,39 제외,
#         print(f'{i} 박수한번')
#         # count += 1
#         if ( (i // 10 == 3 or i // 10 == 6 or i // 10 == 9)): ## 33,36,39,63,66,69,93,96,96 에서 중복발생
#             # count += 2
#             print(f'{i} 박수두번')
#             # count = 0
#     if ( i == 100):
#         break
#     i = i + 1



# 풀이 2 실험중
# i = 3
# count = 0
# while ( i <= 99 ):   ## 3,6,9,13, 16, 19 한번 , 23, 26, 29 한번 , 30,31,32,,33,,34,35,,36,,37,38,39
#                     ## 33,36,39번대 63,66,69번대 93,96,99번대 에서 3의 배수면 2번침 -> 30의 배수이면서 3의 배수면 두번
#                     ## 11*3,2*2*3*3,13*3 / 3*3*7,11*3*2,23*3 / 31*3,3*2*2*2*2*2, 3*3*11
#                     ## 더하기로 하면 3더했을
#                     ## 나머지는 다한번

#     while ( i <= 99 ):
#         print(f'{i} 박수 한번') # 3 박수한번 # 6 박수한번 #  9박수 반번 
#         count += 1              # 카운트 1  # 카운트 2 # 카운트 3 
#         if (count == 3):        # 카운트 3
#             i += 4              # 13 
#             count = 0           # 카운트 0
#         if not( count != 0):
#             i += 3                  # 17





#     i += 1

# Q.<문제> 거스름 돈: 문제 설명
# 당신은 음식점의 계산을 도와주는 점원입니다. 
# 카운터에는 거스름돈으로 사용할 500원, 100원, 50원,10원짜리 동전이 
# 무한히 존재한다고 가정합니다. 
# 손님에게 거슬러 주어야 할 돈이 N원일 때 거슬러 주어야 할 동전의 최소 개수를 구하세요. 
# 단, 거슬러 줘야 할 돈 N은 항상 10의 배수입니다.
# n = 14870 # n = 1870 , 500*3 + 100*3 + 50*1 + 10*2
# count1 =0
# count2 =0
# count3 =0
# count4 =0
# if ((n // 10) >= 1):
#     if ((n // 500) >= 1): # 500원 짜리 동전 거스름
#         won500 = n // 500    # won500 = 1870 // 500 = 3
#         count1 = won500 # count = 3
#         price1 = n - 500*count1 # price1 = 1870 - 500*3 == 370
#         if((price1 // 100) >= 1): # price1 = 370
#             won100 = price1 // 100 # won100 = 3
#             count2 = won100 # count = 3
#             price2 = price1 - 100*count2 # price2 = 370 - 100 *3 = 70
#             if((price2 // 50) >= 1): #price2 = 70
#                 won50 = price2 // 50 # won50 = 1
#                 count3 = won50 # count# = 1
#                 price3 = price2 - 50*count3 # price3 = 70 - 50 = 20
#                 if((price3 // 10) >=1): 
#                     won10 = price3 // 10 # won10 = 2
#                     count4 = won10 # count = 2
#                     price4 = price3 - 10*count4 #price4 = 20 - 20
# print(f'{n}원의 거스름돈을 계산합니다.')
# print(f'500원짜리 동전: {count1}')
# print(f'100원짜리 동전: {count2}')
# print(f'50원짜리 동전: {count3}')
# print(f'10원짜리 동전: {count4}')
# print(f'거슬러 주어야할 최소 동전의 개수는 {count1+count2+count3+count4}개 입니다.')


# Q.<문제> 1이 될 때까지: 문제 설명
# • 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 합니다. 
# 단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있습니다.
# 1. N에서 1을 뺍니다.
# 2. N을 K로 나눕니다.
# • 예를 들어 N이 17, K가 4라고 가정합시다. 
# 이때 1번의 과정을 한 번 수행하면 N은 16이 됩니다. 
# 이후에 2번의 과정을 두 번 수행하면 N은 1이 됩니다. 
# 결과적으로 이 경우 전체 과정을 실행한 횟수는 3이 됩니다. 
# 이는 N을 1로 만드는 최소 횟수입니다.
# • N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 
# 최소 횟수를 구하는 프로그램을 작성하세요.

# 입력 조건 : 1 <= N <= 100000 , 2 <= K <= 100000 , N과 K는 자연수

# n = 17
# k = 4
# count = 0
# while True:
#     if not ( (n % k) == 0 ): # 17 % 4 == 1 False # 16 % 4 == 0 True 실행X
#         n = n - 1 # n = 17 - 1 = 16 
#         count += 1 # count = 1
#     elif ( n % k == 0):
#         n = n // k # n = 16 // 4 = 4 
#         count += 1
#     if ( n <= 1):
#         break

# print(f'최소 횟수 = {count}') # 17- 1 -> 16, 16 // 4 -> 4 

# Q.시각
# • 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는
# 모든 경우의 수를 구하는 프로그램을 작성하세요. 예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되
# 어 있으므로 세어야 하는 시각입니다.
#    • 00시 00분 03초
#    • 00시 13분 30초
# • 반면에 다음은 3이 하나도 포함되어 있지 않으므로 세면 안 되는 시각입니다.
#    • 00시 02분 55초
#    • 01시 27분 45초
start = 0
end = 0
minute = 0
while ( start <= end ): # 0 <= 0 실행
    minute = 0
    while (minute <= 59): # minute = 0 실행
        second = 0
        while (second<= 59): # second = 0 실행
            if (second % 10 == 3 or ((second >= 30) and (second <= 39))):
                print(f'0{start}시 {minute}분 {second}초') #각 조건에 맞게 출력
            second += 1    
        minute += 1
    start += 1

# • 각 자리가 숫자(0부터 9)로만 이루어진 문자열 S가 주어졌을 때, 
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 
# 숫자 사이에 ‘×’ 혹은 ‘+’ 연산자를 넣어 결과적으로 만들어질 수 있는 
# 가장 큰 수를 구하는 프로그램을 작성하세요. 
# 단, +보다 ×를 먼저 계산하는 일반적인 방식과는 달리, 
# 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정합니다.
# • 예를 들어 02984라는 문자열로 만들 수 있는 가장 큰 수는 
# ((((0 + 2) × 9) × 8) × 4) = 576입니다. 
# 또한 만들어질 수 있는 가장 큰 수는 항상 20억 이하의 정수가 되도록 입력이 주어집니다.

# string = "1312" # 가장큰값 (1 + 3 + 1) * 2 , 2 1 3 1 
# # num = int(string[::-1])
# # print(num)
# num = int(string)
# c = 0
# while (True): ## 변수값을 어케 저장하지?
#     a = num % 10  # a = 1312 % 10 = 2 / 
#     b = num // 10 # 2131 // 10 = 213
#     num = b       # 1312
#     if ( a == 1): 
#         c = c + a 
#     elif ( a >= 2):  
#         c = c * a 
#     print(a) 
#     if ( num <= 0): 
#         break
# print(f'입력하신 각 자릿수의 합은 {c} 입니다.')


# string = "00345" ## 여기서 0이 있으면 +, 없으면 x, 값 16이 나와야함
# converted = int(string)
# numberCalculated = []
# i = 10
# calculated = 0
# sum = 0
# while (sum <= 2000000000):
#     calculated = converted % 10  # calculated = 345 % 10 = 5
#     numberCalculated.append(calculated)
#     print(numberCalculated)
#     converted = calculated // 10
#     break
#     # i = string * 10



# scores = []

# scores.append(10) 
# scores.append(50)
# scores.append(30)

# print(scores) # [10, 50, 30]

# for x in scores:
#     print(x)