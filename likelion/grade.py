class Grade:
    def __init__(self):
        self.kor = 0
        self.eng = 0
        self.math = 0

    def set_kor(self, k):
        self.kor = k

    def set_eng(self, e):
        self.eng = e

    def set_math(self, m):
        self.math = m

    def get_total(self):
        return self.kor + self.eng + self.math  

    def get_avg(self):
        return self.get_total() / 3  

    def get_grade(self):
        avg = self.get_avg()  
        if avg >= 90:
            return "수"
        elif avg >= 80:
            return "우"
        elif avg >= 70:
            return "미"
        elif avg >= 60:
            return "양"
        else:
            return "가"
        

def main () : 
    while True :
        grade = Grade()
        kor = int(input("국어 성적: "))
        eng = int(input("영어 성적: "))
        math = int(input("수학 성적: "))

        grade.set_kor(kor)
        grade.set_eng(eng)
        grade.set_math(math)


        print("총합:", grade.get_total())
        print("평균:", grade.get_avg()) 
        print("최종 성적 등급:", grade.get_grade())

        continue_yn = input("그만하시겠습니까? (y / n)")
        if continue_yn.upper() == "Y" or continue_yn.upper() == "YES" : 
            break
        
    print("프로그램 종료")
    

main()
