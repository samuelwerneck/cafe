# Generated by Django 5.1.2 on 2024-10-22 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagamento', '0005_pedido_itenspedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='enviado',
            field=models.BooleanField(default=False),
        ),
    ]
