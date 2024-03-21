from django.urls import path
from user.views import UserListView, UserDetaislView, UserUpdateView, UserCreateView, UserDeleteView

urlpatterns = [
    path('', UserListView.as_view(), name='user-all'),
    path('detail/<int:pk>', UserDetaislView.as_view(), name='user-detail'),
    path('update/<int:pk>', UserUpdateView.as_view(), name='user-update'),
    path('create/',UserCreateView.as_view(), name='user-create'),
    path('delete/<int:pk>',UserDeleteView.as_view(), name='user-delete')
]