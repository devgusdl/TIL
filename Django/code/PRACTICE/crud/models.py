from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    major = models.CharField(max_length=10)
    description = models.TextField()


class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    rank = models.IntegerField()
    # 학생 정보
