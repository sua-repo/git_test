import random

class Person :                  # 각 플레이어 객체를 생성하여 이름, 난수 리스트, 승리 여부를 저장함.
    def __init__(self, name) :
        self.name = name
        self.rand_list = []
        self.win = False

    def rand_play(self) :       # 1~3 난수 3개 저장
        self.rand_list = [random.randint(1, 3) for i in range(3)]
       
        
    def run (self) :            #엔터 입력 시 난수 3개를 출력하고, 모두 같으면 win = True
        self.win = None
        print(f"[{self.name}]")
        while True : 
            self.blank = input("<Enter> ")

            if self.blank == "" : 
                break
            else : 
                print("엔터만 눌러주세요.")
                
        self.rand_play()
        if len(set(self.rand_list)) == 1 :  # 숫자 세 개가 같을 경우
            print(f"{self.rand_list[0]}\t{self.rand_list[1]}\t{self.rand_list[2]}\t{self.name}님이 이겼습니다!")
            self.win = True
        else :                                                                                      # 그렇지 않을 경우
            print(f"{self.rand_list[0]}\t{self.rand_list[1]}\t{self.rand_list[2]}\t아쉽군요!")


first_user = input("1번째 선수 이름 >> ")
second_user = input("2번째 선수 이름 >> ")

person1 = Person(first_user)
person2 = Person(second_user)

while True : 
    person1.run()
    if person1.win : 
        break
    person2.run()
    if person2.win : 
        break
