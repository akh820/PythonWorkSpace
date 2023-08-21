# 학생 점수 계산 프로그램
# 기능: 1. 점수 입력, 2. 통계, 3. 종료

def showMenu():
    print("===========메뉴===========")
    print("1. 점수 입력")
    print("2. 평균 점수 출력")
    print("3. 프로그램 종료")
 
def addScore():
    score = input("점수를 입력해주세요 : ") # 문자로 받음
    score = int(score) # 문자 "50" -> 50 숫자
    scores.append(score) # 입력받은 score를 scores 배열에 저장하겠다
    print(f'현재 저장되어있는 점수 : {scores}')
    input("입력이 완료 되었습니다. 계속 하시려면 Enter를 누르세요") 

def showAvr():
    sum = 0
    for e in scores:
        sum = sum + e   
    length = len(scores) # 배열 크기 계산 API
    avg = sum / length
    print(f'평균 점수 : {avg}')
    input("평균점수를 계산 하였습니다. 계속 하시려면 Enter를 누르세요")
        

print("안녕하세요")
print("학생 점수 계산 프로그램에 오신걸 환영합니다.")

scores = []

while True:
    # 메뉴 출력
    showMenu()
    command = input("실행하고자 하는 번호를 입력해 주세요 : ") # input은 항상 문자를 리턴해줌
    if command == "3":
        break
    elif command == "1": # 입력 로직 구현
        addScore()
    elif command == "2": # 평균 로직 구현
        showAvr()
    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요")
        input("계속 하시려면 enter를 입력해주세요") # 아무거나 입력되도댐

print("이용해주셔서 감사합니다")
print("프로그램을 종료합니다.")
