from django.urls import path
from . import views


urlpatterns = [
    path('production_movement/list/', views.ProductionMovementListView.as_view(), name='production_movement_list'),
    path('production_movement/create/', views.ProductionMovementCreateView.as_view(), name='production_movement_create'),
    path('production_movement/<int:pk>/detail/', views.ProductionMovementDetailView.as_view(), name='production_movement_detail'),
    path('production_movement/<int:pk>/update/', views.ProductionMovementUpdateView.as_view(), name='production_movement_update'),
    path('production_movement/<int:pk>/delete/', views.ProductionMovementDeleteView.as_view(), name='production_movement_delete'),
]
