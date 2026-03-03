from django.contrib.auth.models import User
from django.contrib.auth.views  import  LoginView
from django.views.generic import  CreateView, DetailView
from django.urls import reverse_lazy
from .forms import registerForm, LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from Objectif.models import Goals
from datetime import date

# Create your views here.




class RegisterViews(CreateView):
    model = User
    form_class = registerForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')

class loginViewForm(LoginView):
    
    model = User
    form_class = LoginForm
    template_name = 'account/login.html'

    def form_valid(self, form):
        return super().form_valid(form)
    


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'account/info_compte.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        section = self.kwargs.get('section')
        context =  super().get_context_data(**kwargs)
        user = self.get_object()
        Objectif = Goals.objects.filter(user = user)
        valeur = Objectif.values_list('date_fin', flat=True)
        today  = date.today()
        etat = ''
        for obj in valeur:
            if obj < today : # date passee
                etat = 'Terminer'
            else: #date futur
                etat = 'En cours'
        

        if section == 'objectif':
            
            context['Objectifs'] = Objectif
            context['etat'] = etat
        

    
        return context
    
    def get_template_names(self):
        section =  self.kwargs.get('section')

        if section == 'objectif':
            return ['objectif/objectif_list.html']
        else:
            return ['account/info_compte.html']



