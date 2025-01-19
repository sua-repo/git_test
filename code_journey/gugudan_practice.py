# 구구단 프로그램
# 사용자가 입력한 단수로 구구단 출력
# 문제를 내서 사용자가 정답을 맞히면 점수를 줌
# 맞힌 개수와 오답 개수를 출력
# 사용자 입력값이 int가 아니면 오류 메시지 출력

import random

class Gugudan : 
    def __init__(self) : 
        self.score = [0, 0, 0]     # 정답, 오답, 총 문제수
        self.random_dan = 0
        self.random_num = 0
        self.option = 0
        self.dan = 0
        self.answer_key = 0
        self.user_answer = 0

    def get_int_input(self, prompt, error_message="잘못 입력했습니다. 다시 입력하세요."):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print(f"\n{error_message}")
                
    def print_multiplication_table(self, dan):    # 사용자가 입력한 단수로 구구단 출력
        for i in range(1, 10):
            print(f"{dan} * {i} = {dan * i}")

    def quiz_user(self):
        self.random_dan = random.randint(2, 9)      # 랜덤으로 문제 출제
        self.random_num = random.randint(1, 9)

        print(f"\n{self.random_dan} * {self.random_num}의 정답은?? : ")
        return self.random_dan * self.random_num    # 정답을 리턴

    def show_score(self):
        print("\n현재까지의 점수를 공개합니다.")
        print(f"총 문제 수 : {self.score[2]} \t정답 수 : {self.score[0]} \t오답수 : {self.score[1]}")

    def run(self):
        print("구구단 프로그램을 실행합니다.")

        while True:
            print("\n1. 구구단 출력 \n2. 구구단 맞히기 \n3. 점수 확인 \n4. 종료")
            self.option = self.get_int_input(">> ", "1, 2, 3, 4번 중 하나를 고르세요")

            if self.option == 1:       # 입력한 단수에 맞는 구구단 출력
                self.dan = self.get_int_input("\n원하는 단수를 입력하세요 : ")
                self.print_multiplication_table(self.dan)

            elif self.option == 2:      # 구구단 퀴즈
                self.answer_key = self.quiz_user()
                self.user_answer = self.get_int_input(">> ")

                if self.answer_key == self.user_answer:    # 맞춘 경우
                    self.score[0] += 1
                    self.score[2] += 1
                    print("정답입니다!")
                else:                                       # 틀린 경우
                    self.score[1] += 1
                    self.score[2] += 1
                    print("아쉽지만 정답이 아닙니다.")

            elif self.option == 3:      # 점수 공개
                self.show_score()

            elif self.option == 4:      # 종료
                break

            else:                       # 1~4번 안 고른 경우
                print("\n1, 2, 3, 4번 중 하나를 고르세요.")

        print("\n구구단 프로그램을 종료합니다.")

gugudan = Gugudan()
gugudan.run()
