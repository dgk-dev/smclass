# 1,3,5,7,9 ...99 합계를 구하시오

# sum = 0
# for i in range(1,99+1, 2):
#     sum += i
    
# print(sum)

# 두수를 입력받아, 두수까지 합계를 구하시오
# 예) 3, 8 -> 3+4+5+6+7+8

# if문 사용
# user_input1 = int(input("숫자1"))
# user_input2 = int(input("숫자2"))
# sum = 0
# for i in range (min(user_input1, user_input2), max(user_input1, user_input2) + 1):
#   sum += i

# print(sum)
  
user_input1 = int(input("숫자1"))
user_input2 = int(input("숫자2"))
sum = 0

if user_input1 > user_input2:
  user_input1, user_input2 = user_input2, user_input1
  
for i in range(user_input1, user_input2 + 1):
  sum += i
  


print(sum)



