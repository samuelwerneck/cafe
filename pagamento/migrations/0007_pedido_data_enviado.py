# Generated by Django 5.1.2 on 2024-10-22 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagamento', '0006_pedido_enviado'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='data_enviado',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
