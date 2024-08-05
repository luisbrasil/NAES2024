from django.urls import path
# Importe suas views
from .views import AdocaoCreate, AdocaoDelete, AdocaoList, CachorroCreate, CachorroDelete, CachorroList, CachorroUpdate, CidadeCreate, CidadeUpdate, CidadeDelete, CidadeList
from .views import EstadoCreate, EstadoDelete, EstadoList, EstadoUpdate, RacaCreate, RacaDelete, RacaList, RacaUpdate
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
    
    path('cadastrar/estado/', EstadoCreate.as_view(), name='cadastrar-estado'),
    path('editar/estado/<int:pk>/', EstadoUpdate.as_view(), name='editar-estado'),
    path('excluir/estado/<int:pk>/', EstadoDelete.as_view(), name='excluir-estado'),
    path('listar/estado/', EstadoList.as_view(), name='listar-estado'),
    
    path('cadastrar/raca/', RacaCreate.as_view(), name='cadastrar-raca'),
    path('editar/raca/<int:pk>/', RacaUpdate.as_view(), name='editar-raca'),
    path('excluir/raca/<int:pk>/', RacaDelete.as_view(), name='excluir-raca'),
    path('listar/raca/', RacaList.as_view(), name='listar-raca'),

    path('cadastrar/cachorro/', CachorroCreate.as_view(), name='cadastrar-cachorro'),
    path('editar/cachorro/<int:pk>/', CachorroUpdate.as_view(), name='editar-cachorro'),
    path('excluir/cachorro/<int:pk>/', CachorroDelete.as_view(), name='excluir-cachorro'),
    path('listar/cachorro/', CachorroList.as_view(), name='listar-cachorro'),
    
    path('cadastrar/adocao/', AdocaoCreate.as_view(), name='cadastrar-adocao'),
    path('excluir/adocao/<int:pk>/', AdocaoDelete.as_view(), name='excluir-adocao'),
    path('listar/adocao/', AdocaoList.as_view(), name='listar-adocao'),
]
