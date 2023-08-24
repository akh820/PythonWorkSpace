
start = 2
end = 100
count = 0
 
# 2부터 100사이의 소수 출력
# 소수 판별조건 자기자신 % 1 == 0, 
while( start <= end): # start = 2
    check = 1
    count = 0
     # check = 1
    while (check <= start):    # 1 < =2 로 실행 # 2 <= 2로 실행 / 3 <= 2 므로 실행x
        if (start % check ==0): # 2 % 1 == 0 # 2 % 2 == 0 으로 실행
            count += 1 # count = 1 / count = 2
        check += 1 #check = 
    if (count ==2):
        print(start) # 2를 출력

    start += 1