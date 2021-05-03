from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name="users/sign_in.html"), name="sign_in"),
    path('sign_out', auth_views.LogoutView.as_view(template_name="users/sign_out.html"), name="sign_out"),
    path('sign_up', views.sign_up, name="sign_up")
]
