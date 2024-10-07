students = []
s_title = ["번호","이름","국어","영어","수학","합계","평균","등수"]
user_choice = 0 # 전역변수
stuNo = 0 # 학생 고유 번호
found = 0 # 체크변수
count = 0 # 성적처리
stuNo = len(students) # 리스트에 학생이 있으면, 그 인원으로 숫자 변경
no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0 # 성적처리변수

while True:
  print("[ 학생성적 프로그램 ]")
  print("-"*60)
  print("1.학생성적입력")
  print("2.학생성적출력")
  print("3.학생성적수정")
  print("4.학생성적검색")
  print("5.학생성적삭제")
  print("6.등수처리")
  print("0.프로그램 종료")
  print("-"*60)
  user_choice = input("원하는 번호를 입력하세요.>> ")
  if user_choice =="1":
    while True:
      print("[ 학생성적입력 ]")
      no = stuNo + 1
      name = input(f"{no}번째 학생 이름을 입력하세요.(0. 이전화면) >>")
      if name == "0":
        print("성적입력을 취소합니다.")
        print()
        break
      kor = int(input("국어점수를 입력하세요."))
      eng = int(input("영어점수를 입력하세요."))
      math = int(input("수학점수를 입력하세요."))
      total = kor+eng+math
      avg = total/3
      students.append([no,name,kor,eng,math,total,avg,rank])
      stuNo += 1 #학생 수 증가
      print(f"{name} 학생의 성적이 저장되었습니다.")
      print()
      
  elif user_choice == "2":
    # 상단타이틀 출력
    print("[ 학생성적출력 ]")
    for title in s_title:
      print(f"{title}\t",end="")
    print()
    # print(f"{s_title[0]}\t{s_title[1]}\t{s_title[2]}\t{s_title[3]}\t{s_title[4]}\t{s_title[5]}\t{s_title[6]}\t{s_title[7]}\n")
    print("-" * 60)
    
    # 학생출력
    for s in students:
      print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\n")
      
  elif user_choice =="3":
    print("[ 학생성적수정 ]")
    user_name = input("수정하고자 하는 학생의 이름을 입력하세요.")
    found = 0
    for s in students:
      if s[1] == user_name:
        print(f"{user_name} 학생을 찾았습니다.")
        print()
        print(f"현재 {user_name} 학생의 점수는 국어: {s[2]}, 영어: {s[3]} 수학: {s[4]} 입니다.")
        s[2] = int(input("변경된 국어 점수:"))
        s[3] = int(input("변경된 영어 점수:"))
        s[4] = int(input("변경된 수학 점수:"))
        s[-3] = s[2]+s[3]+s[4]
        s[-2] = s[-3] / 3
        print("변경된 점수는 아래와 같습니다.")
        print()
        for title in s_title:
         print(f"{title}\t",end="")
        print()
        print("-" * 60)
        print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\n")
        found = 1
        
    if found == 0:
      print(f"{user_name} 학생이 없습니다. 다시 입력하세요.")
      print()
    print()
    
  elif user_choice =="4":
    print("[ 학생성적검색 ]")
    user_name = input("찾고자 하는 학생의 이름을 입력하세요.")
    found = 0
    for s in students:
      if s[1] == user_name:
        print(f"{user_name} 학생을 찾았습니다.")
        print()
        for title in s_title:
          print(f"{title}\t",end="")
        print()
        print("-" * 60)
        print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\n")
        print()
        print()
        found = 1
      
    if found == 0:
      print(f"{user_name} 학생이 없습니다. 다시 입력하세요.")
      print()
    
  elif user_choice =="5":
    print("[ 학생성적삭제 ]")
    user_name = input("찾고자 하는 학생의 이름을 입력하세요.")
    found = 0
    for idx, s in enumerate(students):
      if s[1] == user_name:
        found = 1
        user_choice = input(f"{user_name} 학생을 삭제하시겠습니까?(삭제시 복구불가)\n1.삭제 2.취소")
        if user_choice == "1":
          del students[idx]
          print(f"{user_name} 학생이 삭제되었습니다.")
        else:
          print("학생성적 삭제가 취소되었습니다.")
          break
      
    if found == 0:
      print(f"{user_name} 학생이 없습니다. 다시 입력하세요.")
      print()
  
  elif user_choice == "6":
    print("[ 등수처리 ]")
    for s in students:
      count = 1
      for st in students:
        if s[5] < st[5]:
          count += 1
      s[-1] = count # 등수입력
    print("등수처리가 완료되었습니다.")
    print()
      
      
    
  elif user_choice == "0":
    print("[ 프로그램종료 ]")
    print("프로그램을 종료합니다.")
    break
  
  