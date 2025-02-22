# UI 스타일 파일
# 배경색, 버튼색, 폰트 등 전역 스타일을 관리
# 테마를 적용하는 apply_theme() 포함


BG_COLOR = "#FBEFF2"
FONT_STYLE = ("Comic Sans MS", 12)
BUTTON_COLOR = "#FFB6C1"
ENTRY_COLOR = "#FFFACD"

def apply_theme(widget, type_):
    if type_ == "button":
        widget.configure(
                            fg_color="#FFB6C1",  # 버튼 내부 색상 (기존 설정)
                            text_color="black",
                            corner_radius=10,  # 둥근 모서리
                            bg_color="#FBEFF2",  # 버튼 외부 배경색 추가
                            hover_color="#FF6666"  # 호버 색상 (더 진한 핑크)
                        )
    elif type_ == "entry":
        widget.configure(fg_color=ENTRY_COLOR, text_color="black", corner_radius=5)
    elif type_ == "label":
        widget.configure(text_color="black", font=FONT_STYLE)
    elif type_ == "radio":  
        widget.configure(
                            fg_color="#ff9999",  # 내부 색상
                            hover_color="#FFCCCC",  # 호버 색상
                            border_color="#cccccc",  # 외곽선 색상
                            text_color="black"
                        )    
    elif type_ == "frame":  # 프레임 스타일 추가
        widget.configure(bg_color=BG_COLOR)

    elif type_ == "combobox": 
        widget.configure(
                            fg_color="#FFFFFF", 
                            button_color="#FF9999",
                            button_hover_color="#FF6666", 
                            dropdown_hover_color="#FFDDDD", 
                            dropdown_fg_color="#FFFFFF"
                        )