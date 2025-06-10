import datetime
import json
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    def save_data(self, fname="save.json"):
        data = []
        for e in self.expenses:
            data.append({
                "date": e.date,
                "cat": e.category,
                "desc": e.description,
                "amt": e.amount
            })
        with open(fname, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
        print(f"저장 완료: {fname}\n")

    def load_data(self, fname="save.json"):
        try:
            with open(fname, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.expenses = []
            for item in data:
                e = Expense(
                    item["date"],
                    item["cat"],
                    item["desc"],
                    item["amt"]
                )
                self.expenses.append(e)
            print(f"불러오기 완료: {fname}\n")
        except FileNotFoundError:
            print(f"{fname} 파일이 없습니다.\n")
