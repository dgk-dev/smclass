import csv

list = ['10만','3,450','1.7만','500','1,000']

for idx, item in enumerate(list):
    if item.find('만') != -1:
        splitted = item.split("만")
        splitted[0] = float(splitted[0]) * 10000
        if splitted[1] == "":
            splitted[1] = 0
        else:
            splitted[1] = splitted[1].replace(",","")
        list[idx] = splitted[0] + float(splitted[1])
    else:
        list[idx] = float(item.replace(",",""))

# CSV 파일로 저장
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['value'])  # 헤더 작성
    for value in list:
        writer.writerow([value])

print("CSV 파일로 저장되었습니다: output.csv")
