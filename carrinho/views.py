from django.shortcuts import render, get_object_or_404
from .carrinho import Carrinho
from store.models import Produto
from django.http import JsonResponse

def carrinho_resumo(request):
	# Obtem o carrinho
	carrinho = Carrinho(request)
	carrinho_produtos = carrinho.get_produtos
	quantidades = carrinho.get_quantidades
	return render(request, "carrinho_resumo.html", {"carrinho_produtos":carrinho_produtos, "quantidades":quantidades})

def carrinho_add(request):
	# Obtem o Carrinho
	carrinho = Carrinho(request)
	# Teste do POST
	if request.POST.get('action') == 'post':
		# Obtem os produtos no carrinho
		produto_id = int(request.POST.get('produto_id'))
		produto_quantidade = int(request.POST.get('produto_qtde'))


		produto = get_object_or_404(Produto, id=produto_id)
		
		# Salva para a sessao
		carrinho.add(produto=produto, quantidade=produto_quantidade)
		
		# Obtem a quantidade de itens no carrinho
		carrinho_quantidade = carrinho.__len__()

		# Retorna a resposta
		# resposta = JsonResponse({'Nome do Produto: ': produto.nome})
		resposta = JsonResponse({'qtde': carrinho_quantidade})
		return resposta
	

def carrinho_delete(request):
	carrinho = Carrinho(request)
	if request.POST.get('action') == 'post':
		# Obtem os produtos no carrinho
		produto_id = int(request.POST.get('produto_id'))
		# Chama a função deletar no carrinho
		carrinho.delete(produto=produto_id)

		resposta = JsonResponse({'produto':produto_id})
		return resposta



def carrinho_update(request):
	carrinho = Carrinho(request)
	if request.POST.get('action') == 'post':
		# Obtem os produtos no carrinho
		produto_id = int(request.POST.get('produto_id'))
		produto_quantidade = int(request.POST.get('produto_qtde'))

		carrinho.atualizar(produto=produto_id, quantidade=produto_quantidade)

		resposta = JsonResponse({'qtde':produto_quantidade})
		return resposta