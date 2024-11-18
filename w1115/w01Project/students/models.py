from django.db import models

## db생성
class Student(models.Model):
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    grade = models.IntegerField(default=1)
    age = models.IntegerField(default=20)
    gender = models.CharField(max_length=1, default='M')

    def __str__(self):
        return self.name
    

