import csv

# 리스트 내포
# a = [1,2,3,4,5]
# b = [x**2 for x in a]
# print(b)

st_list = ['순위', '종목명', '검색비율', '현재가', '전일비', '등락률', '거래량', '시가', '고가', '저가', 'PER', 'ROE']
sto_list = ['1', '삼성전자', '11.68%', '57,800', '상승100', '+0.17%', '7,670,225', '57,500', '58,200', '57,100', '14.13', '4.15']
sto_list2 = ['2', 'SK하이닉스', '3.25%', '190,600', '상승2,800', '+1.49%', '747,655', '188,500', '191,800', '188,000', '55.54', '-15.61']

# csv파일로 저장시 한글인코딩: utf-8-sig
with open('smclass/c1023/a.csv','w',encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(st_list)
    writer.writerow(sto_list)
    writer.writerow(sto_list2)



# with open('smclass/c1023/list.txt','w',encoding='utf-8') as f:
#     f.writerow(st_list)
#     f.writerow(sto_list)
#     f.writerow(sto_list2)


