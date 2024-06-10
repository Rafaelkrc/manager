from django.views.generic import ListView
from . import models


class CityListView(ListView):
    model = models.City
    template_name = 'city_list.html'
    context_object_name = 'cities'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name', 'state')
        name = self.request.GET.get('name')
        state = self.request.GET.get('state')
        if name:
            queryset = queryset.filter(name__icontains=name)
        if state:
            queryset = queryset.filter(state__name__icontains=state)
        return queryset


class StateListView(ListView):
    model = models.State
    template_name = 'state_list.html'
    context_object_name = 'states'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name')
        name = self.request.GET.get('name')
        country = self.request.GET.get('country')
        region = self.request.GET.get('region')
        if name:
            queryset = queryset.filter(name__icontains=name)
        if country:
            queryset = queryset.filter(country__name__icontains=country)
        if region:
            queryset = queryset.filter(region__name__icontains=region)
        return queryset


class CountryListView(ListView):
    model = models.Country
    template_name = 'country_list.html'
    context_object_name = 'countries'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name')
        name = self.request.GET.get('name')
        abbreviation = self.request.GET.get('abbreviation')
        if name:
            queryset = queryset.filter(name__icontains=name)
        if abbreviation:
            queryset = queryset.filter(abbreviation__icontains=abbreviation)
        return queryset


class RegionListView(ListView):
    model = models.Region
    template_name = 'region_list.html'
    context_object_name = 'regions'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name')
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset
