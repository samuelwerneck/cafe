from django.contrib import admin
from .models import EnderecoEntrega, Pedido, ItensPedido

# Registar o modelo no painel de admin no Django
admin.site.register(EnderecoEntrega)
admin.site.register(Pedido)
admin.site.register(ItensPedido)

# Concatena os itens do pedido e o pedido na página de administração
class PedidoItemInline(admin.StackedInline):
    model = ItensPedido
    extra = 0

class AdminPedido(admin.ModelAdmin):
    model = Pedido
    readonly_fields = ["data_pedido"]
    fields = ["usuario", "nome", "email", "endereco_entrega", "valor_pago", "data_pedido", "enviado", "data_enviado"]
    inlines = [PedidoItemInline]

# "Desregistra" o modelo de Pedido
admin.site.unregister(Pedido)
# Registra novamente os modelos de Pedido E AdminPedido
admin.site.register(Pedido, AdminPedido)