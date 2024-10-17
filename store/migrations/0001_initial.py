# Generated by Django 5.1.2 on 2024-10-13 14:13

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('fone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('senha', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('preco', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('descricao', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('imagem', models.ImageField(upload_to='uploads/product/')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=1)),
                ('endereco', models.CharField(blank=True, default='', max_length=100)),
                ('fone', models.CharField(blank=True, default='', max_length=20)),
                ('data', models.DateField(default=datetime.datetime.today)),
                ('status', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.cliente')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.produto')),
            ],
        ),
        migrations.AddField(
            model_name='produto',
            name='tipo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.tipo'),
        ),
    ]