numbers = [273, 103,5,32,65,9,72,800,99]

for idx, number in enumerate(numbers):
  if number >= 100:
    print(numbers[idx])

numbers.sort(reverse=True) # 역순 정렬
print(numbers)
numbers.reverse()
print(numbers) 



# # 리스트 함수
# a_list = [1,2,3,4,5,3,60,70]
# a_list.remove(3) # 입력된 값 리스트 삭제
# print(a_list)
# print(a_list.count(3))
# a_list.insert(0,100)
# print(a_list)

# 리스트 삭제
# a_list = [1,2,3,4,5]
# del a_list[0] # [2,3,4,5]
# a_list[1:3] = []
# a_list = None
# print(a_list)




# 리스트 수정방법
# a_list = [1,2,3,4,5,6,7]
# a_list[3] = 50 # 1개 변경
# a_list[1:2] = [20,30] # 2개 병경
# a_list[4] = [10, 20] # 리스트안에 리스트로 변경
# print(a_list)




# 리스트 출력방법
# a_list = [1,2,3,4,5]
# b_list = [50, 100]

# print(a_list[3]) # 4
# print(a_list[0:3]) # 1,2,3
# print(a_list[2:4]) # 3,4
# print(a_list[:3]) # 1,2,3
# print(a_list[3:]) # 4,5
# print(a_list+b_list) # [1, 2, 3, 4, 5, 50, 100]
# print(b_list * 3) # [50, 100, 50, 100, 50, 100]
# print(a_list[::2]) # [1, 3, 5]
# print(a_list[::-2]) # [5, 3, 1]
# print(a_list[::-1]) # [5, 4, 3, 2, 1]
# print(a_list[:]) # [1,2,3,4,5]




# a_list = [1,2,3,4,5]
# b_list = a_list[::-1]
# c_list = a_list
# print(a_list)
# print(b_list)
# print(c_list)
# a_list[0] = 100
# print(a_list)
# print(b_list)
# print(c_list)


# for i in range(1, len(a_list)+1):
#   print(a_list[-i])

# # 1-100 숫자가 들어간 리스트를 만드시오
# a_list = []

# # 첫 번째 방법
# for i in range(100):
#   a_list.append(i+1)
# print(a_list)


# # 두 번째 방법
# a_list = [i + 1 for i in range(100)]
# print(a_list)


# # 세 번째 방법
# a_list = list(range(1, 101))
# print(a_list)


 
 
# total = 0

# for i in range(10):
#   j = int(input(f"{i+1}번째 숫자를 입력하세요."))
#   a_list.append(j)
#   total += j

# for idx, a in enumerate(a_list):
#   a = int(input(f"{idx+1}번째 숫자를 입력하세요."))
#   total += a

# print(f"합계: {total}")


# a,b,c,d,e,f,g = 0,0,0,0,0
# total = 0

# # a,b,c,d,e의 변수에 숫자를 입력받아 합계를 출력하시오.
# a = int(input("숫자를 입력하세요."))
# b = int(input("숫자를 입력하세요."))
# c = int(input("숫자를 입력하세요."))
# d = int(input("숫자를 입력하세요."))
# e = int(input("숫자를 입력하세요."))

# print(f"합계: {a+b+c+d+e}")
