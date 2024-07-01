from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models, forms


class SubsidiaryListView(ListView):
    model = models.Subsidiary
    template_name = 'subsidiary_list.html'
    context_object_name = 'subsidiaries'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('id', 'name')
        name = self.request.GET.get('name')
        register = self.request.GET.get('register')

        if name:
            queryset = queryset.filter(name__icontains=name)
        if register:
            queryset = queryset.filter(register__icontains=register)
        return queryset


class SubsidiaryCreateView(CreateView):
    model = models.Subsidiary
    form_class = forms.SubsidiaryForm
    template_name = 'subsidiary_create.html'
    success_url = reverse_lazy('subsidiary_list')


class SubsidiaryDetailView(DetailView):
    model = models.Subsidiary
    template_name = 'subsidiary_detail.html'


class SubsidiaryUpdateView(UpdateView):
    model = models.Subsidiary
    template_name = 'subsidiary_update.html'
    form_class = forms.SubsidiaryForm
    success_url = reverse_lazy('subsidiary_list')


class SubsidiaryDeleteView(DeleteView):
    model = models.Subsidiary
    template_name = 'subsidiary_delete.html'
    success_url = reverse_lazy('subsidiary_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subsidiary = self.get_object()
        context['register'] = subsidiary.register
        context['name'] = subsidiary.name
        context['fantasy_name'] = subsidiary.fantasy_name
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        try:
            self.object.delete()
            return redirect(self.success_url)
        except ProtectedError:
            messages.error(request, "Subsidiary is already related to flows, cannot be deleted!")
            return render(request, 'subsidiary_undelete.html', context)
