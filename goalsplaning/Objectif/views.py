from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.models import User
from .models import Goals
from .forms import GoalsForm, GoalsFormetat
from django.urls import reverse_lazy
from django.contrib.auth.mixins  import LoginRequiredMixin


# Create your views here.


class GoalsCreateView(LoginRequiredMixin, CreateView):
    model = Goals
    form_class = GoalsForm
    template_name = 'objectif/objectif_form.html'
    success_url = reverse_lazy('listgoal')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class GoalsUpdate(UpdateView):
    model = Goals
    form_class = GoalsForm
    template_name = 'objectif/objectif_form.html'
    success_url = reverse_lazy('listgoal')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class GoalsUpdateetat(UpdateView):
    model = Goals
    template_name = 'objectif/objectif_form.html'
    form_class =  GoalsFormetat
    success_url = reverse_lazy('listgoal')
    

class GoalsDelete(DeleteView):
    model = Goals
    