from django.urls import path
from . import views


urlpatterns = [
    path('production_setor/list/', views.ProductionSectorListView.as_view(), name='production_sector_list'),
    path('production_setor/create/', views.ProductionSectorCreateView.as_view(), name='production_sector_create'),
    path('production_sector/<int:pk>/detail/', views.ProductionSectorDetailView.as_view(), name='production_sector_detail'),
    path('production_sector/<int:pk>/update/', views.ProductionSectorUpdateView.as_view(), name='production_sector_update'),
    path('production_sector/<int:pk>/delete/', views.ProductionSectorDeleteView.as_view(), name='production_sector_delete'),
]
