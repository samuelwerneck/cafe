from django.db import models
from django.contrib.auth.models import User
from store.models import Produto
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.validators import RegexValidator
import datetime

class EnderecoEntrega(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ent_nome = models.CharField(max_length=200)
    ent_email = models.CharField(max_length=200)
    ent_endereco = models.CharField(max_length=200)
    ent_complemento = models.CharField(max_length=200, null=True, blank=True)
    ent_cidade = models.CharField(max_length=200)
    ent_estado = models.CharField(max_length=200, null=True, blank=True)
    ent_cep = models.CharField(max_length=9, validators=[RegexValidator(r'^\d{5}-\d{3}$', message='ATENÇÃO! CEP deve estar no formato XXXXX-XXX.')], null=True, blank=True)

    #Não colocar endereço no plural no DJango
    class Meta:
        verbose_name_plural = "Endereços de Entrega"

    def __str__(self):
        return f'Endereço de Entrega - {str(self.id)}'
    
    # Cria um endereço de entrega para usuario
def cria_entrega(sender, instance, created, **kwargs):
	if created:
		endereco_usuario = EnderecoEntrega(usuario=instance)
		endereco_usuario.save()

# Automatiza o perfil
post_save.connect(cria_entrega, sender=User)
    
# Cria um modelo de pedido
class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    endereco_entrega = models.TextField(max_length=1000)
    valor_pago = models.DecimalField(max_digits=7, decimal_places=2)
    data_pedido = models.DateTimeField(auto_now_add=True)
    enviado = models.BooleanField(default=False)
    data_enviado = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'Pedido - {str(self.id)}'


# Adiciona data de envio automaticamente
@receiver(pre_save, sender=Pedido)
def set_data_enviado_on_update(sender, instance, **kwargs):
     if instance.pk:
          agora = datetime.datetime.now()
          obj = sender._default_manager.get(pk=instance.pk)
          if instance.enviado and not obj.enviado:
               instance.data_enviado = agora


# Cria um modelo de itens no pedido
class ItensPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True)
    produtos = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    quantidade = models.PositiveBigIntegerField(default=1)
    preco = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f'Item do Pedido - {str(self.id)}'