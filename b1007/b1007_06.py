import random

# 25개 1차원 리스트

# 25개 중 1을 5개 나머지는 0으로 입력해서 출력하시오

print([0]*20+[1]*5)
a_list = []
for i in range(25):
  if i < 20:
    a_list.append(0)
  else:
    a_list.append(1)
    
print(a_list)
  
  
# [5,5] 2차원리스트에 a_list의 값을 입력한 후 출력하시오

b_list = [a_list[i:i+5] for i in range(0, 25, 5)]
for i in range (5):
  for j in range (5):
    print(b_list[i][j], end="\t")
  print()

user_input = input("좌표를 입력하세요. (x,y)")
xa = int(user_input[0])
ya = int(user_input[-1])
print(f"좌표의 값은: {b_list[ya][xa]}")