students = [
  [1,'홍길동',100,90,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99],
  [4,'강감찬',100,90,99],
  [5,'김구',90,90,99]
]

# 각 학생에 대해 합계와 평균 계산 후 추가
for student in students:
    scores = student[2:]  # 점수 부분 추출
    total = sum(scores)
    average = total / len(scores)
    student.append(total)
    student.append(average)

# 학생 정보 출력
for i, student in enumerate(students):
    student_id = i+1
    name = student[1]
    scores = student[2:-2]
    total = student[-2]
    average = student[-1]
    print(f"학생번호: {student_id}, 이름: {name}, 합계: {total}, 평균: {average:.2f}")