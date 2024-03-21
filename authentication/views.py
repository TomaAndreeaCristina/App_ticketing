from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView, PasswordResetView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from authentication.forms import CreateUserForm


# Create your views here.

class LoginUserView(LoginView):
    template_name = 'authentication/form.html'
    success_url = reverse_lazy('home')
    redirect_authenticated_user = True


class UserChangePasswordView(PasswordChangeView):
    template_name = 'authentication/form.html'
    success_url = reverse_lazy('home')


class CreateUserView(CreateView):
    template_name = 'authentication/form.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('home')


class LogOutUserView(LogoutView):
    success_url = reverse_lazy('home')


class ResetUserPassword(PasswordResetView):
    success_url = reverse_lazy('home')