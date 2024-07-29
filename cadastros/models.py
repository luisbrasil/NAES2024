from django.db import models


class Estado(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ["nome", "sigla"]


class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome}/{self.estado.sigla}"

    class Meta:
        ordering = ["nome", "estado"]


class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=150)
    nascimento = models.DateField(verbose_name="data de nascimento")
    cpf = models.CharField(max_length=14, verbose_name="CPF", unique=True)
    email = models.EmailField(max_length=120, blank=True, null=True)
    rede_social = models.URLField(max_length=255, blank=True, null=True,
                                  help_text="Informe o link do Instagram, Facebook, LinkedIn ou outra rede social.")
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome_completo} ({self.cpf})"


class Raca(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ["nome"]


class Cachorro(models.Model):
    nome = models.CharField(max_length=100)
    raca = models.ForeignKey(Raca, on_delete=models.PROTECT)
    idade = models.IntegerField()
    peso = models.DecimalField(decimal_places=2, max_digits=5)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    adotado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Adocao(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)
    cachorro = models.ForeignKey(Cachorro, on_delete=models.PROTECT)
    data_adocao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pessoa} adotou {self.cachorro} em {self.data_adocao}"
