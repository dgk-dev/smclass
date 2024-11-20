from django.shortcuts import render

def product_form(request):
    return render(request, 'product_form.html')
