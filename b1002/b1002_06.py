students = [
    [1, '홍길동', 100, 100, 99],
    [2, '유관순', 100, 100, 99],
    [3, '이순신', 100, 100, 99]
]

for idx, student in enumerate(students):
  if student[1] == '이순신':
    del students[idx] # index로 구함
    # students.remove(student) # 값으로 구함

print(students)  


