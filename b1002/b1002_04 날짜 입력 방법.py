import datetime
today = datetime.datetime.now()

print(f"{today.year}년")
print(f"{today.month}월")
print(f"{today.day}일")
if today.hour >= 12:
  print("오후")
else:
  print("오전")
print(f"{today.hour}시")
print(f"{today.minute}분")
print(f"{today.second}초")

