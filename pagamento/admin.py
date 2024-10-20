from django.contrib import admin
from .models import EnderecoEntrega, Pedido, ItensPedido

# Registar o modelo no painel de admin no Django
admin.site.register(EnderecoEntrega)
admin.site.register(Pedido)
admin.site.register(ItensPedido)