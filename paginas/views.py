from django.views.generic import TemplateView
import random
from cadastros.models import Cachorro

# Criar uma view para a página inicial
# com herança para a classe TemplateView
class IndexView(TemplateView):
    template_name = "paginas/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Página Inicial"
        context['qtdeCachorrosAdotados'] = Cachorro.objects.filter(adotado=True).count()
        context['qtdeCachorrosDisponiveis'] = Cachorro.objects.filter(adotado=False).count()
        
        cachorrinhos = list(Cachorro.objects.filter(adotado=False).order_by('nome'))
        if cachorrinhos:
            numero_cachorros = min(3, len(cachorrinhos))
            context['cachorrosAleatorios'] = random.sample(cachorrinhos, numero_cachorros)
        else:
            context['cachorrosAleatorios'] = []

        print(context['cachorrosAleatorios'])

        return context


class SobreView(TemplateView):
    template_name = "paginas/sobre.html"
    