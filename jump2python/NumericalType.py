a = 123
print(a)
a = 4.24e10 # 4.24*10의 10승 , 4.24e-10 은 4.24 * 10의 -10승
print(a)

A = 10*18**2+2*11 # 여기서 **은 제곱을 나타낸다 2**7은 2^7
print("10x18^2+2*11", A)

# 14나누기 3 했을때 몫과 나머지를 표기해라
print(14 // 3, 14 % 3)

#"'Python is vey easy.'he says."

print("나\"는\"이상해") # 안에 따옴표를 쓰고싶을때는 \" or \' 를 사용한다
print('나\'는\'이상해') 
print('나는\\이상해') # \\를통해서 \사용가능

print("Life is too short\nYou need Python") # \n을 사용해서 이스케이프

abc = '''
Life is too short
You need python
understand?
'''

print(abc)

head = "Python"
tail = " is fun!"
print(head + tail)

print(head*2) # 문자열에서 곱해서 반복 표현도 가능

Q = "Life\nis too short, You need Python" #여기서 \n은 자리를 잡아 먹지 않는다 
#   "0123456789"
print(len(Q)) # print를 써줘서 표현
print(Q[6]) # 앞에서 6번째
print(Q[-1]) # 뒤에서 첫번째
print(Q[0:4]) # 0,1,2,3 을 불러온다. 즉, Q[0:4] = 0 <= Q < 4 # 끝이 0이라 아예 불러오지 않음
print("=="*20)
print(Q[19:]) # 19부터 끝까지
print(Q[:17]) # 처음부터 17까지
print(Q[19:-7]) # 19부터 뒤에서 7번째까지

#거꾸로 슬라이싱
print("=="*20)
W = "20230331Rainy"
date = W[:8]
weather = W[8:]
print(date + weather)

#문자열 포맷팅
print("=="*20)
E = "I eat %d apples." %3 # %d는 정수, %f는 부동소수
print(E)
E = "I eat %s apples." %"five" # %s는 문자, %s 는 자동으로 뒤에있는 것을 문자열로 바꾸어 대입한다
# 그러므로 숫자든, 문자든 둘다 대입가능 (하지만 나중에 계산 같은거 하게 되면 계산이 안될듯?, 근데 생각해보니 문자열에서만 쓰니까 더할일이 없을듯)
print(E)
number = 4
E = "I eat %d apples." %number
print(E)
days = 3
E = "I ate %d apples. so I was sick for %s days." %(10, days)
print(E)
E = "Error is %f%%" %98.88 # 만약에 %를 사용하고 싶다면 %%를 사용하도록 하자
print(E)
# E = "아오 %s 시치, %s 하는거야" %"페리" %시치 -----------> 한문장에서 %s 두번사용은 안되네?
# print(E)

#포맷 코드와 숫자 함께 사용하기
print("=="*20)
a = "%10s"  %"hi" # 전체길이 10개에서 오른쪽정렬로 hi를 집어넣음 0,1,2,3,4,5,6,7,h(8),i(9) 가 된다
print(a) 
a = "%-10sjane" %"hi" # 왼쪽정렬
print(a)

#소수점 표현하기
a = "%0.4f" % 3.42134234 # %.4f 로도 사용가능, 소수점 4번째까지 자리만 표기해겠다.
print(a)
a = "%10.4f" % 3.421
print(a)

# 숫자 바로 대입하기
print("=="*20)
a = "I eat {0} apples".format(3) # 숫자 바로 대입
print(a)
a = "I eat %d apples" %3 #무슨 차이? 자주 안쓰는 방식? 
print(a)
number = 3
days = "Tommorow"
a = "I eat {0} apples. but i can't eat {1} apples. if {2} is coming, I want to eat {3} apples" .format(number, 2, days, 5) # 순서대로간다
print(a)
a = "I ate {number} apples. so I was sick for {day} days.".format(number = 3, day = 3) # .format()안에 있는 변수지정
print(a)

#정렬
print("=="*20)
a = "{0:<10}".format("hi") # 크기 10에서 왼쪽정렬
print(a)
a = "{0:>10}".format("hi") # 오른쪽정렬
print(a)
a = "{0:^10}".format("hi") # 가운데 정렬
print(a)
a = "{0:は^10}".format("hi") # ?? 5로도 정렬이되네? ㄷ으로도 정렬이되네?　は로도 정렬이되네?
print(a)

#소수점 표현하기
y = 3.42134234
a = "아{0:10.4f}아".format(y) # 열자리 맞추고 소수점 4자리까지
print(a)

#문자 표현
a = "{{ and }}".format() # 이거 중괄호 밖에 안되서 사용빈도가 적을듯?
print(a)

#f문자열 포맷팅
print("=="*20)
name = "홍길동"
age = 30
a = f"나의 이름은 {name}입니다. 나이는 {age} 입니다"
print(a)
a = f"나의 나이는 {age+1} 이다"
print(a)
d = {"name": "안계홍", "age": 35} # 흠 책이랑 다름, 여기서는 dictinary는 큰따옴표, 사용할때는 ''로 묶어야 에러가 없다.
a = f"내 이름은 {d['name']} 이고, 나이는 {d['age']} 가 됐다"
print(a)
print(f'{"hi":<10}끝') # f로 열때는 ''작은 따옴표를 써야 오류가 없네?
print(f'시작{"hi":>10}') # 오른쪽 정렬
print(f'시작{"hi":^10}끝') # 가운데 정렬
print(f'{"hi":아^10}') # 
y = 3.42134234
print(f'{y:0.4f}') 

# format 함수 or f 문자열 포맷팅을 이용해 !!!python!!! 출력해라
print(f'{"python":!^12}')
print('{0:!^12}'.format('python'))

# 문자 갯수 세기
print("=="*20)
a = "hobby"
print(a.count('b')) # 문자갯수 세는겅 
a = "Python is the best choice"
print(a.find('b')) # 문자열에서 'b' 가 처음 나온 위치
print(a.find('k')) # -1을 반환 = 문자열이 존재하지 않음