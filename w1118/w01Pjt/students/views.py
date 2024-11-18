from django.shortcuts import render

def write(request):
    return render(request, "write.html")

def list(request):
    return render(request, "list.html")

