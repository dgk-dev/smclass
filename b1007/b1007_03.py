# [3,3] 리스트 [1,2,3],[4,5,6],[7,8,9]

# a_list = [
#   [1,2,3],
#   [3,4,5],
#   [6,7,8]
# ]

# b_list=[]
# for i in range(3):
#   a=[]
#   for j in range(1,4):
#     a.append(3*i+j)
#   b_list.append(a)
# print(b_list)

# a_list=[]
# for i in range(9):
#   a_list.append(i+1)
# print(a_list)

# 첫번째 버전
a_list=[]
a=[]
for i in range(1, 10):
  a.append(i)
  if(i%3)==0:
    a_list.append(a)
    a=[]
print(a_list)

# 다른 버전
b_list = [[i, i+1, i+2] for i in range(1, 10, 3)]
print(b_list)

# 3번째 버전
d_list = []
for i in range (1,10,3):
  d_list.append([i, i+1, i+2]);
print(d_list)


# for문을 작성해서 5,5 작성
c_list = [[i, i+1, i+2, i+3, i+4] for i in range (1,25,5)]
print(c_list)

  
    
  







# # 2차원 리스트
# a_list = [
#   [1,2,3,4],
#   [5,6,7,8],
#   [9,10,11,12]
# ]

# for list in list_lists:
#   for numbers in list:
#     print(numbers)
