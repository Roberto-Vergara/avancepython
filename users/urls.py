from django.urls import path
from .views import RegisterView, LoginView, LogoutView,ListProfesionalesView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),
    path('profesionales/', ListProfesionalesView.as_view()),
]