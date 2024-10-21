class Student:
    # 인스턴스 변수 - 객체선언을 하면 변수는 개별적으로 생성
    count = 0  # 클래스 변수

    def __init__(self, name, kor, eng, math):
        Student.count += 1
        self.no = Student.count  # 클래스 변수 - 공용으로 사용
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = (kor + eng + math) / 3
        self.rank = 0

    # 객체를 문자열리턴함수 - 리턴은 항상 문자열이 되어야 함.
    def __str__(self):
        return f'{"no":{self.no},"name":{self.name},"kor":{self.kor},"eng":{self.eng},"math":{self.math},"total":{self.total},"avg":{self.avg},"rank":{self.rank}}'

    def print(self):
        return {
            "no": self.no,
            "name": self.name,
            "kor": self.kor,
            "eng": self.eng,
            "math": self.math,
            "total": self.total,
            "avg": self.avg,
            "rank": self.rank,
        }


# students리스트 딕셔너리로 저장
students = []


s1 = Student("홍길동", 100, 100, 99)
print(s1.print())
students.append(s1.print())
print(s1)  # __str__() 정의 된 형태로 출력됨
s2 = Student("유관순", 90, 90, 99)
print(s2.print())
students.append(s2.print())
print(students)


# print(s1.name, s1.count)
# print(s2.name, s1.count)
# s1.print()
