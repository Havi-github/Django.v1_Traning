from django.contrib import admin
from django.urls import path
from student import views
urlpatterns = [
    # path('student/', views.students,name='student'),
    path('', views.students, name='student'),
]
