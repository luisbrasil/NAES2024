from django_filters import FilterSet
from .models import Pessoa, Cachorro


class PessoaFilter(FilterSet):
    class Meta:
        model = Pessoa
        fields = {
            'nome_completo': ['icontains'],
            'nascimento': ['exact', 'gt', 'lt'],
            'cidade__nome': ['icontains'],
            'cadastrado_em': ['year__exact'],
        }

class CachorroFilter(FilterSet):
    class Meta:
        model = Cachorro
        fields = {
            'nome': ['icontains'], 
            'raca__nome': ['icontains'], 
            'idade': ['exact','gt','lt'], 
            'cidade__nome': ['icontains'] 
        }