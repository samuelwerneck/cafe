# Generated by Django 5.1.2 on 2024-10-20 17:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagamento', '0004_rename_cep_enderecoentrega_ent_cep_and_more'),
        ('store', '0003_perfil_carrinho_salvo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('endereco_entrega', models.TextField(max_length=1000)),
                ('valor_pago', models.DecimalField(decimal_places=2, max_digits=7)),
                ('data_pedido', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItensPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveBigIntegerField(default=1)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7)),
                ('produtos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.produto')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pagamento.pedido')),
            ],
        ),
    ]