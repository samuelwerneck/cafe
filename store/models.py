from django.db import models
import datetime

# Tipos de Produtos
class Tipo(models.Model):
	nome = models.CharField(max_length=50)

	def __str__(self):
		return self.nome

# Clientes
class Cliente(models.Model):
	nome = models.CharField(max_length=50)
	fone = models.CharField(max_length=10)
	email = models.EmailField(max_length=100)
	senha = models.CharField(max_length=100)

	def __str__(self):
		return self.nome

# Produtos
class Produto(models.Model):
	nome = models.CharField(max_length=50)
	preco = models.DecimalField(default=0, decimal_places=2, max_digits=6)
	tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, default=1)
	descricao = models.CharField(max_length=200, default='', blank=True, null=True)
	imagem = models.ImageField(upload_to='uploads/product/')

	def __str__(self):
		return self.nome

# Pedidos
class Pedido(models.Model):
	produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	quantidade = models.IntegerField(default=1)
	endereco = models.CharField(max_length=100, default='', blank=True)
	fone = models.CharField(max_length=20, default='', blank=True)
	data = models.DateField(default=datetime.datetime.today)
	status = models.BooleanField(default=False)

	def __str__(self):
		return self.produto