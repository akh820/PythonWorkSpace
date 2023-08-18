# 영어 알파벳으로 이루어진 문자열 str이 주어집니다. 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.

# 제한사항
# 1 ≤ str의 길이 ≤ 20
# str은 알파벳으로 이루어진 문자열입니다.
# str = input()

str = input()
swapped_str = str.swapcase()
upper_str = str.upper()
lower_str = str.lower()
capitalized_str = str.capitalize()
print(swapped_str)
print(upper_str)
print(lower_str)
print(capitalized_str)

# upper() - > 전부 대문자 변경, lower() - > 전부 소문자 변경 swapcase() - > 대소문자 바꿈 capitalize() - > 맨앞만 대문자