from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=10)
    major = models.CharField(max_length=20)
    grade = models.IntegerField(default=1)
    age = models.IntegerField(default=18)
    gender = models.CharField(max_length=1, default='M')

    def __str__(self):
        return self.name

    
