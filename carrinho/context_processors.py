from .carrinho import Carrinho

# Cria o processador de contexto pro carrinho funcionar em todas as paginas
def carrinho(request):
	#
	return {'carrinho': Carrinho(request)}