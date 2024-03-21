from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from servicii.forms import ServiciiForm
from servicii.models import ServiciiModel
from user.forms import UserForm
from user.models import UserModel


# Create your views here.

class UserListView(ListView):
    template_name = 'user/all.html'
    model = UserModel


class UserDetaislView(DetailView):
    template_name = 'user/detalii.html'
    model = UserModel

class UserUpdateView(UpdateView):
    template_name = 'user/create_update_form.html'
    form_class = UserForm
    model = UserModel
    success_url = reverse_lazy('user-all')


class UserDeleteView(DeleteView):
    template_name = 'user/delete_form.html'
    model = UserModel
    success_url = reverse_lazy('user-all')
    success_message = 'User sters!!!'


class UserCreateView(CreateView):
    form_class = UserForm
    template_name = 'user/create_update_form.html'
    model = UserModel
    success_url = reverse_lazy('user-all')