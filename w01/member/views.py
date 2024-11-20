from django.shortcuts import render
from member.models import Member

def mlist(request):
  qs = Member.objects.all()
  context = {"mlist":qs}
  return render(request,'mlist.html',context)
