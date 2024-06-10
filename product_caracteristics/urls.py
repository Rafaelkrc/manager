from django.urls import path
from . import views


urlpatterns = [
    path('product_caracteristics/group/', views.GroupListView.as_view(), name='group_list'),
    path('product_caracteristics/brand/', views.BrandListView.as_view(), name='brand_list'),
    path('product_caracteristics/unitmeasure/', views.UnitMeasureListView.as_view(), name='unitmeasure_list'),
]
