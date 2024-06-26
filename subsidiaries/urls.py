from django.urls import path
from . import views

urlpatterns = [
    path('subsidiaries/list/', views.SubsidiaryListView.as_view(), name='subsidiary_list'),
    path('subsidiaries/create/', views.SubsidiaryCreateView.as_view(), name='subsidiary_create'),
    path('subsidiaries/<int:pk>/detail/', views.SubsidiaryDetailView.as_view(), name='subsidiary_detail'),
    path('subsidiaries/<int:pk>/update/', views.SubsidiaryUpdateView.as_view(), name='subsidiary_update'),
    path('subsidiaries/<int:pk>/delete/', views.SubsidiaryDeleteView.as_view(), name='subsidiary_delete'),
]
