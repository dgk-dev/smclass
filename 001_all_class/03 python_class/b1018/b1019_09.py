students = []


class StudentNumberTracker:
    def __init__(self):
        self.current = 0

    def getNextNumber(self):
        self.current += 1
        return self.current


# 클래스 생성
class Student:
    def __init__(self, name, kor, eng, math):
        self.__no = number_tracker.getNextNumber()
        self.name = name  # 인스턴스 변수: 객체선언할 때 만들어짐, 각각의 객체마다 변수가 생성됨.
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = (kor + eng + math) / 3
        self.rank = 0
        students.append(self)  # 학생 리스트에 추가

    def __str__(self):
        return f"{self.__no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}\t{self.rank}"

    def get_no(self):
        return self.__no

    def set_no(self, no):
        if no < 0:
            raise "0이하는 입력을 할 수 없습니다."
        self.__no = no

    def update_scores(self, kor=None, eng=None, math=None):
        if kor is not None:
            self.kor = kor
        if eng is not None:
            self.eng = eng
        if math is not None:
            self.math = math
        self.total = self.kor + self.eng + self.math
        self.avg = (self.kor + self.eng + self.math) / 3

    @classmethod
    def stu_print(cls):
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
        print("-" * 50)
        for s in students:
            print(s)

    @classmethod
    def update_student(cls):
        try:
            no = int(input("수정할 학생의 번호를 입력하세요: "))
            student = next((s for s in students if s.get_no() == no), None)
            if student is None:
                print("해당 번호의 학생을 찾을 수 없습니다.")
                return
            kor = input("새로운 국어 점수를 입력하세요 (변경하지 않으려면 Enter): ")
            eng = input("새로운 영어 점수를 입력하세요 (변경하지 않으려면 Enter): ")
            math = input("새로운 수학 점수를 입력하세요 (변경하지 않으려면 Enter): ")
            student.update_scores(kor=int(kor) if kor else None, eng=int(eng) if eng else None, math=int(math) if math else None)
            print("학생 성적이 수정되었습니다.")
        except ValueError:
            print("잘못된 입력입니다. 숫자로 점수를 입력해주세요.")


number_tracker = StudentNumberTracker()

# 학생 성적 입력 받기
while True:
    name = input("학생 이름을 입력하세요 (종료하려면 '종료' 입력): ")
    if name == '종료':
        break
    try:
        kor = int(input("국어 점수를 입력하세요: "))
        eng = int(input("영어 점수를 입력하세요: "))
        math = int(input("수학 점수를 입력하세요: "))
    except ValueError:
        print("잘못된 입력입니다. 숫자로 점수를 입력해주세요.")
        continue

    Student(name, kor, eng, math)

# 학생 정보 출력 및 수정 옵션 제공
while True:
    action = input("학생 정보를 출력하려면 '출력', 성적을 수정하려면 '수정', 종료하려면 '종료'를 입력하세요: ")
    if action == '출력':
        Student.stu_print()
    elif action == '수정':
        Student.update_student()
    elif action == '종료':
        break
    else:
        print("잘못된 입력입니다. 다시 시도해주세요.")
