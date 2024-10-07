students = [
    [1, '홍길동', 100, 100, 99],
    [2, '유관순', 100, 100, 99],
    [3, '이순신', 100, 100, 99]
]

# 새로운 학생 추가
s = [4, '강감찬', 100, 100, 99]
students.append(s)

# 각 학생에 대해 합계와 평균 계산 후 추가
for student in students:
    scores = student[2:]  # 점수 부분 추출
    total = sum(scores)
    average = total / len(scores)
    student.append(total)
    student.append(average)

# 학생 정보 출력
for i, student in enumerate(students):
    student_id = i
    name = student[1]
    scores = student[2:-2]
    total = student[-2]
    average = student[-1]
    print(f"학생번호: {student_id}, 이름: {name}, 합계: {total}, 평균: {average:.2f}")

str = "12345"
for idx,data in enumerate(str):
  print(f"{idx}: {data}")

# # 문자열 슬라이싱
# str = "좋은 하루 되세요! 안녕히 가세요!"
# print(len(str))

# # 뒤쪽에서 5자리 전까지 출력
# print(str[-5:])
# print(str[-1])
# print(str[::-1])

# a_list = [1,2,3]

# a_list.append(10)

# a_list.insert(2,100)

# del a_list[1] # index 1번 삭제
# print(a_list)

# a_list.remove(100) # 100이라는 값으로 삭제
# print(a_list)