# 데이터 저장 및 불러오기 파일
# CSV 파일을 읽고 쓰는 함수 (save_data(), load_data())
# 예산 데이터 저장 / 불러오기 함수 포함 (save_budget(), load_budget())

import csv
import os
from tkinter import messagebox  
from date_utils import format_date

# 데이터 파일 이름 (프로그램의 현재 디렉토리에 저장됨)
DATA_FILE = "records.csv"

# 파일 초기화
if not os.path.exists(DATA_FILE): 
    with open(DATA_FILE, mode="w", encoding="utf-8") as file:
        file.write("date,type,amount,category,memo\n")
        
def save_data(records): 
    try:
        # 날짜를 변환 후 저장
        for record in records:
            record["date"] = format_date(record["date"])

        with open(DATA_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["date", "type", "amount", "category", "memo"])
            writer.writeheader()
            writer.writerows(records)  # 리스트의 딕셔너리 항목을 CSV로 저장
    except Exception as e:
        messagebox.showwarning("오류 발생", f"데이터 저장 중 오류 발생: {e}")

def load_data(): 
    if not os.path.exists(DATA_FILE): 
        return []  # 파일이 없으면 빈 리스트 반환
    try:
        with open(DATA_FILE, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return [{"date": format_date(row["date"]), **row} for row in reader]  # 날짜 변환 적용 CSV 데이터를 딕셔너리 리스트로 변환하여 반환
    except Exception as e:
        messagebox.showwarning("오류 발생", f"데이터 불러오기 중 오류 발생: {e}")
        return []