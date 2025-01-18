class Phone:
    def __init__(self, name, tel):
        self.name = name
        self.tel = tel

    def set_name(self, name):
        self.name = name

    def set_tel(self, tel):
        self.tel = tel


class PhoneBook:
    def __init__(self):
        self.phone_list = []  # 딕셔너리 대신 리스트로 저장 (중복 허용)
        self.phone_list_max = None  # 최대 인원수

    def add(self, name, tel):
        self.phone_list.append(Phone(name, tel))  # 잘못된 튜플 괄호 제거

    def run(self):
        # 인원수 입력받기
        while True:
            try:
                self.phone_list_max = int(input("인원수 >> "))
                break
            except ValueError:
                print("잘못된 입력입니다. 인원수를 숫자로 입력해주세요.")
                continue

        # 이름과 전화번호 입력
        count = 0
        while count < self.phone_list_max:
            tel_name = input("이름과 전화번호 입력 (빈칸은 종료) >> ").strip()

            if tel_name == "":  # 빈 줄이면 종료
                print("프로그램을 종료합니다.")
                return  # 프로그램 종료

            tel_name_split = tel_name.split(" ")

            if len(tel_name_split) != 2:  # 이름과 전화번호가 모두 입력되었는지 확인
                print("잘못된 입력입니다. 이름과 전화번호를 공백으로 구분해 주세요.")
                continue

            # 입력 정상 처리
            self.add(tel_name_split[0], tel_name_split[1])
            count += 1

        print("저장되었습니다...")

        # 검색하기 루프
        while True:
            name = input("검색할 이름 입력 (그만 입력 시 종료) >> ").strip()

            if name == "그만":
                print("프로그램 종료 되었습니다.")
                break  # 검색 루프 종료

            # 검색 결과 처리
            searched_list = [phone for phone in self.phone_list if phone.name == name]

            if len(searched_list) == 0:
                print("찾는 이름이 없습니다.")
            else:
                for phone in searched_list:
                    print(f"이름: {phone.name}, 전화번호: {phone.tel}")


# 프로그램 실행
phone_book = PhoneBook()
phone_book.run()
