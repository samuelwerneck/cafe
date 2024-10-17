from store.models import Produto


class Carrinho():
	def __init__(self, request):
		self.session = request.session

		# Obtem a sessao atual, se existir
		carrinho = self.session.get('session_key')

		# Cria a sessao, se for um novo usuario
		if 'session_key' not in request.session:
			carrinho = self.session['session_key'] = {}


		# Garante que o carrinho esta disponivel em todas as paginas do site
		self.carrinho = carrinho
	
	def add(self, produto, quantidade):
		produto_id = str(produto.id)
		produto_qtde = str(quantidade)

		if produto_id in self.carrinho:
			pass
		else:
			#self.carrinho[produto_id] = {'Preço :': str(produto.preco)}
			self.carrinho[produto_id] = int(produto_qtde)

		self.session.modified = True

	def total(self):
		# Obtem o ID dos produtos
		produto_id = self.carrinho.keys()
		# Procura os IDs no banco de dados
		produtos = Produto.objects.filter(id__in=produto_id)
		# Obtem as quantidades
		quantidades = self.carrinho
		# Faz a totalização do carrinho
		total = 0

		for key, value in quantidades.items():
			key = int(key)
			for produto in produtos:
				if produto.id == key:
					total = total + (produto.preco * value)
		return total


	def __len__(self):
		return len(self.carrinho)
	
	def get_produtos(self):
		# Obtem os IDs do carrinho
		produto_ids = self.carrinho.keys()
		# Usa os ids pra buscar os produtos no banco
		produtos = Produto.objects.filter(id__in=produto_ids)
		

		return produtos
	
	def get_quantidades(self):
		quantidades = self.carrinho
		return quantidades
	
	def atualizar(self, produto, quantidade):
		produto_id = str(produto)
		produto_quantidade = int(quantidade)

		meucarrinho = self.carrinho
		meucarrinho[produto_id] = produto_quantidade

		self.session.modified = True

		mudanca = self.carrinho
		return mudanca
	
	def delete (self, produto):
		produto_id = str(produto)
		# Deleta do dicionario/carrinho
		if produto_id in self.carrinho:
			del self.carrinho[produto_id]
		
		self.session.modified = True