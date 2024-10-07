students = [
  [1,'홍길동',100,90,99],
  [2,'유관순',100,87,99],
  [3,'이순신',100,66,99],
  [4,'강감찬',100,97,99],
  [5,'김구',90,77,99]
]

# 각 학생에 대해 합계와 평균 계산 후 추가
for student in students:
    scores = student[2:]  # 점수 부분 추출
    total = sum(scores)
    average = total / len(scores)
    student.append(total)
    student.append(average)
    student.append(0)

s_title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']
for s in s_title:
  print(s,end="\t")
print();print("-" * 60)

# 학생 정보 출력
for idx, student in enumerate(students):
    student_id = idx+1
    name = student[1]
    kor = student[2]
    eng = student[3]
    math = student[4]
    total = student[-3]
    average = student[-2]
    rank = student[-1]
    print(f"{student_id}\t{name}\t{kor}\t{eng}\t{math}\t{total}\t{average:.2f}\t{rank}")