from django.urls import path
from . import views


urlpatterns = [
    path('dispatch_production/list/', views.DispatchProductionListView.as_view(), name='dispatch_production_list'),
    path('dispatch_production/create/', views.DispatchProductionCreateView.as_view(), name='dispatch_production_create'),
    path('dispatch_production/<int:pk>/detail', views.DispatchProductionDetailView.as_view(), name='dispatch_production_detail'),
    path('dispatch_production/<int:pk>/update', views.DispatchProductionUpdateView.as_view(), name='dispatch_production_update'),
    path('dispatch_production/<int:pk>/delete', views.DispatchProductionDeleteView.as_view(), name='dispatch_production_delete'),
]
