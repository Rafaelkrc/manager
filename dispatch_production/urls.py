from django.urls import path
from . import views


urlpatterns = [
    path('dispatch_production/list/', views.DispatchProductionListView.as_view(), name='dispatch_production_list')
]
