# 863은 소수인가?
value = 863
a = 2
isPrime = True # 한번이라도 걸리면 False로 스위칭?
while a < value: 

    if value % a==0:
        isPrime = False
        break

    a = a + 1

if isPrime == True:
    print("소수입니다")
else :
    print("소수가 아닙니다")