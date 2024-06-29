from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models, forms


class OrganizationListView(ListView):
    model = models.Organization
    template_name = 'organization_list.html'
    context_object_name = 'organizations'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name')
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class OrganizationCreateView(CreateView):
    model = models.Organization
    form_class = forms.OrganizationForm
    template_name = 'organization_create.html'
    success_url = reverse_lazy('organization_list')


class OrganizationDetailView(DetailView):
    model = models.Organization
    template_name = 'organization_detail.html'


class OrganizationUpdateView(UpdateView):
    model = models.Organization
    template_name = 'organization_update.html'
    form_class = forms.OrganizationForm
    success_url = reverse_lazy('organization_list')


class OrganizationDeleteView(DeleteView):
    model = models.Organization
    template_name = 'organization_delete.html'
    success_url = reverse_lazy('organization_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        organization = self.get_object()
        context['register'] = organization.register
        context['name'] = organization.name
        context['fantasy_name'] = organization.fantasy_name
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        try:
            self.object.delete()
            return redirect(self.success_url)
        except ProtectedError:
            messages.error(request, "Organization is already related to flows, cannot be deleted!")
            return render(request, 'organization_undelete.html', context)
