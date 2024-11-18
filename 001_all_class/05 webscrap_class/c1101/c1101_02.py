import datetime

print(datetime.datetime.now().year)
nowYear = datetime.datetime.now().year

in_year = input("생일입력: ")
print(nowYear - int(in_year[:4]))
