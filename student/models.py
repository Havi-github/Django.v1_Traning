from django.db import models

# Create your models here.
class Student_table(models.Model):
    student_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.student_name} {self.father_name}"