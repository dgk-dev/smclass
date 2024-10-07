import random

# 1-25까지 중복 없는 숫자 25개 추출
a_list = []

while len(a_list) < 25:
    num = random.randint(1, 25)
    if num not in a_list:
        a_list.append(num)

# [5, 5] 형태의 2차원 리스트로 변환
b_list = [a_list[i:i + 5] for i in range(0, 25, 5)]

print(b_list)
random.shuffle(b_list)
print(b_list)

while True:
  for i in range(5):
    for j in range(5):
      print(b_list[i][j],end='\t')
    print()
  input1 = input("좌표를 입력하세요.[0,1]>>")
  xa = int(input1[0]); ya = int(input1[-1])
  print(f"{input1} 좌표의 값: {b_list[xa][ya]}")
  

# for i in range(25):
#   a_list.append(i+1)
# b_list = random.choices(a_list,k=25)
# a_list = []
# c_list = []
# for i in range(25):
#   a_list.append(b_list[i])
#   if i % 5 == 0:
#     c_list.append(a_list)
#   a_list=[]

# print(c_list)