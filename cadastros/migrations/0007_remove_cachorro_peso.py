# Generated by Django 5.0.7 on 2024-08-05 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0006_alter_cidade_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cachorro',
            name='peso',
        ),
    ]
