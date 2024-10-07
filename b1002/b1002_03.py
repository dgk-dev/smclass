user_input = int(input("숫자를 입력하세요."))

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