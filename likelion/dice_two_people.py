import random

class DiceGame: 
    def __init__(self): 
        self.user_name1 = ""
        self.user_name2 = ""

    def run(self): 
        print("주사위 게임을 시작합니다!")

        while True:  
            # 이름 입력받기
            while True:
                self.user_name1 = input("첫 번째 참가자 이름을 입력하세요: ").strip()
                self.user_name2 = input("두 번째 참가자 이름을 입력하세요: ").strip()

                if self.user_name1.isalpha() and self.user_name2.isalpha():    
                    break
                print("이름은 반드시 영문 또는 한글로 입력해주세요.\n")
        
            # 주사위 던지기
            dice_num1 = random.randint(1, 6)
            dice_num2 = random.randint(1, 6)

            print(f"{self.user_name1}의 주사위 숫자: {dice_num1}")
            print(f"{self.user_name2}의 주사위 숫자: {dice_num2}\n")

            # 결과 출력
            if dice_num1 > dice_num2: 
                print(f"{self.user_name1}님이 승리했습니다!\n")
            elif dice_num1 < dice_num2: 
                print(f"{self.user_name2}님이 승리했습니다!\n")
            else: 
                print("무승부입니다!\n")

            # 게임 반복 여부
            retry = input("게임을 다시 하시겠습니까? (Y/N): ").strip().upper()
            print()
            
            if retry not in ["Y", "YES"]:
                print("게임을 종료합니다.\n감사합니다!")
                break

dice_game = DiceGame()
dice_game.run()
