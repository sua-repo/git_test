# 기능 관련 파일 
# 기록 관리, 예산 관리, 데이터 필터링 등 프로그램의 핵심 로직 포함
# 기록 관리 : add_record / edit_record / delete_record / get_montly_records
# 분석 로직 : generate_pie_chart, generate_bar_chart / calculate_remaing_budget

from record_manager import list_records
from datetime import datetime


def generate_bar_chart(frame, treeview, categories) : 

    import matplotlib.ticker as mticker
    import matplotlib.pyplot as plt
    from matplotlib import rc, font_manager
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


    # 한글 폰트 경로 설정 (Windows: 맑은 고딕, macOS: AppleGothic)
    font_path = "C:/Windows/Fonts/malgun.ttf"  # Windows의 경우
    font = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font)


    # 한글이 깨지지 않도록 마이너스(-) 기호도 설정
    plt.rcParams['axes.unicode_minus'] = False


    records = treeview.get_children()
    data = {category: 0 for category in categories}  # 초기화된 카테고리별 지출
    
    for record in records:
        values = treeview.item(record, "values")
        category = values[2]  # TreeView의 세 번째 열이 '카테고리'라고 가정
        amount = float(values[3])  # TreeView의 네 번째 열이 '금액'이라고 가정
        if category in data:
            data[category] += amount

    # 데이터 정렬 (카테고리 순서 유지)
    sorted_categories = categories
    sorted_values = [data[category] for category in sorted_categories]
    
    # Matplotlib로 막대 그래프 생성
    if "seaborn-v0_8-muted" in plt.style.available:
        plt.style.use("seaborn-v0_8-muted")
    else:
        plt.style.use("default")  # 기본 스타일 적용

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(sorted_categories, sorted_values, color=plt.get_cmap("Set2").colors)

    # y축 눈금을 5만 원 단위로 설정
    max_value = max(sorted_values) if sorted_values else 50000  # 최대값이 없으면 기본 5만 원 설정
    max_value = ((max_value // 50000) + 1) * 50000  # 최대값을 5만 원 단위로 반올림

    ax.yaxis.set_major_locator(mticker.MultipleLocator(50000))  # y축 간격을 5만 원으로 고정
    ax.set_ylim(0, max_value)  # y축 범위를 5만 원 단위로 설정
    
    # 그래프 레이블 및 제목
    ax.set_title("월별 지출 비율")
    ax.set_ylabel("금액")
    ax.set_xlabel("카테고리")
    ax.set_xticks(range(len(sorted_categories)))
    ax.set_xticklabels(sorted_categories, rotation=45, ha="right")

    # 기존 그래프 제거
    for widget in frame.winfo_children():
        widget.destroy()

    # Tkinter Frame에 그래프 삽입
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)


def calculate_remaining_budget(year, month, records, budget) : 

    # 해당 연도/월에 해당하는 지출 기록 필터링
    monthly_expenses = [
                            float(item["amount"]) for item in records 
                            if item["type"] == "지출" and item["date"].startswith(f"{year}-{str(month).zfill(2)}")
                        ]

    # 총 지출 계산
    total_expenditure = sum(monthly_expenses)

    # 남은 예산 계산
    remaining_budget = budget - total_expenditure

    return remaining_budget


def calculate_monthly_income_expense(records, selected_month, format_date):
        income = 0
        expense = 0
        for record in records:
            formatted_date = format_date(record["date"])

            if formatted_date.startswith(selected_month):  # 선택한 달의 기록만 계산
                try:
                    amount = float(record["amount"])  # 문자열이 아닌 경우에만 변환
                except ValueError:
                    continue
                
                if record["type"] == "수입":
                    income += float(record["amount"])
                elif record["type"] == "지출":
                    expense += float(record["amount"])
        return income, expense


def update_remaining_budget(entry_budget, budget_result_label, format_date) : # 남은 예산 업데이트
        # 예산 입력
        try:
            # 입력된 예산 값 가져오기
            budget = float(entry_budget.get()) if entry_budget.get().replace(".", "", 1).isdigit() else 0
        except ValueError:
            budget = 0  # 잘못된 입력 처리

         # 현재 달 데이터 가져오기
        records = list_records()
        selected_month_value = datetime.now().strftime("%Y-%m")  # 현재 달

        # 현재 달의 수입과 지출 계산
        income, expense = calculate_monthly_income_expense(records, selected_month_value, format_date)
        
        # 남은 예산 계산
        remaining_budget = budget + income - expense
    
        # UI 업데이트
        budget_result_label.configure(
            text=f"이번 달 수입: {income:,.0f} 원\n"
                f"이번 달 지출: {expense:,.0f} 원\n"
                f"남은 예산: {remaining_budget:,.0f} 원")

