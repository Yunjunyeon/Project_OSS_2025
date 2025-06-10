from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
	print("3. 총 지출 보기")
	print("4. 지출 내역 삭제")   # 추가
	print("5. 종료")            # 번호 조정

        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()
	elif choice == "4":
   	    budget.list_expenses()  
   	    if not budget.expenses:
                continue
   	    try:
       		idx = int(input("삭제할 지출 번호: ")) - 1  
        	budget.remove_expense(idx)
   	    except ValueError:
       		print("숫자를 입력해주세요.\n")
        elif choice == "5":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
