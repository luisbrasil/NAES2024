from django.urls import path
# Importe suas views
from .views import CidadeCreate, CidadeUpdate, CidadeDelete, CidadeList
from .views import PessoaCreate, PessoaUpdate, PessoaDelete, PessoaList

urlpatterns = [
    # Crie suas urls para as views
    path('cadastrar/cidade/', CidadeCreate.as_view(), name='cadastrar-cidade'),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name='editar-cidade'),
    path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name='excluir-cidade'),
    path('listar/cidade/', CidadeList.as_view(), name='listar-cidade'),

    path('cadastrar/pessoa/', PessoaCreate.as_view(), name='cadastrar-pessoa'),
    path('editar/pessoa/<int:pk>/', PessoaUpdate.as_view(), name='editar-pessoa'),
    path('excluir/pessoa/<int:pk>/', PessoaDelete.as_view(), name='excluir-pessoa'),
    path('listar/pessoa/', PessoaList.as_view(), name='listar-pessoa'),
]
