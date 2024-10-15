
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