# 비교 연산자 2
a = 10 > 1 # 10이 1보다 크나?
print("10 > 1 값은?", a)
a = 10 < 1 
print("10 < 1 값은?", a)

b = 10 == 15 # 10은 15랑같냐?
print(b)

c = 10 != 15 # 10은 15랑 같지 않다
print(c)

value = 7
result = value % 2 == 0 # 나머지가 0이다 ==짝수, 나머지가 1이다 ==홀수

print(result) # True = 짝수, False = 홀수

a = 15
b = 10

result = a > 10 and b < 5 # 참고로 이상이하는 >=,<=
print(result)
result = a > 10 or b < 5
print(result)

