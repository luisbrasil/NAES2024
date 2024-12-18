from .models import Adocao, Cachorro, Cidade, Estado, Pessoa, Raca

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy

from django.contrib.messages.views import SuccessMessageMixin

from django_filters.views import FilterView
from .filters import PessoaFilter, CachorroFilter


class CidadeCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'form.html'
    success_url = reverse_lazy('listar-cidade')
    model = Cidade
    fields = ['nome', 'estado']
    success_message = "Cidade %(nome)s adicionada com sucesso!"

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar cidade'
        return dados


class CidadeUpdate(LoginRequiredMixin, SuccessMessageMixin,  UpdateView):
    template_name = 'form.html'
    success_url = reverse_lazy('listar-cidade')
    model = Cidade
    fields = ['nome', 'estado']
    success_message = "Cidade %(nome)s atualizada!"

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Editar registro de Cidade'
        return dados


class CidadeDelete(GroupRequiredMixin, SuccessMessageMixin,  DeleteView):
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-cidade')
    model = Cidade
    group_required = ["Administrador"]
    
    success_message = "Cidade excluída!"


class CidadeList(LoginRequiredMixin, ListView):
    template_name = 'list/cidade.html'
    model = Cidade

    def get_queryset(self):
        query = Cidade.objects.all()  # Consultando todas as cidades
        query = query.select_related("estado")  # Carregar o estado junto
        return query

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
    
    def get_object(self):
        pessoa = Pessoa.objects.get(
            pk=self.kwargs["pk"],
            cadastrado_por=self.request.user
        )
        return pessoa


class PessoaList(LoginRequiredMixin, FilterView):
    template_name = 'list/pessoa.html'
    model = Pessoa
    paginate_by = 50
    # Definir a classe criada no filters.py
    filterset_class = PessoaFilter
    
    def get_queryset(self):
        query = Pessoa.objects.filter(cadastrado_por=self.request.user)
        query = query.select_related("cidade")

        return query

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
    
    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        url_sucesso = super().form_valid(form)

        return url_sucesso

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar Cachorro'
        return dados

class CachorroUpdate(UpdateView):
    template_name = 'form.html'
    success_url = reverse_lazy('listar-cachorro')
    model = Cachorro
    fields = ['nome','raca','idade','cidade','adotado']
    
    def get_object(self):
        cachorro = Cachorro.objects.get(
            pk=self.kwargs["pk"], 
            cadastrado_por=self.request.user 
        )
        return cachorro

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Editar registro de Cachorro'
        return dados


class CachorroDelete(DeleteView):
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-cachorro')
    model = Cachorro
    
    def get_object(self):
        cachorro = Cachorro.objects.get(
            pk=self.kwargs["pk"],
            cadastrado_por=self.request.user
        )
        return cachorro


class CachorroList(LoginRequiredMixin, FilterView):
    template_name = 'list/cachorro.html'
    model = Cachorro
    paginate_by = 50

    # Definir a classe criada no filters.py
    filterset_class = CachorroFilter

    def get_queryset(self):
        query = Cachorro.objects.filter(cadastrado_por=self.request.user)
        # Carregar raca e cidade junto
        query = query.select_related("raca", "cidade")
        return query
    
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

    def form_valid(self, form):
        response = super().form_valid(form)

        cachorro = form.instance.cachorro
        cachorro.adotado = True
        cachorro.save()

        return response

class AdocaoDelete(DeleteView):
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-adocao')
    model = Adocao


class AdocaoList(ListView):
    template_name = 'list/adocao.html'
    model = Adocao

    def get_queryset(self):
        query = Adocao.objects.all()
        # Carregar pessoa e cachorro junto
        query = query.select_related("pessoa", "cachorro")
        return query
