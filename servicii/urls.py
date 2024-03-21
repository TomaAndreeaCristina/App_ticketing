from django.urls import path
from servicii.views import ServiciiListView, ServiciiDetaislView, ServiciiUpdateView,ServiciiCreateView,ServiciiDeleteView

urlpatterns = [
    path('', ServiciiListView.as_view(), name='serviciu-all'),
    path('detail/<int:pk>', ServiciiDetaislView.as_view(), name='serviciu-detail'),
    path('update/<int:pk>', ServiciiUpdateView.as_view(), name='serviciu-update'),
    path('create/',ServiciiCreateView.as_view(), name='serviciu-create'),
    path('delete/<int:pk>',ServiciiDeleteView.as_view(), name='serviciu-delete'),
]

