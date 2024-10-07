# 입력한 숫자가 짝수인지, 홀수인지 출력하시오.

user_input = int(input("숫자를 입력하세요."))

# if user_input % 2 == 0:
#   print(f"짝수입니다.")
# else:
#   print(f"홀수입니다.")

# 입력한 숫자가 1보다 크고 10보다 작을때만 정답입니다.

# if 10 >= user_input or 100 <= user_input:
#   print(f"정답")
# else:
#   print(f"오답")
  
# if 0 < user_input / 3 < 1 or user_input == 12:
#   print("겨울입니다")
# elif user_input / 3 < 2:
#   print("봄입니다")
# elif user_input / 3 < 3:
#   print("여름입니다")
# elif user_input / 3 < 4:
#   print("가을입니다")
# else:
#   print("숫자를 잘못 입력하셨습니다.")

score = ""  

if 100 >= user_input >= 90:
  score += "A"
  if user_input >= 98:
    score += "+"
  elif user_input <= 93:
    score += "-"
elif 89 >= user_input >= 80:
  score += "B"
  if user_input >= 88:
    score += "+"
  elif user_input <= 83:
    score += "-"
elif 79 >= user_input >= 70:
  score += "C"
  if user_input >= 78:
    score += "+"
  elif user_input <= 73:
    score += "-"
elif user_input >= 60:
  score += "D"
else:
  score += "F"
  
print(score)
    
  
  



# 숫자를 입력받아 100보다 큰수인지 작은수인지 출력하시오.

# user_input = float(input("숫자를 입력하세요."))
# if user_input > 100:
#   print(f"100보다 큰 수 입니다.")
# elif user_input == 100:
#   print(f"100과 같습니다.")
# else:
#   print(f"100보다 작은 수입니다.")
  
  

# a = 100
# if a>10:
#   print(f"10보다 큰수입니다.")
  
# if a>10:
#   #if 문에는 1줄이 있어야 에러가 나지 않음, 아무것도 넣지 않을려면 pass를 넣으면 됨.
#   pass