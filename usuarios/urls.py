from django.urls import path
from django.contrib.auth import views
from django.urls import reverse_lazy
from .views import UsuarioCreate

urlpatterns = [

    path("entrar/", views.LoginView.as_view(
        template_name="usuarios/form.html",
        extra_context={
            'titulo': 'Autenticação de usuários'
        }
    ), name="login"),

    path("sair/", views.LogoutView.as_view(), name="logout"),

    path("minha-senha/", views.PasswordChangeView.as_view(
        template_name="cadastros/form.html",
        success_url=reverse_lazy("index"),
        extra_context={
            'titulo': 'Atualizar minha senha'
        }
    ), name="alterar-senha"),

    path('registrar/', UsuarioCreate.as_view(
        success_url=reverse_lazy("index"),
        template_name="usuarios/form_registrar.html",
    ), name='registrar')
]