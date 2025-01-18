import random
import sys
from random_word import RandomWords



class Hangman : 
    def __init__(self):
        self.max_attempt = 3        # 디폴트로 3번까지 틀릴 수 있다.
        self.attempt = 0            # 현재 시도 횟수
        self.letters = ""           # 현재 입력한 글자
        self.display_word = ['_'] * 5      # 현재 상태를 보여주는 단어
        self. is_stop = False

        self.word = self.get_random_word()  # 5글자 단어 가져오기

        
    def get_random_word(self) : 
        r = RandomWords()

        while True:
            word = r.get_random_word()          # 랜덤 단어 가져오기
            if word is not None and len(word) == 5:         # 단어가 None이 아니고, 길이가 5글자인 경우
                return word.lower()             # 소문자로 변환하여 반환


    def initialize_game(self, max_attempt) :    # 초기화를 통해 최대 도전 횟수 변경 가능
        self.max_attempt = max_attempt          
    

    def can_continue(self) :                    # 남아있는 목숨 개수를 비교해서 게임을 더 할 지 말 지를 결정하는 메서드
        if self.attempt < self.max_attempt :        
            return True
        else : 
            return False
    
    def show_lives(self) :                      # 글자를 맞추기 전 남아있는 목숨 개수를 하트 모양으로 보여주는 메서드
        for _ in range(self.max_attempt - self.attempt) : 
            print("♥", end = ' ')
        print()


    def guess_letter(self) :                    # 한 글자를 입력받아 update_display_word()로 전달하는 메서드
        while True : 
            try :

                self.letters = input("한 글자씩 추측해보세요  >>> ")

                # 종료 조건 
                if self.letters == "" or self.letters == "그만" or self.letters.upper() == "STOP" : 
                    print("게임을 종료합니다.")
                    sys.exit()
                
                
                if len(self.letters) == 1 and self.letters.isalpha() : 
                    self.letters = self.letters.lower()     # 소문자로 통일
                    break 

                else : 
                    raise ValueError
            except ValueError : 
                print("잘못 입력하셨습니다. 다시 입력하세요.")


        self.update_display_word(self.letters)


    def update_display_word(self, letter) :         # 입력받은 글자를 확인하고 업데이트 한 후 show_game_status() 실행하는 메서드
        if letter in self.word : 
            
            for i in range(5) : 
                if letter == self.word[i] : 
                    self.display_word[i] = letter

            self.show_game_status()
        
        else : 
            self.attempt += 1
            self.show_game_status()


    
    def show_game_status(self) :                    # 현재까지 상태를 보여주는 메서드
        
        print('[', end = ' ')

        for i in range( 5 ) : 
            print(f' \'{self.display_word[i]}\' ', end = ', ')
        
        print(']')


        if '_' not in self.display_word :       # 모든 글자를 다 찾음
            self.is_stop = True
            self.attempt = self.max_attempt     # 이제 더이상 입력받지 않아도 됨




hm = Hangman()

while True : 
    try : 
        max_attempt = int(input("최대 도전 횟수를 입력하세요. 입력하지 않을 경우 3회로 정해집니다.  >>> "))
        hm.initialize_game(max_attempt)       # 최대 도전 횟수 5번으로 변경
        break
    except : 
        print("3번 틀릴 경우 게임이 종료됩니다.")
        break

while hm.can_continue() : # 목숨이 남아있냐

    hm.show_lives()

    hm.guess_letter()


if hm.is_stop :    # 글자를 다 맞춘 경우
    print("성공~~!! \ ^ o ^/")

else :              # 목숨을 다 쓴 경우
    print(f"조금만 더 노력하면 성공할 거예요! 정답은 \'{hm.word}\'였어요. 화이팅!")