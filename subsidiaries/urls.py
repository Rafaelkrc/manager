from django.urls import path
from . import views

urlpatterns = [
    path('subsidiaries/list/', views.SubsidiaryListView.as_view(), name='subsidiary_list')
]
