from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeeList, name='employee_list'),
    path('employee_update/<int:id>', views.EmployeeUpdate, name='employee_update'),
    path('employee_delete/<int:id>', views.EmployeeDelete, name='employee_delete'),
    path('employee_delete/<int:id>', views.EmployeeDelete, name='employee_delete'),
    path('employee_api/', views.EmployeeApi),
 
]
