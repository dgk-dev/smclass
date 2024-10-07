# 로또 당첨 프로그램

a_list = [
  [0,1,0],
  [0,0,1],
  [1,0,0]
]

for i in range(3):
  for j in range(3):
    pass


print(a_list)
user_input = input("좌표를 입력하세요.")
if a_list[int(user_input[0])][int(user_input[-1])] == 1:
  print("당첨")
  print(a_list[int(user_input[0])][int(user_input[-1])])
else:
  print("노당첨")
  
