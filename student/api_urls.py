# for API_URL
from django.urls import path, include
from rest_framework import routers
from student import views

router = routers.DefaultRouter()
router.register(r'', views.Studentviewset)

urlpatterns = [
    path('student/', include(router.urls)), 
]