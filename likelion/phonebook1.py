class Phone : 
    def __init__(self, name, tel) :
        self.name = name
        self.tel = tel


class PhoneBook :
    def __init__(self) : 
        self.people_num = 0
        self.tel_list = []
        self.find_name = ""
        self.stop = False

    def save_tel(self) : 
        for i in range(self.people_num) :       # 입력받은 인원수만큼
            self.name_input, self.tel_input = input("이름과 전화번호(이름과 전화번호는 빈칸 없이 입력) >> ").split()    
            self.phone = Phone(self.name_input, self.tel_input)
            self.tel_list.append(self.phone)    # 이름과 전화번호를 입력받아 Phone 인스턴스를 만들어 tel_list에 추가

        
        print("저장되었습니다...")

    def search_name(self) : 
        self.find_name = input("검색할 이름을 입력하세요 >> ")

        for phone in self.tel_list : 
            if self.find_name == "그만" : 
                self.stop = True
                return

            elif self.find_name == phone.name :       # 찾으려는 이름 발견
                return f"{phone.name}의 번호는 {phone.tel} 입니다."
        
        return f"{self.find_name}님이 없습니다."
        


    def open(self) : 
       
        while True :        # 인원수 입력 
            try : 
                self.people_num = int(input("인원수 >> "))
                break
            except ValueError:
                print("잘못 입력하셨습니다. 다시 입력하세요.")

        self.save_tel()

        while True : 
            
            result = self.search_name()
            if result is not None : 
                print(result)
            
            if self.stop : 
                break


phonebook = PhoneBook()
phonebook.open()

