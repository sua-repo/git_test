import random

class UpDownGame: 
    def run(self): 
        print("다운 게임을 시작합니다! 1~100 사이의 숫자를 맞혀보세요.\n")
        rand_num = random.randint(1, 100)
        attempts = 0

        while attempts < 10:
            try:
                user_input = input(f"{attempts + 1}번째 시도: 숫자를 입력하세요 (1~100): ").strip()
                input_num = int(user_input)

                if not (1 <= input_num <= 100):
                    print("1에서 100 사이의 숫자를 입력해주세요.\n")
                    continue

                attempts += 1

                if input_num == rand_num:
                    print(f"정답입니다! {attempts}번 만에 맞혔어요!\n")
                    break
                elif input_num > rand_num:
                    print("DOWN!\n")
                else:
                    print("UP!\n")

            except ValueError:
                print("잘못된 입력입니다. 숫자로 입력해주세요.\n")

        if attempts == 10:
            print("10번 시도했습니다. \n게임에서 졌습니다.")
            print(f"정답은 {rand_num}였습니다.\n")

game = UpDownGame()
game.run()
