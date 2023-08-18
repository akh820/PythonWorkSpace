# 반복문에는 continue, break란 키워드가 있다...

a = 10
while True:
    print("안녕하세요")
    a = a + 1
    if a > 15: #break 문은 무조건 if이랑 같이감
        break

print("==="*20)

a = 10
while a <= 15:
    print("안녕하세요")
    a = a + 1

print("==="*20)

a = 0
sum = 0
while a <= 10 : # <1> <5>
    a = a + 1 # <2> <6>

    if a % 2 != 0 : # <3> <7>
        continue # <4> <8>조건에 맞으면 더이상 실행 시키지 않고 위로 가서
                 # 조건확인  
                 # break문은 탈출

    sum = sum + a # <9>

