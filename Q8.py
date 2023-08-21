# 863은 소수인가?
value = 400
a = 2
isPrime = True # 한번이라도 걸리면 False로 스위칭?
while a < value: # 2로 나누는 이유는 속도를 빠르게 어차피 몫이 1이상이나옴 

    if value % a == 0: #소수를 판별하는 
        isPrime = False
        break

    a = a + 1

if isPrime == True:
    print("소수입니다")
else :
    print("소수가 아닙니다")