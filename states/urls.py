from django.urls import path
from . import views


urlpatterns = [
    path('states/cities/list/', views.CityListView.as_view(), name='city_list'),
    path('states/cities/create/', views.CityCreateView.as_view(), name='city_create'),
    path('states/cities/<int:pk>/details/', views.CityDetailView.as_view(), name='city_detail'),
    path('states/cities/<int:pk>/update/', views.CityUpdateView.as_view(), name='city_update'),
    path('states/cities/<int:pk>/delete/', views.CityDeleteView.as_view(), name='city_delete'),
    path('states/states/list/', views.StateListView.as_view(), name='state_list'),
    path('states/states/create/', views.StateCreateView.as_view(), name='state_create'),
    path('states/states/<int:pk>/details/', views.StateDetailView.as_view(), name='state_detail'),
    path('states/states/<int:pk>/update/', views.StateUpdateView.as_view(), name='state_update'),
    path('states/states/<int:pk>/delete/', views.StateDeleteView.as_view(), name='state_delete'),
    path('states/countries/list/', views.CountryListView.as_view(), name='country_list'),
    path('states/countries/create/', views.CountryCreateView.as_view(), name='country_create'),
    path('states/countries/<int:pk>/details/', views.CountryDetailView.as_view(), name='country_detail'),
    path('states/countries/<int:pk>/update/', views.CountryUpdateView.as_view(), name='country_update'),
    path('states/countries/<int:pk>/delete/', views.CountryDeleteView.as_view(), name='country_delete'),
    path('states/regions/list/', views.RegionListView.as_view(), name='region_list'),
    path('states/regions/create/', views.RegionCreateView.as_view(), name='region_create'),
    path('states/regions/<int:pk>/details/', views.RegionDetailView.as_view(), name='region_detail'),
    path('states/regions/<int:pk>/update/', views.RegionUpdateView.as_view(), name='region_update'),
    path('states/regions/<int:pk>/delete/', views.RegionDeleteView.as_view(), name='region_delete'),
]
