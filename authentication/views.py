from django.shortcuts import render
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView, PasswordResetView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from authentication.forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from authentication.models import Companie


# Create your views here.

class LoginUserView(LoginView):
    template_name = 'authentication/form.html'
    success_url = reverse_lazy('ticket-all')
    redirect_authenticated_user = True


class UserChangePasswordView(PasswordChangeView):
    template_name = 'authentication/form.html'
    success_url = reverse_lazy('home')


class CreateUserView(CreateView):
    template_name = 'company_register.html'
    form_class = CreateUserForm
    success_message = "User creat cu succes"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.save()

        # Salvăm numele companiei asociate utilizatorului
        nume_companie = form.cleaned_data.get('nume_companie')

        # Verificăm dacă utilizatorul este deja asociat cu o companie
        try:
            companie = user.companie
            companie.nume_companie = nume_companie
            # actualizează alte câmpuri dacă este necesar
            companie.save()
        except Companie.DoesNotExist:
            # Creăm o nouă companie dacă utilizatorul nu este încă asociat cu nicio companie
            Companie.objects.create(nume_companie=nume_companie, user=user)

        return super().form_valid(form)


class LogOutUserView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)

        success_url = reverse_lazy('home')
        return response


class ResetUserPassword(PasswordResetView):
    success_url = reverse_lazy('home')


User = get_user_model()


# @login_required
# def approve_user(request, user_id):
#     if request.user.is_superuser:
#         user = User.objects.get(pk=user_id)
#         user.approve_user()
#         return redirect('admin')  # Redirecționare către panoul de administrare
#     else:
#         return redirect('home')  # Redirecționare către pagina de start sau altă pagină adecvată
#
#
@login_required
def company_register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()

            nume_companie = form.cleaned_data.get('nume_companie')

            # Verificăm dacă utilizatorul este deja asociat cu o companie
            try:
                companie = user.companie
                companie.nume_companie = nume_companie
                # actualizează alte câmpuri dacă este necesar
                companie.save()
            except Companie.DoesNotExist:
                # Creăm o nouă companie dacă utilizatorul nu este încă asociat cu nicio companie
                Companie.objects.create(nume_companie=nume_companie, user=user)

            return redirect('register-company')
    else:
        form = CreateUserForm()
    return render(request, 'authentication/form.html', {'form': form})


@login_required
def user_register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()

            nume_companie = form.cleaned_data.get('nume_companie')
            Companie.objects.create(nume_companie=nume_companie, user=user)

            return redirect('home')
    else:
        form = CreateUserForm()
    return render(request, 'authentication/form.html', {'form': form})
