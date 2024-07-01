from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models, forms


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


class CityCreateView(CreateView):
    model = models.City
    form_class = forms.CityForm
    template_name = 'city_create.html'
    success_url = reverse_lazy('city_list')


class CityDetailView(DetailView):
    model = models.City
    template_name = 'city_detail.html'


class CityUpdateView(UpdateView):
    model = models.City
    form_class = forms.CityForm
    template_name = 'city_update.html'
    success_url = reverse_lazy('city_list')


class CityDeleteView(DeleteView):
    model = models.City
    template_name = 'city_delete.html'
    success_url = reverse_lazy('city_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city = self.get_object()
        context['name'] = city.name
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        try:
            self.object.delete()
            return redirect(self.success_url)
        except ProtectedError:
            messages.error(request, "City is already related, cannot be deleted!")
            return render(request, 'city_undelete.html', context)


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


class StateCreateView(CreateView):
    model = models.State
    form_class = forms.StateForm
    template_name = 'state_create.html'
    success_url = reverse_lazy('state_list')


class StateDetailView(DetailView):
    model = models.State
    template_name = 'state_detail.html'


class StateUpdateView(UpdateView):
    model = models.State
    form_class = forms.StateForm
    template_name = 'state_update.html'
    success_url = reverse_lazy('state_list')


class StateDeleteView(DeleteView):
    model = models.State
    template_name = 'state_delete.html'
    success_url = reverse_lazy('state_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        state = self.get_object()
        context['name'] = state.name
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        try:
            self.object.delete()
            return redirect(self.success_url)
        except ProtectedError:
            messages.error(request, "State is already related, cannot be deleted!")
            return render(request, 'state_undelete.html', context)


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


class CountryCreateView(CreateView):
    model = models.Country
    form_class = forms.CountryForm
    template_name = 'country_create.html'
    success_url = reverse_lazy('country_list')


class CountryDetailView(DetailView):
    model = models.Country
    template_name = 'country_detail.html'


class CountryUpdateView(UpdateView):
    model = models.Country
    form_class = forms.CountryForm
    template_name = 'country_update.html'
    success_url = reverse_lazy('country_list')


class CountryDeleteView(DeleteView):
    model = models.Country
    template_name = 'country_delete.html'
    success_url = reverse_lazy('country_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        country = self.get_object()
        context['name'] = country.name
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        try:
            self.object.delete()
            return redirect(self.success_url)
        except ProtectedError:
            messages.error(request, "Country is already related, cannot be deleted!")
            return render(request, 'country_undelete.html', context)


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


class RegionCreateView(CreateView):
    model = models.Region
    form_class = forms.RegionForm
    template_name = 'region_create.html'
    success_url = reverse_lazy('region_list')


class RegionDetailView(DetailView):
    model = models.Region
    template_name = 'region_detail.html'


class RegionUpdateView(UpdateView):
    model = models.Region
    form_class = forms.RegionForm
    template_name = 'region_update.html'
    success_url = reverse_lazy('region_list')


class RegionDeleteView(DeleteView):
    model = models.Region
    template_name = 'region_delete.html'
    success_url = reverse_lazy('region_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        region = self.get_object()
        context['name'] = region.name
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        try:
            self.object.delete()
            return redirect(self.success_url)
        except ProtectedError:
            messages.error(request, "Region is already related, cannot be deleted!")
            return render(request, 'region_undelete.html', context)
