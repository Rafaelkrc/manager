from django.urls import path
from . import views


urlpatterns = [
    path('production_setor/list/', views.ProductionSectorListView.as_view(), name='production_sector_list')
]
