# 원의 넓이 : 반지름 * 반지름 * 3.14
# 반지름을 입력받아, 원의 넓이를 구하시오.

# user_radius = float(input(f"반지름을 입력하세요."))
# circle_space = user_radius ** 2 * 3.14
# print(round(circle_space, 3))

# 길이를 입력받아, 삼각형의 넓이, 직사각형의 넓이를 구하시오
# user_height = float(input("세로를 입력하세요."))
# user_width = float(input("가로를 입력하세요."))
# rectangle = user_height*user_width
# triangle = rectangle / 2

# print(f"{triangle}, {rectangle}")


# user_input = input("두개 내놔")
# list = user_input.split(" ")
# triangle = float(list[0]) * float(list[1]) / 2
# print(triangle)

stu_title = ['번호', '이름', '국어', '영어', '수학', '과학', '합계', '평균']
stu_datas = [
    ["홍길동", 100, 100, 100, 99],
    ["유관순", 99, 99, 100, 99],
    ["이순신", 100, 99, 98, 99],
    ["김구", 80, 100, 100, 99],
    ["김유신", 97, 89, 77, 99]
]

# Print title with tab separation
print("\t".join(stu_title))  
print("-" * 60)

# stu_datas를 돌면서 한명씩 출력
for id, stu_data in enumerate(stu_datas, start=1):
    total_score = sum(stu_data[1:])  # 점수 전체의 합
    average_score = total_score / len(stu_data[1:])  # 평균 구하기
    
    # 번호 + 학생 데이터 + 합계 + 평균
    result_data = [id] + stu_data + [total_score, f"{average_score:.2f}"]
    
    # 탭으로 조인
    print("\t".join(map(str, result_data)))

print(map(str, result_data))

del a_list[0]





### 복합대입연산자 +=, -=, *=,

# a = 10
# a += 5;print(a) # 15
# a -= 5;print(a) # 10
# a *= 5;print(a) # 50
# a /= 5;print(a) # 10
# a //= 5;print(a) # 2
# a %= 5;print(a) # 2
# a **= 5;print(a) # 32




# 두수를 입력받아 더하기, 빼기, 곱하기, 나누기를 출력하시오.

# input_1 = int(input("숫자1을 입력하시오."))
# input_2 = int(input("숫자2를 입력하시오."))

# plus = input_1 + input_2
# minus = input_1 - input_2
# multiply = input_1 * input_2
# divide = input_1 / input_2

# print(f"{type(plus)}, {type(minus)}, {type(multiply)}, {type(divide)}")
# print(f"{type(plus)}, {type(minus)}, {type(multiply)}, {type(divide)}")

# a=0
# for i in range(1,11):
#   a += i
#   print(a)

# // - 정수형태 몫, ** - 제곱


# print(5+2) # 7
# print(5-2) # 3
# print(5*2) # 10
# print(5/2) # 2.5
# print(5%2) # 1
# print(5//2) # 2 - 정수형태 몫
# print(5**2) # 25 - 제곱
# print(3**2) # 9
# print(4**4) # 4*4*4*4 

#불형

# a = (10>100)
# print(a)

# b = (10==10)
# print(b)
# print(type(b))

# # 문자열
# print(f"안녕 영어로는 \"hello\" 입니다.")

# # 함수 선언
# def add() :
#   print(10+9)

# add()

## 파이썬에는 ++, --가 없음

# # 여러 줄을 한 줄 형태로 표현
# # 1줄 선언 방식
# a=10;b=5

# # 1줄 선언 방식
# s1,s2,s3 = 1,2,3
# c,d=4,5

