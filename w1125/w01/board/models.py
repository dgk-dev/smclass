from django.db import models
from member.models import Member

class Board(models.Model):
  bno = models.AutoField(primary_key=True)
  member = models.ForeignKey(Member,on_delete=models.DO_NOTHING,null=True)
  btitle = models.CharField(max_length=1000)
  bcontent = models.TextField()
  # 계층형 게시판
  bgroup = models.IntegerField(null=True)
  bstep = models.IntegerField(default=0)
  bindent = models.IntegerField(default=0)
  bhit = models.IntegerField(default=0)
  bdate = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.bno}, {self.btitle}, {self.bgroup}, {self.bdate}"