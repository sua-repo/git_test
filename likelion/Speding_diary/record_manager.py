# 수입/지출 데이터 관리 (추가, 삭제, 수정, 조회)
# 수입/지출 데이터 관리 (추가, 삭제, 수정, 조회)
# UI 관련 공통 함수 관리

from file_manager import save_data, load_data
from date_utils import format_date
from datetime import datetime
from tkinter import messagebox

# 프로그램 시작 시 데이터 불러오기
rec_list = sorted(load_data(), key=lambda record: record["date"])


def save_and_sort() :    # 데이터를 정렬 후 저장하는 함수
    global rec_list

    # 모든 데이터의 날짜를 표준 형식으로 변환
    for record in rec_list:
        record["date"] = format_date(record["date"])

    # 날짜를 datetime 객체로 변환 후 정렬
    rec_list.sort(key=lambda record: datetime.strptime(record["date"], "%Y-%m-%d"))

    save_data(rec_list)  # 정렬 후 저장

def add_record(amount, category, memo, date, type_) : 
    global rec_list     # 전역 변수로 선언
    rec_list.append({"date" : format_date(date), "type" : type_, "amount" : amount, "category" : category, "memo" : memo})
    save_and_sort()  # 정렬 후 저장


def edit_record(original_record, new_amount, new_category, new_memo, new_date, new_type_) : 
    global rec_list     # 전역 변수로 선언

    # 기존 데이터 변환 (날짜 & 금액 형식 통일)
    original_record["date"] = format_date(original_record["date"])
    original_record["amount"] = str(original_record["amount"])  # 금액을 문자열로 변환

    for i, record in enumerate(rec_list):

        # 리스트 내 데이터도 변환하여 비교
        record_formatted = {
            **record,
            "date": format_date(record["date"]),
            "amount": str(record["amount"]),
        }

        if record_formatted == original_record:  # 기존 데이터와 일치하는 항목 찾기
            # 새로운 값으로 업데이트
            if (
                    format_date(record["date"]) == format_date(original_record["date"])
                    and str(record["amount"]) == str(original_record["amount"])
                    and record["category"] == original_record["category"]
                    and record["memo"] == original_record["memo"]
                    and record["type"] == original_record["type"]
                ):
                rec_list[i] = {
                                    "date": format_date(new_date),
                                    "type": new_type_,
                                    "amount": new_amount,
                                    "category": new_category,
                                    "memo": new_memo,
                                }
            save_and_sort()  # 정렬 후 저장
            return

    # 🔴 기존 데이터를 찾지 못한 경우 경고 메시지 출력
    messagebox.showwarning("수정 오류", "기존 데이터를 찾을 수 없습니다. 새 데이터가 추가될 가능성이 있습니다.")


def delete_record(selected_record):
    global rec_list     # 전역 변수로 선언

    # 날짜 변환 (리스트 데이터와 비교 가능하도록)
    selected_record["date"] = format_date(selected_record["date"])
    selected_record["amount"] = str(selected_record["amount"])  # 금액을 문자열로 변환

    # 삭제 수행
    rec_list = [record for record in rec_list 
                if not (
                            format_date(record["date"]) == selected_record["date"] and
                            str(record["amount"]) == selected_record["amount"] and
                            record["category"] == selected_record["category"] and
                            record["memo"] == selected_record["memo"]
                        )
                ]
    
    save_and_sort()  # 정렬 후 저장


def list_records() : 
    global rec_list
    return rec_list  # 이미 정렬된 리스트 반환