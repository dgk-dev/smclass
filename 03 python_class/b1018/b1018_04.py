class Circle:
    def __init__(self, radius):
        # private 속성으로 변경
        self.__radius = radius
        self.area = 3.14 * radius * radius
        self.circumference = 3.14 * 2 * radius

    # Getter 메서드
    @property
    def radius(self):
        return self.__radius

    def print(self):
        print(f"넓이: {self.area:.2f} \n둘레: {self.circumference:.2f}")


# 사용 예시
c1 = Circle(50)
# setter를 통해 안전하게 반지름 변경
c1.__radius = 50
c1.print()

# 직접 변경 시도 (실패)
# c1.__radius = 30  # 외부에서 접근 불가
