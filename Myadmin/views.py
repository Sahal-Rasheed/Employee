from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib import messages
from Employee.models import Employee
from Employee.forms import EmployeeForm
from Employee.serializers import EmployeeSerializer
# Create your views here.


def EmployeeList(request):
    employees = Employee.objects.all()
    return render(request, 'myadmin/employee_list.html',{'employees':employees})

def EmployeeUpdate(request ,id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(data=request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated')
            return redirect('employee_list')
        else:
            messages.error(request, 'Failed')
            return redirect('employee_list')
        
    form = EmployeeForm(instance=employee)
    return render(request, 'myadmin/employee_update.html',{'form':form})
    
def EmployeeDelete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('employee_list')

@api_view(['GET'])
def EmployeeApi(request):
    employee = Employee.objects.all()
    employee_serializer = EmployeeSerializer(employee,many=True)
    return Response(data=employee_serializer.data)
    



