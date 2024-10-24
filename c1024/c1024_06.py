list = ['10억','9억5,000','11억 500','7억','12억']


# list = [item.split("억") for item in list]
# result = []

# for item in list:
#     if item[0] != '':
#         item[0] = int(item[0].replace(",",""))*100000000
#     else:
#         item[0] = 0
#     if item[1] != '':
#         item[1] = int(item[1].replace(",",""))*10000
#     else:
#         item[1] = 0
#     result.append(item[0] + item[1])



# print(result)

def convert_to_numbers(item):
    splited = item.split("억")
    uk_won = int(splited[0])*100000000 if splited[0] else 0
    man_won = int(splited[1].replace(",",""))*10000 if splited[1] else 0
    return uk_won+man_won

list = [convert_to_numbers(item) for item in list]
print(list)