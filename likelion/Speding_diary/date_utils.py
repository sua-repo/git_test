from datetime import datetime

def format_date(date_str):  # 날짜를 'YYYY-MM-DD' 형식으로 변환하는 함수
    try:
        # 날짜 형식이 %m/%d/%y 인 경우 변환
        return datetime.strptime(date_str, "%m/%d/%y").strftime("%Y-%m-%d")
    except ValueError:
        # 이미 %Y-%m-%d 형식인 경우 그대로 반환
        return date_str