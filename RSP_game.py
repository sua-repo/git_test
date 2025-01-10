import random

RSP_inven = ["가위", "바위", "보"]

class RSPGame:
    def run(self):
        print("가위 바위 보 게임을 시작합니다!\n")

        while True:
            # 유저 입력
            while True:        
                user_RSP = input("가위 바위 보 중 하나를 입력하세요: ").strip()

                if user_RSP in RSP_inven:  
                    break
                print("잘못된 입력입니다. 가위, 바위, 보 중 하나를 입력해주세요.\n")
            
            # 컴퓨터 선택
            com_RSP = random.choice(RSP_inven)
            print(f"컴퓨터는 '{com_RSP}'를 냈습니다.\n")

            # 결과 판단
            if user_RSP == com_RSP:
                print("무승부입니다!\n")
            elif (user_RSP == "가위" and com_RSP == "보") or (user_RSP == "바위" and com_RSP == "가위") or (user_RSP == "보" and com_RSP == "바위") :
                print("이겼습니다!! 축하합니다!!\n")
            else:
                print("앗... 졌습니다...\n")

            # 게임 반복 여부
            retry = input("게임을 계속 하시겠습니까? (Y/N): ").strip().upper()
            print()
            if retry not in ["Y", "YES"]:
                print("게임을 종료합니다. \n감사합니다!\n")
                break

game = RSPGame()
game.run()