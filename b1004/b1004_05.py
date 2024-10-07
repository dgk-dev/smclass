# user_input = int(input("숫자를 입력하세요: "))

# for i in range(1, user_input + 1):
#     print(f"{i}단:")
#     for j in range(1, 10):  # 구구단은 1부터 9까지 곱합니다.
#         print(f"{i} * {j} = {i * j}")
#     print()  # 단과 단 사이에 빈 줄 추가
    
    
# for i in range(1, user_input + 1):
#   print(f"{i}단:")
#   for j in range(1, 10):
#     print(f"{i} x {j} = {i * j}")
#   print()




# user_input = int(input("숫자를 입력하세요."))

# print(f"{user_input}단:")
# for j in range(1, 9 + 1):
#   print(f"{user_input} x {j} = {user_input*j}")
# print()
  
#000 ~ #999


# for i in range(10):
#   for j in range(10):
#     for k in range(10):
#       print(f"{i}{j}{k}")
  
# for i in range(999 + 1):
#   print(f"{i:03d}")

a = 10

# print(f"{a:010.10f}")

# for문을 출력
for i in range(1,10):
  for j in range(1,10):
    print(f"{j} x {i} = {i*j}",end="\t")
  print()