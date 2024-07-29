# Generated by Django 4.2.5 on 2024-07-29 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("cadastros", "0004_remove_pessoa_salario"),
    ]

    operations = [
        migrations.CreateModel(
            name="Estado",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("sigla", models.CharField(max_length=2)),
            ],
            options={
                "ordering": ["nome", "sigla"],
            },
        ),
        migrations.CreateModel(
            name="Raca",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
            ],
            options={
                "ordering": ["nome"],
            },
        ),
        migrations.CreateModel(
            name="Cachorro",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("idade", models.IntegerField()),
                ("peso", models.DecimalField(decimal_places=2, max_digits=5)),
                ("adotado", models.BooleanField(default=False)),
                (
                    "cidade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="cadastros.cidade",
                    ),
                ),
                (
                    "raca",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="cadastros.raca"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Adocao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data_adocao", models.DateTimeField(auto_now_add=True)),
                (
                    "cachorro",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="cadastros.cachorro",
                    ),
                ),
                (
                    "pessoa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="cadastros.pessoa",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="cidade",
            name="estado",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="cadastros.estado"
            ),
        ),
    ]
