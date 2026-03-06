from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.models import User
from .models import Goals
from .forms import GoalsForm, GoalsFormetat
from django.urls import reverse_lazy
from django.contrib.auth.mixins  import LoginRequiredMixin
from Taches.models import Tasks
from django.db.models import Count


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
    success_url = reverse_lazy('listgoal')
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class GoalsListView(ListView):
    model = Goals
    template_name = 'objectif/objectif_list.html'
    context_object_name = 'goals'
class DetailGoalsView(DetailView):
    model = Goals
    template_name = 'objectif/details/objectif_taches.html'
    context_object_name = 'goals'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        section = self.kwargs.get('section')

        goals = self.get_object()
        taches = Tasks.objects.filter(objectif = goals)
        nbretaches = taches.count()

        if section == 'taches':
             context['taches'] = taches
        else:

            context['nbretaches'] = nbretaches
        return context


    def get_template_names(self):
        section = self.kwargs.get('section')

        if section == 'taches':
            return ['objectif/details/objectif_taches.html']
        else:
            return ['objectif/details/objectif_stat.html']

        
    