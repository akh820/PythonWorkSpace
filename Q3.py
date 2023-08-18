# 1+(-2)+3+(-4)+... 과 같은 식으로 계속 더해나갔을 때, 몇까지 더해야 총합이 100이상이 되는지 구하시오.
# 1번 방법
x = 1
sum = 0 

while True:
    if x % 2 == 1:
        sum = sum + x
    else :
        sum = sum - x

    if sum >= 100:
        break

    x = x + 1

print(x)
print(sum)  

print("==="*20)

# 내 방법 -> 사실 의미가 없다. 이런식으로 할거면 뭘해도 이렇게할수있을듯;

# 2번방법, 스위칭 변수 (껐다,켰다)

x = 0
sum = 0
i = -1 # 스위칭 변수
while sum < 100:
    i = i * -1
    x = x + 1
    sum = sum + (x * i) # ()우선순위 높임

print(x)
print(sum)