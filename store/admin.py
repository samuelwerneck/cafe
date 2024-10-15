from django.contrib import admin
from .models import Tipo, Cliente, Produto, Pedido

admin.site.register(Tipo)
admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(Pedido)