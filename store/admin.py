from django.contrib import admin
from .models import Tipo, Cliente, Produto, Pedido, Perfil
from django.contrib.auth.models import User

admin.site.register(Tipo)
admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(Perfil)

# Junta o perfil e a informação do usuário
class PerfilEmpilhado(admin.StackedInline):
    model = Perfil

# Estende o perfil do usuario
class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username", "first_name", "last_name", "email"]
    inlines = [PerfilEmpilhado]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)