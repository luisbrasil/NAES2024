from .models import Cachorro, Cidade, Estado, Pessoa, Raca

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView

from django.urls import reverse_lazy


class CidadeCreate(CreateView):
    template_name = 'form.html'
    success_url = reverse_lazy('listar-cidade')
    model = Cidade
    fields = ['nome', 'estado']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar cidade'
        return dados


class CidadeUpdate(UpdateView):
    template_name = 'form.html'
    success_url = reverse_lazy('listar-cidade')
    model = Cidade
    fields = ['nome', 'estado']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Editar registro de Cidade'
        return dados


class CidadeDelete(DeleteView):
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-cidade')
    model = Cidade


class CidadeList(ListView):
    template_name = 'list/cidade.html'
    model = Cidade

##############################################################


class PessoaCreate(CreateView):
    template_name = 'form.html'
    success_url = reverse_lazy('listar-pessoa')
    model = Pessoa
    fields = [
        'nome_completo', 'nascimento', 'cpf', 'email',
        'rede_social', 'cidade',
    ]

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar nova Pessoa'
        return dados


class PessoaUpdate(UpdateView):
    template_name = 'form.html'
    success_url = reverse_lazy('listar-pessoa')
    model = Pessoa
    fields = [
        'nome_completo', 'nascimento', 'cpf', 'email',
        'rede_social', 'cidade',
    ]

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = f"Editar registro de {self.object.nome_completo}"
        return dados


class PessoaDelete(DeleteView):
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-pessoa')
    model = Pessoa


class PessoaList(ListView):
    template_name = 'list/pessoa.html'
    model = Pessoa

## Estado
class EstadoCreate(CreateView):
    template_name = 'form.html'
    success_url = reverse_lazy('listar-estado')
    model = Estado
    fields = ['nome', 'sigla']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar estado'
        return dados


class EstadoUpdate(UpdateView):
    template_name = 'form.html'
    success_url = reverse_lazy('listar-estado')
    model = Estado
    fields = ['nome', 'sigla']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Editar registro de Estado'
        return dados


class EstadoDelete(DeleteView):
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-estado')
    model = Estado


class EstadoList(ListView):
    template_name = 'list/estado.html'
    model = Estado
    
## Raça
class RacaCreate(CreateView):
    template_name = 'form.html'
    success_url = reverse_lazy('listar-raca')
    model = Raca
    fields = ['nome']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar cachorro'
        return dados

class RacaUpdate(UpdateView):
    template_name = 'form.html'
    success_url = reverse_lazy('listar-raca')
    model = Raca
    fields = ['nome']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Editar registro de Raça'
        return dados


class RacaDelete(DeleteView):
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-raca')
    model = Raca


class RacaList(ListView):
    template_name = 'list/raca.html'
    model = Raca
    
## Cachorro

class CachorroCreate(CreateView):
    template_name = 'form.html'
    success_url = reverse_lazy('listar-cachorro')
    model = Cachorro
    fields = ['nome','raca','idade','cidade']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar raça'
        return dados

class CachorroUpdate(UpdateView):
    template_name = 'form.html'
    success_url = reverse_lazy('listar-cachorro')
    model = Cachorro
    fields = ['nome','raca','idade','cidade','adotado']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Editar registro de Raça'
        return dados


class CachorroDelete(DeleteView):
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-cachorro')
    model = Cachorro


class CachorroList(ListView):
    template_name = 'list/cachorro.html'
    model = Cachorro