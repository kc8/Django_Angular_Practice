from django.conf.urls import url
from django.urls import path

from .api import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]