from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Sessions
from .forms import SessionForm, SessionForm2
from django.urls import reverse_lazy
from django.utils import timezone


# Create your views here.

class sessionCreateView(CreateView):
    model = Sessions
    template_name ='session/session_form.html'
    form_class = SessionForm
    success_url = reverse_lazy('terminersession')


class sessionValideeView(UpdateView):
    model = Sessions
    template_name ='session/session_page.html'
    form_class = SessionForm2
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('listgoal')

    def form_valid(self, form):
        form.instance.heure_fin = timezone.now().time()
        return super().form_valid(form)



