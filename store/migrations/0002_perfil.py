# Generated by Django 5.1.2 on 2024-10-18 23:03

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_modificado', models.DateTimeField(auto_now=True, verbose_name=django.contrib.auth.models.User)),
                ('fone', models.CharField(blank=True, max_length=20)),
                ('endereco1', models.CharField(blank=True, max_length=200)),
                ('endereco2', models.CharField(blank=True, max_length=200)),
                ('cidade', models.CharField(blank=True, max_length=200)),
                ('estado', models.CharField(blank=True, max_length=200)),
                ('cep', models.CharField(blank=True, max_length=200)),
                ('pais', models.CharField(blank=True, max_length=200)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
