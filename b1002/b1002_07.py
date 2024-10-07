all_list = [
 [1, '홍길동',100, 90, 90],
 [1, '유관순',100, 90, 90],
 [1, '이순신',100, 90, 90],
 [1, '강감찬',100, 90, 90],
 [1, '김구',100, 90, 90]
]

a = input("이름을 입력하세요.")
tested = False

for idx, list in enumerate(all_list):
  if a==list[1]:
    del all_list[idx]
    tested = True

if not tested:
  print("이름이 없습니다")
  
print("테스트가 완료되었습니다.")
    
    
# print(all_list)


# 이름을 입력받아 같은 이름이 있으면 데이터 삭제, 없으면 없습니다. 출력하시요.



# aArr = [2,3,4,6,7,8,9,10]

# aArr.extend([50, 100])
# print(aArr)
# aArr.insert(1, 30)
# print(aArr)
# aArr.remove(6)
# print(aArr)
# del aArr[0]; del aArr[3]
# print(aArr)