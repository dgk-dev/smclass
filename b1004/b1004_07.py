## 구구단을 출력

i = 0
while(i<10):
  print(i)
  i += 1

for i in range(10):
  print(i)
  
  s_list = []
no = 1

while True:
  # 번호, 이름, 국어, 영어, 수학 -> 번호, 이름, 국어, 영어, 수학, 합계, 평균
  print("이름을 입력하세요.")
  name = input("이름을 입력하세요. (종료 : 0)")
  if name == '0':
    break
  kor = int(input("국어점수를 입력하세요."))
  eng = int(input("영어점수를 입력하세요."))
  math = int(input("수학점수를 입력하세요."))
  print(f"번호: {no}, 이름: {name}, 국어: {kor}, 영어: {eng} 수학: {math}, 합계: {kor+eng+math}, 평균: {(kor+eng+math)/3:.2f}")
  no += 1
  
print("프로그램을 종료합니다.")


  


# 두수를 입력받아 +,-,*,/

# while True:
#   num = int(input("숫자를 입력하세요."))
#   num2 = int(input("숫자를 입력하세요.(종료:0)"))
  
#   if num2 == 0:
#     break 
  
#   print(f"[ 두수의 사칙연산 ]")
#   print(f"-" * 50)
#   print(f"1. 두수 더하기")
#   print(f"2. 두수 빼기")
#   print(f"3. 두수 곱하기")
#   print(f"4. 두수 나누기")
#   print(f"-" * 50)
#   choice = int(input("원하는 번호를 입력하세요.>>"))
#   if choice == 1:
#     print(f"결과값 : {num+num2}")
#   elif choice == 2:
#     print(f"결과값 : {num-num2}")
#   elif choice == 3:
#     print(f"결과값 : {num*num2}")
#   elif choice == 4:
#     print(f"결과값 : {num/num2}")
    