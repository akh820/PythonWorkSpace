# 배열 (자료구조...)
# 배열을 쓴다? -> 순서가 있다 == 반복문을 쓴다.

scores = [50, 60, 70, 80, 90] # 초기화값이라 별로 쓸일이 없음  
                              # 대부분의 언어에서 []은 배열을 의미함
index = 0
while index < 5:
    print(scores[index])
    index = index + 1

#파이썬 에서의 반복문은 foreach, 고전적 for문 아님
for e in scores: #여기서 e는 변수
    print(e) # 순차적으로 안에있는걸 전부 출력

# score1 = 10
# score2 = 10
# score3 = 10
# score4 = 10
# score5 = 10

# print(score1)
# print(score2)
# print(score3)
# print(score4)
# print(score5)