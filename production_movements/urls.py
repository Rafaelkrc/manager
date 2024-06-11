from django.urls import path
from . import views


urlpatterns = [
    path('production_movement/list/', views.ProductionMovementListView.as_view(), name='production_movement_list')
]
