from .models import Adocao, Cachorro, Cidade, Estado, Pessoa, Raca

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy


class CidadeCreate(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    success_url = reverse_lazy('listar-cidade')
    model = Cidade
    fields = ['nome', 'estado']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar cidade'
        return dados


class CidadeUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    success_url = reverse_lazy('listar-cidade')
    model = Cidade
    fields = ['nome', 'estado']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Editar registro de Cidade'
        return dados


class CidadeDelete(GroupRequiredMixin, DeleteView):
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-cidade')
    model = Cidade
    group_required = ["Administrador"]


class CidadeList(LoginRequiredMixin, ListView):
    template_name = 'list/cidade.html'
    model = Cidade

##############################################################


class PessoaCreate(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    success_url = reverse_lazy('listar-pessoa')
    model = Pessoa
    fields = [
        'nome_completo', 'nascimento', 'cpf', 'email',
        'rede_social', 'cidade',
    ]
    
    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        url_sucesso = super().form_valid(form)

        return url_sucesso

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar nova Pessoa'
        return dados


class PessoaUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    success_url = reverse_lazy('listar-pessoa')
    model = Pessoa
    fields = [
        'nome_completo', 'nascimento', 'cpf', 'email',
        'rede_social', 'cidade',
    ]

    def get_object(self):
        pessoa = Pessoa.objects.get(
            pk=self.kwargs["pk"],
            # Além do id, faz um WHERE também com o usuário
            cadastrado_por=self.request.user
        )
        return pessoa

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = f"Editar registro de {self.object.nome_completo}"
        return dados


class PessoaDelete(GroupRequiredMixin, DeleteView):
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-pessoa')
    model = Pessoa
    group_required = ["Administrador"]


class PessoaList(LoginRequiredMixin, ListView):
    template_name = 'list/pessoa.html'
    model = Pessoa

## Estado
class EstadoCreate(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    success_url = reverse_lazy('listar-estado')
    model = Estado
    fields = ['nome', 'sigla']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar estado'
        return dados


class EstadoUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    success_url = reverse_lazy('listar-estado')
    model = Estado
    fields = ['nome', 'sigla']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Editar registro de Estado'
        return dados


class EstadoDelete(GroupRequiredMixin, DeleteView):
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-estado')
    model = Estado
    group_required = ["Administrador"]


class EstadoList(LoginRequiredMixin, ListView):
    template_name = 'list/estado.html'
    model = Estado
    
## Raça


class RacaCreate(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    success_url = reverse_lazy('listar-raca')
    model = Raca
    fields = ['nome']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar Raça'
        return dados

class RacaUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    success_url = reverse_lazy('listar-raca')
    model = Raca
    fields = ['nome']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Editar registro de Raça'
        return dados


class RacaDelete(GroupRequiredMixin, DeleteView):
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-raca')
    model = Raca
    group_required = ["Administrador"]

class RacaList(LoginRequiredMixin, ListView):
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
        dados['titulo'] = 'Cadastrar Cachorro'
        return dados

class CachorroUpdate(UpdateView):
    template_name = 'form.html'
    success_url = reverse_lazy('listar-cachorro')
    model = Cachorro
    fields = ['nome','raca','idade','cidade','adotado']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Editar registro de Cachorro'
        return dados


class CachorroDelete(DeleteView):
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-cachorro')
    model = Cachorro


class CachorroList(ListView):
    template_name = 'list/cachorro.html'
    model = Cachorro
    
## Adoção
class AdocaoCreate(CreateView):
    template_name = 'form.html'
    success_url = reverse_lazy('listar-adocao')
    model = Adocao
    fields = ['pessoa','cachorro']

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar adoção'
        return dados

class AdocaoDelete(DeleteView):
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-adocao')
    model = Adocao


class AdocaoList(ListView):
    template_name = 'list/adocao.html'
    model = Adocao