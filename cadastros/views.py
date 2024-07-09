from .models import Cidade, Pessoa

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class CidadeCreate(CreateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'form.html'
    success_url = reverse_lazy('index')
    
class PessoaCreate(CreateView):
    model = Pessoa
    fields = ['nome_completo', 'nascimento', 'cpf', 'email',
              'rede_social', 'salario', 'cidade']
    template_name = 'form.html'
    success_url = reverse_lazy('index')

class CidadeUpdate(UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'form.html'
    success_url = reverse_lazy('index')

class PessoaUpdate(UpdateView):
    model = Pessoa
    fields = ['nome_completo', 'nascimento', 'email',
              'rede_social', 'salario', 'cidade']
    template_name = 'form.html'
    success_url = reverse_lazy('index')
