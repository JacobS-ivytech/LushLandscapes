from django.urls import path
from . import views

urlpatterns = [
    path('workday_list/', views.workday_list, name ='workday_list'),
]