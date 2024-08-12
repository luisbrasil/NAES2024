from django.urls import path, reverse_lazy
from django.contrib.auth import views

urlpatterns = [
    path("entrar/", views.LoginView.as_view(
            template_name="form.html",
            extra_context={
                'titulo': 'Autenticação de usuários'    
            }
        ), name="login"),

    path("sair/", views.LogoutView.as_view(), name="Logout"),
    
    path("senha/", views.PasswordChangeView.as_view(
            template_name = "form.html",
            success_url = reverse_lazy("index"),
            extra_context = {
                    'titulo': 'Alterar senha'
            }
        ), name="alterar-senha"),
]