from django.urls import path

from .views import Token

urlpatterns = [
    path('login', Token.as_view()),
]
