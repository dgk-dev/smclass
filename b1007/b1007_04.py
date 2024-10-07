import random

# a_list = []

# while len(a_list) < 25:
#   num = random.randint(1, 25)
#   if num not in a_list:
#     a_list.append(num)

# print(a_list)

a_list = []
for i in range(25):
  a_list.append(i+1)

b_list = random.sample(a_list,25)

a_list = []
for i in range(25):
  a_list.append(i+1)
  
b_list = random.choices(a_list,k=25)

print(a_list)
print(b_list)
# # a_list = [1,2,3,4,5,6,7,8,9]

# a_list = []
# for i in range (1,10,3):
#   a_list.append([i, i+1, i+2]);
# print(a_list)

# a_list=[]
# for i in range(25):
#   a_list.append(i+1)
# print(a_list)

# # 1차원리스트 -> 2차원리스트 변경
# b_list = []
# for i in range(0,len(a_list),5):
#   b_list.append(a_list[i:i+5])
# print(b_list)