from django.urls import path

from api.views import CodeExplainView, UserView, TokenView

urlpatterns = [
    path('users/', UserView.as_view(), name='usersapi' ),
    path('tokens/', TokenView.as_view(), name='tokens' ),
    path('code-explain/', CodeExplainView.as_view(), name='code-explain'),

]