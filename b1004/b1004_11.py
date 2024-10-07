# 학생 정보를 저장할 리스트
student_list = []

while True:
    # 메인 메뉴 출력
    print("[ 학생성적프로그램 ]")
    print("-" * 60)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("0. 프로그램종료")
    print("-" * 60)
    choice = input("원하는 번호를 입력하세요.>> ")
    print()
    
    if choice == "0":
      print("프로그램을 종료합니다.")
      break  
    
    if choice == '1':
        print("[ 학생성적입력 ]")
        while True:
            # 이름 입력 및 상위 메뉴 이동 처리
            name = input("이름을 입력하세요. 0. 상위메뉴이동: ").strip()
            if name == '0':
                print("메뉴 화면으로 이동합니다.")
                break

            # 국어, 영어, 수학 점수 입력
            kor = int(input("국어 점수: "))
            eng = int(input("영어 점수: "))
            math = int(input("수학 점수: "))

            # 총점과 평균 계산 후 학생 정보 리스트에 추가
            sum_scores = kor + eng + math
            avg = sum_scores / 3
            no = len(student_list) + 1  # 학생 번호 생성 (리스트 길이 + 1)
            
            student = [no, name, kor, eng, math, sum_scores, avg, 0]  # 등수는 0으로 초기화
            student_list.append(student)
            print(f"{no}. {name}: {kor}, {eng}, {math} | 합계: {sum_scores} | 평균: {avg:.2f}")
            
    elif choice == "2":
      print("[ 학생성적출력 ]")
    
    elif choice == "3":
      print("[ 학생성적수정 ]")
