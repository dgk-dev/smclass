from django.shortcuts import render, redirect

# 학생입력페이지 호출
def write(request):
  if request.method == 'GET':
    # render(): html 파일을 호출
    print("GET방식으로 들어옴")
    return render(request,'write.html')
  else:
    print("POST방식으로 들어옴")
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    print("입력데이터 : ",name,major,grade,age,gender)
    return redirect("/")

# # 학생입력저장
# def dowrite(request):
#   if request.method == 'POST':
#     name = request.POST['name']
#     major = request.POST['major']
#     grade = request.POST['grade']
#     age = request.POST['age']
#     gender = request.POST['gender']
#     print("입력데이터 : ",name,major,grade,age,gender)
#   else:
#     print("해당되는 데이터가 없습니다.")
#   return redirect("/")