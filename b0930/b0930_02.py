# 10은 2의 배수

# 프린트 사용 방법
# print("%d은 %d의 배수입니다." % (10, 2))
# a = 10
# b = 2
# print(a,b)

# 출력 자리수
# print("%d" % b)
# print("%5d" % b) # 공간 5자리를 확보
# print("%05d" % b) 


### 001 010 100.00
# num = 1
# num2 = 10
# num3 = 100
# print("%03d" % num) 
# print("%03d" % num2) 
# print("%.2f" % num3) 
# print("%03d %03d %.2f" % (num, num2, num3)) 

print("%5d" % (-10))

num4 = 758.12345678
print(f"{num4:.2f}")

num5 = 25.05
print(f"{num5:013.2f}")

num6 = 150.15
# 문자(String)로 출력
print(f"{str(num6)}")  # 문자로 출력: 150.15

# 정수(Integer)로 출력 (소수점을 버리고 정수로 변환)
print(f"{int(num6)}")  # 정수로 출력: 150

# 실수(Float)로 출력 (소수점 이하 2자리까지)
print(f"{num6:.2f}")  # 실수로 출력: 150.15

str = "안"
print(10+10)
print("안녕 "+"hello")
print(f"안녕 {str}하세요." * 9)
print(f"{123456789.123:5.3f}")


# 10*2=20
# print("%d * %d = %d" % (a,b,a*b))

# 사용 표시 = %s:문자열, %c:문자1개, %f: 실수, %d: 정수
# name = "홍길동"
# kor = 100
# eng = 100
# math = 99

# print("%s 총합 : %d, 평균 : %.2f" % (name, kor+eng+math, (kor+eng+math)/3))



# print(a,"은",b,"의 배수입니다.")
# print("%d은 %d의 배수입니다." % (a, b))
# print("{}은 {}의 배수입니다." .format(a,b))

# 아래 방법이 가장 최신
# print(f"{a}은 {b}의 배수입니다.")

