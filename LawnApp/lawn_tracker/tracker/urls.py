from django.urls import path, include
from . import views
from django.contrib import admin
from django.contrib.auth import views as v

urlpatterns = [
    path('', views.workday_list, name ='workday_list'),
    path('admin/', admin.site.urls),
    path('yard/<int:pk>/', views.yard_detail, name='yard_detail'),
    path('employee/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('accounts/login/', v.LoginView.as_view(), name='login'),
    path('accounts/logout/', v.LogoutView.as_view(next_page='/'), name='logout'),
    path('new/workday/', views.new_workday, name='new_workday'),
    path('new/yard/', views.new_yard, name='new_yard'),
    path('new/employee/', views.new_employee, name='new_employee'),
    path('yards/', views.yard_list, name='yard_list'),
    path('employees/', views.employee_list, name='employee_list')
]