# Generated by Django 4.2.5 on 2024-07-29 23:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cadastros", "0003_alter_cidade_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pessoa",
            name="salario",
        ),
    ]
