from django.urls import path
from . import views

urlpatterns = [
    path('employees/list/', views.EmployeeListView.as_view(), name='employee_list'),
    path('employees/create/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/<int:pk>/detail/', views.EmployeeDetailView.as_view(), name='employee_detail'),
]
