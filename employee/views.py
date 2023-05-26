from django.shortcuts import render
from .models import Employee

# Create your views here.
def home(request):
    salary = Employee.objects.all().order_by('salaire')
    e22 = Employee.objects.filter(date_embauche__year='2022')
    alls = Employee.objects.all()
    return render(request, 'seedcorrection/employee/employee.html', {"salary": salary, 'e22': e22, "alls": alls})