from django.shortcuts import render
from django.http import HttpResponse
from .models import Student_table
from django.contrib import messages


#for API Purpose
from django.contrib.auth.models import User  # this id for API
from rest_framework import viewsets  #   this is for the API  
from student.serializers import StudentSerializer  # this is for API
#
class Studentviewset(viewsets.ModelViewSet):
    queryset = Student_table.objects.all()
    serializer_class = StudentSerializer












# Create your views here.
def students(request):
    if request.method == 'POST':
        students = Student_table.objects.all()[:3]  # Fetch only the first 3 rows
        messages.success(request, "Student information submitted successfully!")
        s_name = request.POST['student_name']
        f_name = request.POST['father_name']
        age = request.POST['age']
        gender = request.POST['gender']
        email = request.POST['email']

        if len(s_name) <2:
            return HttpResponse('ERROR, Student name is to short')
        else:

            New_student = Student_table(student_name=s_name,father_name=f_name,age=age,gender=gender,email=email)
            New_student.save()
     
    return render(request,'studentR.html')
   