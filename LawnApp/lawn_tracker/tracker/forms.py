from django import forms
from .models import Employee, Yard, WorkDay

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('name', 'contact')

class YardForm(forms.ModelForm):

    class Meta:
        model = Yard
        fields = ('address', 'time')

class WorkDayForm(forms.ModelForm):

    class Meta:
        model = WorkDay
        fields = ('staff', 'yards_cut')