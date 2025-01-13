# 백준 2480번 
# 같은 눈 3개 : 10000 + 같 * 1000
# 같은 눈 2개 : 1000 + 같 * 100
# 모두 다른 눈 : 가장 큰 눈 * 100

import random

class Dice : 
    def __init__(self) :    # 생성자 및 초기화
        self.prize = 0
        self.dice_lst = []

    def run(self) :
        self.dice_lst = list(map(int, input().split()))   # 세 수 입력

        self.dup_dice = set(self.dice_lst)     # 중복 제거
        self.dup_lst = list(self.dup_dice)

        if len(self.dup_lst) == 1 :      # 같은 눈 3개
            self.prize = self.dup_lst[0] * 1000 + 10000

        elif len(self.dup_lst) == 2 :    # 같은 눈 2개
            if self.dice_lst.count(self.dup_lst[0]) == 2 :  # self.dup_lst[0]이 중복된 숫자라면
                self.prize = self.dup_lst[0] * 100 + 1000
            else :  # self.dup_lst[1]이 중복된 숫자라면
                self.prize = self.dup_lst[1] * 100 + 1000

        else : 
            self.prize = max(self.dice_lst) * 100
    
        print(self.prize)

dice = Dice()
dice.run()
 

 


