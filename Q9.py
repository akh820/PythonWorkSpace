# 1-10000사이에 8이 몇번나오는가?

start = 1
end = 10000
value = start
count = 0

while value <= end:
    temp = value # 오염되지 않는 변수값
    while True:
        if temp % 10 == 8:
            count += 1
        temp = temp // 10
        if temp == 0:
            break



    value += 1

print(count)