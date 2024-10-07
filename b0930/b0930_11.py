yahoo = int(input("숫자를 입력하세요."))

if yahoo >= 50000:
  print(f"50000원 :{yahoo//50000}")
  yahoo %= 50000
if yahoo >= 10000:
  print(f"10000원 :{yahoo//10000}")
  yahoo %= 10000
if yahoo >= 5000:
  print(f"5000원 :{yahoo//5000}")
  yahoo %= 5000
if yahoo >= 1000:
  print(f"1000원 :{yahoo//1000}")
  yahoo %= 1000
if yahoo >= 500:
  print(f"500원 :{yahoo//500}")
  yahoo %= 500
if yahoo >= 100:
  print(f"100원 :{yahoo//100}")
  yahoo %= 100
if yahoo >= 50:
  print(f"50원 :{yahoo//50}")
  yahoo %= 50
if yahoo >= 10:
  print(f"10원 :{yahoo//10}")


# str1 = input("문자를 입력하세요.")
# a = len(str1)

# if a==5:
#   print("a는 5입니다.")
# elif a==4:
#   print("a는 4입니다.")
# elif a==3:
#   print("a는 3입니다.")
# else:
#   print("a는 2이하입니다.")
  