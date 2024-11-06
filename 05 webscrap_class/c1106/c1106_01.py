import functions


def main():
    conn = functions.connects()
    while True:
        choice = functions.screen()
        if choice == "1":
            functions.input_student(conn)
        elif choice == "2":
            functions.print_students(conn)
        elif choice == "3":
            functions.search_student(conn)
        elif choice == "4":
            functions.sort_students(conn)
        elif choice == "5":
            functions.update_rank(conn)
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 선택해주세요.")

    conn.close()


if __name__ == "__main__":
    main()
