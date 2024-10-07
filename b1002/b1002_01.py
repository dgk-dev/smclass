# 문자열

# slice 같은 기능
a = "123"
str1 = f"abcde{a}"
print(str1[2:]) #cde123
print(str1[:5]) #abcde
print(str1[0:5:2]) #ace [위치:위치:x칸씩]
print(str1[::-1]) #[처음:끝까지:역순으로]

# [] - 배열 : 배열은 한번 범위가 정해지면 수정이 불가 : C, 자바
# [] - 리스트 : 범위 상관 없음 : 파이썬




# input_str = input("글자를 입력하세요.")

# # 문자가 입력되지 않았을 때
# if input_str !== "": # 빈 공백이 아니냐?
#   print(f"입력문자 : {input_str}")
#   print(f"프로그램이 종료됩니다.")
# else:
#   print(f"글자를 입력하셔야 합니다.")
  
