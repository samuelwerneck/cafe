# Generated by Django 5.1.2 on 2024-10-19 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_perfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='carrinho_salvo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
