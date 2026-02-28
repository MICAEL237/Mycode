from django.contrib.auth.models import User
from django.contrib.auth.views  import  LoginView
from django.views.generic import  CreateView
from django.urls import reverse_lazy
from .forms import registerForm, LoginForm
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

