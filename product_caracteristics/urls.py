from django.urls import path
from . import views


urlpatterns = [
    path('product_caracteristics/group/list/', views.GroupListView.as_view(), name='group_list'),
    path('product_caracteristics/group/create/', views.GroupCreateView.as_view(), name='group_create'),
    path('product_caracteristics/group/<int:pk>/detail/', views.GroupDetailView.as_view(), name='group_detail'),
    path('product_caracteristics/brand/list/', views.BrandListView.as_view(), name='brand_list'),
    path('product_caracteristics/brand/create/', views.BrandCreateView.as_view(), name='brand_create'),
    path('product_caracteristics/brand/<int:pk>/detail/', views.BrandDetailView.as_view(), name='brand_detail'),
    path('product_caracteristics/unitmeasure/list', views.UnitMeasureListView.as_view(), name='unitmeasure_list'),
    path('product_caracteristics/unitmeasure/create', views.UnitMeasureCreateView.as_view(), name='unitmeasure_create'),
    path('product_caracteristics/unitmeasure/<int:pk>/detail/', views.UnitMeasureDetailView.as_view(), name='unitmeasure_detail'),
]
