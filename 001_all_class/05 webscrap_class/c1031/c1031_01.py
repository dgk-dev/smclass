import func

while True:
    # 로그인이 되어 있는 상태의 첫메뉴
    # print("[ 학생성적 프로그램 ]")
    # print("1. 학생성적 입력")
    # print("2. 학생성적 출력")
    # print("3. 학생성적 수정")
    # print("4. 로그아웃")

    # 시작 화면 출력
    choice = func.screen()

    # 로그인
    if choice == '1':
        func.memLogin()
    
    # 비밀번호 찾기
    elif choice == '2':
        func.searchPassword()

    elif choice == '3':
        pass
    






