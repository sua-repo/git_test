# 메인 실행 파일 
# 전체 프로그램의 진입점으로 창을 생성하고 메인 화면 호출
# 전반적인 실행 흐름만 포함

import logging
import customtkinter as ctk
from theme import BG_COLOR
from main_screen import show_main_screen

def cancel_all_after(win) :         # 현재 Tkinter 창에서 실행 중인 after 예약된 작업들을 모두 취소

    try:
        after_jobs = win.tk.call('after', 'info')  # after 예약된 작업 리스트 가져오기
        if isinstance(after_jobs, tuple):  # 튜플이면 그대로 반복문 처리
            for after_id in after_jobs:
                try:
                    win.after_cancel(after_id)
                except Exception:
                    pass  # 이미 취소된 경우 예외 무시
    except Exception as e :
        logging.error("after 예약 취소 중 오류 발생", exc_info=True)  # 오류 로그 기록


def on_closing(win) :   # 창 닫기(X 버튼) 이벤트 핸들러"
    cancel_all_after(win)  # 예약된 after() 작업 모두 취소
    win.destroy()  # 안전하게 창 종료


def run_win() : 
    win = ctk.CTk()

    win.title("Spending Diary")
    win.geometry("1200x650")
    win.configure(fg_color=BG_COLOR)  

    # X 버튼 클릭 시 안전하게 종료하도록 설정
    win.protocol("WM_DELETE_WINDOW", lambda: on_closing(win))

    show_main_screen(win)  # 메인 화면 호출

    win.mainloop()


run_win()