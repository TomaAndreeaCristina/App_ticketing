# Create your views here.
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView, PasswordResetView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from authentication.forms import CreateUserForm


# Create your views here.

class LoginUserView(LoginView):
    template_name = 'authentication/form.html'
    success_url = reverse_lazy('ticket-all')
    redirect_authenticated_user = True


class UserChangePasswordView(PasswordChangeView):
    template_name = 'authentication/form.html'
    success_url = reverse_lazy('home')


class CreateUserView(CreateView):
    template_name = 'authentication/form.html'
    form_class = CreateUserForm
    success_message = "User creat cu succes"
    success_url = reverse_lazy('home')


class LogOutUserView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)

        success_url = reverse_lazy('home')
        return response


class ResetUserPassword(PasswordResetView):
    success_url = reverse_lazy('home')
