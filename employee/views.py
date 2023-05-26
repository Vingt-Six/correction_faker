from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def home(request):
    salary = Employee.objects.all().order_by('salaire')
    e22 = Employee.objects.filter(date_embauche__year='2022')
    alls = Employee.objects.all()
    return render(request, 'seedcorrection/employee/employee.html', {"salary": salary, 'e22': e22, "alls": alls})

def createemployee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm()
    return render(request, 'seedcorrection/employee/createemployee.html', {"form": form})