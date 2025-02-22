import customtkinter as ctk
from tkcalendar import Calendar
from tkinter import ttk, messagebox  
from datetime import datetime

from ui_manager import setup_main_window, update_bottom_right_section
from record_manager import add_record, edit_record, delete_record, list_records
from func_manager import update_remaining_budget, generate_bar_chart
from theme import apply_theme, BG_COLOR, FONT_STYLE
from date_utils import format_date


# 테마가 적용된 Entry 생성 함수
def create_thematic_entry(parent, **kwargs):
    entry = ctk.CTkEntry(parent, **kwargs)
    apply_theme(entry, "entry")
    return entry

# 테마가 적용된 Label 생성 함수
def create_thematic_label(parent, **kwargs):
    label = ctk.CTkLabel(parent, **kwargs)
    apply_theme(label, "label")
    return label
    
def show_main_screen(win) : 
    left_frame, top_right_frame, bottom_right_frame = setup_main_window(win)

    # 현재 날짜 가져오기
    today = datetime.now()

    # 왼쪽 영역
    date_var = ctk.StringVar(value = "")
    cal = Calendar(left_frame, selectmode = "day", year=today.year, month=today.month)
    cal.configure(
                    background="#FFCCCC",         # 배경색
                    foreground="black",           # 텍스트 색상
                    selectbackground="#FF6666",   # 선택된 날짜 배경색
                    selectforeground="white",     # 선택된 날짜 텍스트 색상
                    weekendbackground="#FFDAB9",  # 주말 배경색
                    font=("Arial", 12),           # 글꼴과 크기
                    headersbackground="#FFB6C1",  # 헤더 배경색
                    headersforeground="black",    # 헤더 텍스트 색상
                    bordercolor=BG_COLOR         # 테두리 색상
                )
    cal.pack(pady = 10)

    def select_date(event) : 
         date_var.set(cal.get_date())

    cal.bind("<<CalendarSelected>>", select_date)       # 날짜 선택 시 select_date() 호출

    def clear_inputs():
        date_var.set("")        # 날짜 선택 초기화
        category_var.set("카테고리 선택")  # 카테고리 초기화
        entry_amount.delete(0, "end")  # 금액 초기화
        entry_memo.delete(0, "end")  # 내역 초기화
        transaction_type.set("지출")  # 기본값을 '지출'로 설정
        
    # 수입/지출 선택 라디오 버튼
    transaction_type = ctk.StringVar(value="지출")  # 기본값 설정

    radio_frame = ctk.CTkFrame(left_frame, fg_color = BG_COLOR)  # 왼쪽 영역에 프레임 추가
    radio_frame.pack(pady=5)  # 프레임 배치 

    radio_income = ctk.CTkRadioButton(radio_frame, text="수입", variable=transaction_type, value="수입")
    apply_theme(radio_income, "radio")
    radio_income.pack(side="left", padx=5)

    radio_expense = ctk.CTkRadioButton(radio_frame, text="지출", variable=transaction_type, value="지출")
    apply_theme(radio_expense, "radio")
    radio_expense.pack(side="right", padx=5)

    # 카테고리 선택 콤보박스 (수입 / 지출)
    income_categories = ["월급", "용돈", "기타"]
    expense_categories = ["식비", "교통", "쇼핑", "정기결제", "여가생활", "기타", "경조사", "화장품", "게임"]

    category_var = ctk.StringVar(value="카테고리 선택")
    category_combo = ctk.CTkComboBox(left_frame, values=expense_categories, variable=category_var)
    apply_theme(category_combo, "combobox")  # 테마 적용
    category_combo.configure(fg_color="#FFFFFF", button_color="#FF9999", button_hover_color="#FF6666", dropdown_hover_color="#FFDDDD", dropdown_fg_color="#FFFFFF")
    category_combo.pack(pady=5)


    def update_category(*args) :    # 라디오 버튼에 따라 카테고리 변경
        if transaction_type.get() == "수입":
            category_combo.configure(values=income_categories)
        else:                                              
            category_combo.configure(values=expense_categories)         

    transaction_type.trace_add("write", update_category)

    # 금액 / 내역 입력 
    entry_amount = ctk.CTkEntry(left_frame, placeholder_text="금액")
    entry_amount.pack(pady=5)

    entry_memo = ctk.CTkEntry(left_frame, placeholder_text="내역")
    entry_memo.pack(pady=5)

    selected_record_index = ctk.IntVar(value=-1)

    # 오른쪽 위 - 기록 조회
    header_frame = ctk.CTkFrame(top_right_frame, fg_color = BG_COLOR)
    header_frame.pack(fill="x", pady=5)
    
    # 선택된 달을 저장하는 변수
    selected_month = ctk.StringVar(value=datetime.now().strftime("%Y-%m"))



    style = ttk.Style()
    style.theme_use("default")
    style.configure(
        "TCombobox",
        fieldbackground="#FFFFFF",  # 드롭다운 배경색
        background="#FFFFFF",       # 콤보박스 배경색
        foreground="black",          # 텍스트 색상
        arrowcolor = "#FF9999"
    )

    style.map(
                "TCombobox",
                fieldbackground=[("readonly", "#FFFFFF")],  # 읽기 전용 상태에서 배경색 유지
                background=[("active", "#FF6666")],        # 버튼 활성화 시 색상 (CTkComboBox의 button_hover_color와 유사)
                foreground=[("readonly", "black")],        # 읽기 전용 상태에서 텍스트 색상
            )
    
    month_values = [f"{y}-{str(m).zfill(2)}" for y in range(2023, 2031) for m in range(1, 13)]

    # ComboBox 생성
    month_combo = ttk.Combobox(top_right_frame, values = month_values, state = "readonly")
    month_combo.set(datetime.now().strftime("%Y-%m"))
    month_combo.place(relx=1.0, rely=0.0, anchor="ne")  # 프레임 오른쪽 상단에 배치

    # Combobox 값 변경 시 업데이트 실행
    def on_month_selected(event):
        selected_month.set(month_combo.get())  # 선택된 달 업데이트
        update_records()
        update_bottom_right_section(bottom_right_frame, records_box)

    month_combo.bind("<<ComboboxSelected>>", on_month_selected)

    label_records = ctk.CTkLabel(header_frame, text="기록 조회", font = FONT_STYLE)
    label_records.pack(side="top", pady=5)
    
    # Treeview 스타일 설정
    style = ttk.Style()
    style.theme_use("default")  # 기본 테마 사용
    style.configure(
        "Treeview", 
        borderwidth=0,            # 테두리 두께 0으로 설정
        relief="flat",            # 테두리를 플랫으로 설정
        background="#FFFFFF",     # 배경색
        foreground="black",       # 텍스트 색상
        fieldbackground="#FFFFFF" # 필드 배경색
    )
    style.configure(
        "Treeview.Heading", 
        background="#FFCCCC",     # 헤더 배경색
        foreground="black",       # 헤더 텍스트 색상
        borderwidth=0             # 헤더 테두리도 제거
    )
    style.map(
        "Treeview", 
        background=[("selected", "#FF9999")],  # 선택된 행 배경색
        foreground=[("selected", "white")]    # 선택된 행 텍스트 색상
    )

    global records_box
    records_box = ttk.Treeview(top_right_frame, columns=("date", "type", "category", "amount", "memo"), show="headings")

    # 헤더 설정
    records_box.heading("date", text="날짜")
    records_box.heading("type", text="구분")
    records_box.heading("category", text="카테고리")
    records_box.heading("amount", text="금액")
    records_box.heading("memo", text="내역")
    
    # 각 열의 너비 및 정렬 설정
    records_box.column("date", width=100, anchor="center")
    records_box.column("type", width=50, anchor="center")
    records_box.column("category", width=100, anchor="center")
    records_box.column("amount", width=80, anchor="e")
    records_box.column("memo", width=200, anchor="center")

    # 스크롤바 추가 (수직)
    scrollbar_y = ttk.Scrollbar(records_box, orient = "vertical", command=records_box.yview)
    records_box.configure(yscrollcommand=scrollbar_y.set)

    # 스크롤바 추가 (수평)
    scrollbar_x = ttk.Scrollbar(records_box, orient="horizontal", command=records_box.xview)
    records_box.configure(xscrollcommand=scrollbar_x.set)

    records_box.pack(pady=5, fill="both", expand=True)
    scrollbar_y.pack(side="right", fill="y")
    scrollbar_x.pack(side="bottom", fill="x")

    def on_record_select(event):
        selected_item = records_box.selection()
        if not selected_item:
            return

        item = records_box.item(selected_item[0])["values"]  # 선택된 행 데이터 가져오기
        date_var.set(item[0])  # 날짜 설정
        category_var.set(item[2])  # 카테고리 설정

        entry_amount.delete(0, "end")
        entry_amount.insert(0, item[3])  # 금액 설정
        entry_memo.delete(0, "end")
        entry_memo.insert(0, item[4])  # 내역 설정

        # 선택한 카테고리가 income_categories에 있으면 "수입", 아니면 "지출"
        if item[2] in income_categories:
            transaction_type.set("수입")
        else:
            transaction_type.set("지출")
    # Treeview에서 선택 시 실행될 함수 바인딩
    records_box.bind("<<TreeviewSelect>>", on_record_select)  # 선택 시 자동 입력


    def update_records():   # 기록 목록 업데이트
        
        records_box.delete(*records_box.get_children())  # 기존 데이터 삭제
        selected_month_value = selected_month.get()  # 사용자가 선택한 달 

        records = list_records()    # 기존 데이터 가져오기

        for i, record in enumerate(records):
            formatted_date = format_date(record["date"])  # 날짜 형식 변환

            # 날짜 변환 후 비교
            if formatted_date.startswith(selected_month_value) :                 
                records_box.insert("", "end", iid=str(i), values=(formatted_date, record["type"], record["category"], record["amount"], record["memo"]))


        # Treeview 크기 고정
        records_box.configure(height=10)

        # 날짜 초기화
        date_var.set("")  # 날짜 입력 필드 초기화
        cal.selection_clear()  # 캘린더 날짜 초기화

    
    # 등록 / 수정 / 삭제 버튼
    btn_frame = ctk.CTkFrame(left_frame, fg_color = BG_COLOR)
    btn_frame.pack(pady=5)


    def add_new_record() :      # 새로운 기록 추가 후 UI 업데이트

        try:
            record_date = date_var.get() if date_var.get() else ""      # 날짜 입력 확인
            amount_value = entry_amount.get().strip()  # 입력값 정리
            memo_value = entry_memo.get().rstrip()

            # 금액과 내역을 바꿔서 입력한 경우 알아서 바꿔서 저장
            # 입력값이 숫자/문자인지 판별
            is_amount_digit = amount_value.replace(".", "", 1).isdigit()  # 실수 가능 체크
            is_memo_digit = memo_value.replace(".", "", 1).isdigit()

            # 입력값이 서로 반대로 들어간 경우 자동 교환
            if not is_amount_digit and is_memo_digit:
                amount_value, memo_value = memo_value, amount_value  # 교환


            # 필수 입력값 확인
            if not amount_value or not memo_value or category_var.get() == "카테고리 선택" or not record_date:
                messagebox.showwarning("입력 오류", "모든 항목을 입력하세요.")
                return  # 입력이 안 된 경우 등록하지 않음
            
            add_record(amount_value, category_var.get(), memo_value, record_date, transaction_type.get())

            update_records()
            update_bottom_right_section(bottom_right_frame, records_box)
        finally:
            clear_inputs()  # 오류가 발생하더라도 항상 초기화

    def edit_existing_record() :    # 기록 수정 후 UI 업데이트

        try:
            selected_item = records_box.selection()
            if not selected_item:
                messagebox.showwarning("선택 오류", "수정할 기록을 선택하세요.")
                return

            item = records_box.item(selected_item[0])["values"]  # 선택된 행 데이터 가져오기
            original_record = {
                                    "date":  format_date(item[0]),
                                    "type": item[1],
                                    "category": item[2],
                                    "amount": str(item[3]),  # 금액을 문자열로 변환
                                    "memo": item[4],
                                }

            # 입력된 새로운 값
            new_amount = entry_amount.get().strip()
            new_category = category_var.get()
            new_memo = entry_memo.get().strip()
            new_date = date_var.get() if date_var.get() else original_record["date"]  # 비어있으면 기존 날짜 사용
            new_type_ = transaction_type.get()

            # 필수 입력값 확인
            if not new_amount or not new_memo or new_category == "카테고리 선택":
                messagebox.showwarning("입력 오류", "모든 항목을 입력하세요.")
                return

            edit_record(original_record, new_amount, new_category, new_memo, new_date, new_type_)

            update_records()  # 수정된 데이터 반영
            update_bottom_right_section(bottom_right_frame, records_box)

        finally :
            clear_inputs()  # 입력 필드 초기화

    def delete_selected_record() :      # 기록 삭제 후 UI 업데이트
        try:
            selected_item = records_box.selection()
            if not selected_item:
                clear_inputs()  # 아무 항목도 선택되지 않았을 경우에도 초기화
                return

            item = records_box.item(selected_item[0])["values"]  # 선택된 항목의 데이터 가져오기
            selected_record = {
                                    "date": item[0],
                                    "type": item[1],
                                    "category": item[2],
                                    "amount": item[3],
                                    "memo": item[4],
                                }
            
            delete_record(selected_record)  # 데이터 자체를 전달하여 삭제

            update_records()
            update_bottom_right_section(bottom_right_frame, records_box)

        finally:
            clear_inputs()  # 오류가 발생해도 항상 실행

    btn_add = ctk.CTkButton(btn_frame, text="등록", width = 5, command=add_new_record)
    apply_theme(btn_add, "button")
    btn_add.pack(side="left", padx=5)

    btn_edit = ctk.CTkButton(btn_frame, text="수정", width = 5, command=edit_existing_record)
    apply_theme(btn_edit, "button")
    btn_edit.pack(side="left", padx=5)

    btn_delete = ctk.CTkButton(btn_frame, text="삭제", width = 5, command=delete_selected_record)
    apply_theme(btn_delete, "button")
    btn_delete.pack(side="left", padx=5)

    update_records()

    # 이번 달 예산 입력
    budget_frame = ctk.CTkFrame(left_frame, fg_color = BG_COLOR)
    budget_frame.pack(pady=(80, 10))

    ctk.CTkLabel(budget_frame, text="이번 달 예산").pack(side="left", padx=5)
    entry_budget = ctk.CTkEntry(budget_frame, width=100)
    entry_budget.pack(side="left", padx=5)


    # 이번 달 남은 돈 표시
    budget_result_label = ctk.CTkLabel(left_frame, text="이번 달 수입: 0 원\n이번 달 지출: 0 원\n남은 예산: 계산 중...", justify="left")
    budget_result_label.pack(pady=5)

    btn_update_budget = ctk.CTkButton(left_frame, text="예산 계산", command = lambda: update_remaining_budget(entry_budget, budget_result_label, format_date))
    apply_theme(btn_update_budget, "button")
    btn_update_budget.pack(pady=5)

    btn_exit = ctk.CTkButton(left_frame, text = "종료", width = 5, command = win.quit)
    apply_theme(btn_exit, "button")
    btn_exit.pack(pady = (15, 0))

    update_bottom_right_section(bottom_right_frame, records_box)

    # 기록 목록도 처음 실행 시 자동으로 업데이트
    update_records()

def update_bottom_right_section (frame, treeview) : 

    categories = ["식비", "교통", "쇼핑", "정기결제", "여가생활", "기타", "경조사", "화장품", "게임"]
    generate_bar_chart(frame, treeview, categories)
