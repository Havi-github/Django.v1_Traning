from rest_framework import serializers #library
from django.contrib.auth.models import User #autantication


#from_framework import serializers
from.models import Student_table

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_table
        fields = '__all__' #include all fields , all means all table filed