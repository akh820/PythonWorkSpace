print("==="*20)
print(r'5. 1부터 200까지의 정수 중에서 2 또는 3의 배수가 아닌 수의 총합을 구하시오.')
print("답)")
i = 1
sum = 0
while i <= 200: # 1, 2, 3, 4, 5, 6, 7, 8, 9 ,10 -> 1+5+7 = 13
    if not (i % 2 == 0 or i % 3 == 0):
        sum += i
    i += 1
print(sum)
print("==="*20)