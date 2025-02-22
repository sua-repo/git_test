# UI 공통 관리 파일 
# 위젯 초기화 및 화면 전환 함수 포함 
# 공통적으로 사용하는 UI 유틸리티 함수만 포함

import customtkinter as ctk
from theme import *


def clear_widget(win) : 
    
    for widget in win.winfo_children() : 
        
        if widget.winfo_manager() in ('pack', 'grid', 'place'):
            if widget.winfo_manager() == 'pack':
                widget.pack_forget()
            elif widget.winfo_manager() == 'grid':
                widget.grid_forget()
            elif widget.winfo_manager() == 'place':
                widget.place_forget()
        else:
            print(f"{widget} \t위젯을 제거할 수 없음! (winfo_manager: {widget.winfo_manager()})")
        



def setup_main_window(win) : 
    # 메인 창을 왼쪽 / 오른쪽 위 / 오른쪽 아래 로 나눔

    # 전체 화면을 2개 column으로 배치

    win.grid_columnconfigure(0, weight = 1)     # 왼쪽 비율 1
    win.grid_columnconfigure(1, weight=3)       # 오른쪽 비율 3

    # 오른쪽을 위아래로 나눔
    win.grid_rowconfigure(0, weight = 1)        # 오른쪽 위 / 기록 조회
    win.grid_rowconfigure(1, weight = 1)        # 오른쪽 아래 / 그래프

    # 왼쪽 영역
    left_frame = ctk.CTkFrame(win, fg_color=BG_COLOR, width=250, height=600)
    left_frame.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=10, pady=10)
    left_frame.pack_propagate(False)  # 프레임 크기 자동 조정 비활성화

    # 오른쪽 위 영역
    top_right_frame = ctk.CTkFrame(win, fg_color=BG_COLOR, width=800, height=300)
    top_right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
    top_right_frame.pack_propagate(False)  # 프레임 크기 자동 조정 비활성화

    # 오른쪽 아래 영역
    bottom_right_frame = ctk.CTkFrame(win, fg_color=BG_COLOR, width=800, height=300)
    bottom_right_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
    bottom_right_frame.pack_propagate(False)  # 프레임 크기 자동 조정 비활성화

    apply_theme(left_frame, "frame")
    apply_theme(top_right_frame, "frame")
    apply_theme(bottom_right_frame, "frame")

    return left_frame, top_right_frame, bottom_right_frame


def update_top_right_section(frame):
    clear_widget(frame)
    frame.configure(width=800, height=300)
    label = ctk.CTkLabel(frame, text="기록 조회", font =FONT_STYLE)
    label.pack(pady=10)
    listbox = ctk.CTkTextbox(frame, width=300, height=100)
    listbox.pack(pady=5)
    listbox.insert("end", "2025-02-01 | 식비 | 5000원")

def update_bottom_right_section(frame):
    clear_widget(frame)
    frame.configure(width=800, height=300)
    label = ctk.CTkLabel(frame, text="그래프", font = FONT_STYLE)
    label.pack(pady=10)
   