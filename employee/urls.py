#  Created by btrif Trif on 03-06-2022 , 2:24 PM.

from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('employee', views.EmployeeViewSet, basename='employee')

urlpatterns = [
    # path('', include(router.urls)),
    path("", views.apiOverview, name="api-overview"),
    path('average-age-industry/', views.averageAgeIndustry, name="average-age-industry"),
    path('average-salary-industry/', views.averageSalaryIndustry, name="average-salary-industry"),
    path('average-salary-experience/', views.averageSalaryExperience, name="average-salary-experience"),

]

# no Pain, no Gain - ModelViewSets
urlpatterns += router.urls
