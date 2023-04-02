from django.db import models

# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64, null=True, blank=True)
    gender = models.CharField(max_length=1, null=True, blank=True)
    date_of_birth = models.DateField()
    industry = models.CharField(max_length=64, null=True, blank=True)
    salary = models.FloatField(max_length=16, null=True, blank=True)
    years_of_experience = models.IntegerField(null=True, blank=True)



    def __str__(self):
        return f'Name : {self.first_name} {self.last_name}, E-mail:  {self.email}, ' \
               f'gender : {self.gender}, DOB : {self.date_of_birth}, Industry : {self.industry}, ' \
               f'Salary :{self.salary}, Years active : {self.years_of_experience}'