#  Created by btrif Trif on 03-06-2022 , 3:25 PM.
from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # fields = ('id', 'first_name', 'last_name', 'email', 'gender', 'date_of_birth', 'industry', 'salary', 'years_of_experience')
        fields = '__all__'

