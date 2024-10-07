# 학생 정보를 저장할 리스트
student_list = []

while True:
    # 메인 메뉴 출력
    print("[ 학생성적프로그램 ]")
    print("-" * 60)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    print("0. 프로그램종료")
    print("-" * 60)
    choice = input("원하는 번호를 입력하세요.>> ")
    print()

    # 프로그램 종료
    if choice == '0':
        print("프로그램을 종료합니다.")
        break

    # 학생 성적 입력
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

    # 학생 성적 출력
    elif choice == '2':
        print("[ 학생성적출력 ]")
        print()
        # 제목 출력
        students_title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']
        print("\t".join(students_title))
        print("-" * 60)

        # 학생 정보를 평균 점수를 기준으로 정렬하여 출력
        sorted_list = sorted(student_list, key=lambda x: x[6], reverse=True)  # 평균 점수를 기준으로 내림차순 정렬
        for idx, student in enumerate(sorted_list):
            student[7] = idx + 1  # 등수 업데이트 (평균 점수가 높은 순서대로 1부터 할당)
            print(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]}\t{student[5]}\t{student[6]:.2f}\t{student[7]}")

    # 학생 성적 수정
    elif choice == '3':
        print("[ 학생성적수정 ]")
        print()
        edit_no = int(input("수정할 학생의 번호를 입력하세요: "))

        # 학생 번호에 해당하는 학생 찾기
        found = False
        for student in student_list:
            if student[0] == edit_no:
                found = True
                print(f"현재 성적 - 국어: {student[2]}, 영어: {student[3]}, 수학: {student[4]}")

                # 새로운 국어, 영어, 수학 점수 입력
                student[2] = int(input("새 국어 점수: "))
                student[3] = int(input("새 영어 점수: "))
                student[4] = int(input("새 수학 점수: "))

                # 총점과 평균 재계산
                student[5] = student[2] + student[3] + student[4]  # 총점 업데이트
                student[6] = student[5] / 3  # 평균 업데이트
                print("성적이 수정되었습니다.")
                break
        if not found:
            print("해당 번호의 학생을 찾을 수 없습니다.")
    
    elif choice == '4':
        print("[ 학생성적삭제 ]")
        print()
        delete_no = int(input("삭제할 학생의 번호를 입력하세요: "))
        
        # 학생 번호에 해당하는 학생 찾기
        found = False
        for student in student_list:
            if student[0] == delete_no:
                found = True
                del student_list[delete_no]         
                print("학생 데이터가 삭제되었습니다.")
                break
        if not found:
            print("해당 번호의 학생을 찾을 수 없습니다.")
        
    
    else:
        print("올바른 번호를 입력해주세요.")

# print(student_list)