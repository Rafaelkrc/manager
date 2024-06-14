from django.urls import path
from . import views

urlpatterns = [
    path('subsidiaries/list/', views.SubsidiaryListView.as_view(), name='subsidiary_list'),
    path('subsidiaries/create/', views.SubsidiaryCreateView.as_view(), name='subsidiary_create'),
    path('subsidiaries/<int:pk>/detail/', views.SubsidiaryDetailView.as_view(), name='subsidiary_detail'),
]
