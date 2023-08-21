# 학생 점수 계산 프로그램
# 기능: 1. 점수 입력, 2. 통계, 3. 종료 + def사용

scores = []
print("안녕하세요. 프로그램을 시작합니다.")

def showMenu():
    print("===========메뉴==========")
    print("1. 점수를 입력하세요.")
    print("2. 입력하신 평균을 계산합니다.")
    print("3. 프로그램을 종료합니다.")

def addScore():
    score = input("점수를 입력하여 주세요 : ") # 문자로 받는다
    score = int(score)
    scores.append(score)
    print(f"점수를 저장하였습니다. 현재 저장된 점수는 {scores} 입니다.")
    input("메뉴로 돌아갑니다. Enter를 눌러주세요")
def showAvr():
    sum = 0
    for i in scores:
        sum += i
    length = len(scores)
    avg = sum / length 
    print(f"평균은 {avg} 입니다")
    input("메뉴로 돌아갑니다. Enter를 눌러주세요")

while True:
    showMenu()
    command = input("실행하고자 하는 번호를 입력해주세요 : ")
    if command == "1":
        addScore()
    elif command == "2":
        showAvr()
    elif command == "3":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요")
        input("계속 하시려면 enter를 입력해주세요")