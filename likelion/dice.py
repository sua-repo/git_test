# 첫번째 참가자의 이름을 입력하세요.
# 두번째 참가자의 이름을 입력하세요.
# ~ 주사위 : 
# ~ 주사위 : 
# ~ 가 이겼습니다.

import random

class DiceGame() : 
    def __init__(self) : 
        while True : 
            try : 
                self.user_name1 = input("첫번째 참가자의 이름을 입력하세요. : ")
                self.user_name2 = input("두번째 참가자의 이름을 입력하세요. : ")
                break

            except ValuError : 
                print("입력이 잘못되었습니다. 처음부터 다시 입력하세요.")
                continue
        
    def run(self) : 
        try :         
            self.dice_num1 = random.randint(1, 6)
            self.dice_num2 = random.randint(1, 6)
            
            print(self.user_name1 + " 주사위 숫자는 " + str(self.dice_num1))
            print(self.user_name2 + " 주사위 숫자는 " + str(self.dice_num2))

            if self.dice_num1 > self.dice_num2 : 
                print(self.user_name1 + "님이 이겼습니다.")

            elif self.dice_num2 > self.dice_num1 : 
                print(self.user_name2 + "님이 이겼습니다.")
            else : 
                print("비겼습니다.")
            
        except Exception as msg:
            print("알 수 없는 오류가 발생했습니다: " + msg)


dice_game = DiceGame()
dice_game.run()
