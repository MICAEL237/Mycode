from django.shortcuts import render
from django.views.generic import*
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from .models import Tasks
from .forms import *
# Create your views here.


class TaskcreateView(CreateView):
    model = Tasks
    form_class = TasKForm
    template_name = 'taches/form_tache.html'
    success_url = reverse_lazy('create')

    def get_form_kwargs(self):
        kwargs =  super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        if form.cleaned_data['objectif'].user != self.request.user:
            raise 
        PermissionDenied()
        return super().form_valid(form)
    
class TaskUpdateView(UpdateView):
    model = Tasks
    form_class = TasKForm
    template_name = 'taches/form_tache.html'
    success_url = reverse_lazy('create')


class StatusUpdateView(UpdateView):
    model = Tasks
    form_class = TaskFormeStatus
    template_name = 'taches/form_tache.html'
    success_url = reverse_lazy('create')


class TaskDeleteView(DeleteView):
    model = Tasks
    success_url = reverse_lazy('createtache')
