from django.views.generic import ListView, CreateView, DetailView
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
