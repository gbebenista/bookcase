from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import UserCreation, UserLogin


class RegisterView(CreateView):
    form_class = UserCreation
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'


class ViewLogin(LoginView):
    redirect_authenticated_user = True
    form_class = UserLogin
    succes_url = reverse_lazy('home')
    template_name = 'registration/login.html'


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'users/home.html'
