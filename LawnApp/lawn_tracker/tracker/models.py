from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Yard(models.Model):
    address = models.CharField(max_length=150)
    time = models.IntegerField(default=60)

    def __str__(self):
        return self.address


class WorkDay(models.Model):
    date = models.DateField(primary_key=True)
    staff = models.ManyToManyField(Employee, related_name='work_day')
    yards_cut = models.ManyToManyField(Yard, related_name='work_day')

    def __str__(self):
        return str(self.date)