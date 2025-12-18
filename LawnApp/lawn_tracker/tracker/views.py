from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import WorkDay, Yard, Employee
from .forms import EmployeeForm, YardForm, WorkDayForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.
def workday_list(request):
    workdays = WorkDay.objects.prefetch_related('yards_cut', 'staff').order_by('-date')
    template = loader.get_template('tracker/Workdays.html')
    context = {
        'workdays': workdays,
    }
    return HttpResponse(template.render(context, request))

def yard_list(request):
    yards = Yard.objects.all()
    return render(request, 'tracker/yard_list.html', {'yards':yards})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'tracker/employee_list.html', {'employees': employees})

def yard_detail(request, pk):
    yard = get_object_or_404(Yard, pk=pk)
    workdays = yard.work_day.order_by('-date')
    return render(request, 'tracker/yard_detail.html', {'yard': yard, 'work_day': workdays})

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'tracker/employee_detail.html', {'employee': employee})

@login_required
def new_workday(request):
    if request.method=="POST":
        form = WorkDayForm(request.POST)
        if form.is_valid():
            workday = form.save(commit=False)
            workday.date = timezone.now().date()
            workday.save()
            form.save_m2m()
            return redirect('workday_list')
    else:
        form = WorkDayForm()
    return render(request, 'tracker/new_workday.html', {'form':form})

@login_required
def new_yard(request):
    if request.method=="POST":
        form = YardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('yard_list')
    else:
        form = YardForm()
    return render(request, 'tracker/new_yard.html', {'form': form})

@login_required
def new_employee(request):
    if request.method=="POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'tracker/new_employee.html', {'form': form})