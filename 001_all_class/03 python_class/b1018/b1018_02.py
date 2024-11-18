# class 생성방법

# 학생 1명 정보
# 번호, 이름, 국어, 영어, 수학, 합계, 평균, 등수
# 학생클래스 설계도 생성

# 매개변수가 있는 생성자
class Student:
  def __init__(self,no,name,kor,eng,math):  # 생성자
    self.no = no
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor+eng+math
    self.avg = (kor+eng+math)/3
    self.rank = 0
    
  def print(self):
    print(f"{self.no}\t{self.name}\t{self.kor}")



  def stu_input():
    pass
  
  def stu_output():
    pass
  
  
    
# 클래스 사용방법
# 클래스 선언
s1 = Student(1, "홍길동", 100,100,100)
s1.print()


  


# 전체학생리스트 정보
# class Students:
#   pass


