stu_title = ['번호', '이름', '국어', '영어', '수학', '과학', '합계', '평균']
stu_datas = [
    ["홍길동", 100, 100, 100, 99],
    ["유관순", 99, 99, 100, 99],
    ["이순신", 100, 99, 98, 99],
    ["김구", 80, 100, 100, 99],
    ["김유신", 97, 89, 77, 99],
    ["강규석", 97, 89, 77, 99]
]


for id, stu_data in enumerate(stu_datas, start=1):
  stu_sum = sum(stu_data[1:])
  stu_data.insert(0, id)
  stu_data.insert(len(stu_data)-1,stu_sum)
  stu_data.append(stu_sum/len(stu_data[1:5])) # 합계 / 4
  print("\t".join(map(str, stu_data)))
