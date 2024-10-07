# var1 = 100
# var2 = var1
# var3 = var2
# var4 = var3

# print(var4)

# v4 = v3 = v2 = v1 = 10
# print(v4)

# name = "홍길동"
# print(type(name))

# level = '3레벨'
# print(type(level))

# n = 3.14
# print(type(n))

# num = 100
# print(type(num))

# a_bool = True # True, Flase는 대문자로 넣어야함 - 파이썬만 대문자임
# print(type(a_bool))

#name,kor,eng,math,total,avg 출력
# 홍길동, 100, 100, 99, 합계, 평균 1줄에 출력하시오.
name = input("이름을 입력하시오.")
kor = int(input("한글 점수"))
eng = int(input("영어 점수"))
math = int(input("수학 점수"))
sum = kor + eng + math
avg = sum / 3

print(f"{name}의 점수는: {kor}, {eng}, {math} | 합계: {sum} | 평균: {avg:.2f}")



a = '100'
b = "200"
print(type(a))
print(type(b))

print(a+b) #문자연결연산자 100200
print(int(a)+int(b)) # 타입변경 300
name = "홍길동"
# print(int(name)) # 문자를 숫자로는 변경이 불가능, 문자숫자는 가능
c = 3.14
print(int(c)) # 실수 -> 정수, 소수점 날려버리기
print(c)
print(str(c))
print(bool(c)) # 0, null이 아닌 경우 True로 출력

c = "3.14"
print(int(float(c))) #문자실수형은 정수로 바로 바꿀 수 없고, 문자실수 -> 실수 -> 정수 이렇게 바꿔줘야함

d = "True"
print(bool(d)) #문자불형을 불형으로 변경 

# 타입 변경 - str,float,int,bool







