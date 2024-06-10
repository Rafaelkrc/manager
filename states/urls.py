from django.urls import path
from . import views


urlpatterns = [
    path('states/cities/list/', views.CityListView.as_view(), name='city_list'),
    path('states/states/list/', views.StateListView.as_view(), name='state_list'),
    path('states/countries/list/', views.CountryListView.as_view(), name='country_list'),
    path('states/regions/list/', views.RegionListView.as_view(), name='region_list'),
]
