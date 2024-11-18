from django.shortcuts import render, redirect
from students.models import Student
from django.http import HttpResponse

# Create your views here.
def write(request):
    return render(request, "stu_write.html")

def save(request):
    print("학생정보저장 호출")
    if request.method == 'POST':
        # 모델 필드명과 일치하도록 수정
        student = Student(
            name=request.POST['name'],      # s_name이 아닌 name 사용
            major=request.POST['major'],    # s_major가 아닌 major 사용
            grade=request.POST['grade'],    # s_year가 아닌 grade 사용
            age=request.POST['age'],        # s_age가 아닌 age 사용
            gender=request.POST['gender']   # s_gender가 아닌 gender 사용
        )
        student.save()
        print("학생정보 저장완료")
    return redirect('index')

def list(request):
    # 모든 학생 데이터 조회
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'stu_list.html', context)


    
    


