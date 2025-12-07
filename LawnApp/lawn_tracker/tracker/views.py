from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import WorkDay

# Create your views here.
def workday_list(request):
    workdays = WorkDay.objects.prefetch_related('yards_cut', 'staff').order_by('date')
    template = loader.get_template('Workdays.html')
    context = {
        'workdays': workdays,
    }
    return HttpResponse(template.render(context, request))