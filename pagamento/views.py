from django.shortcuts import render, redirect
from carrinho.carrinho import Carrinho
from pagamento.forms import EntregaForm, PagamentoForm
from pagamento.models import EnderecoEntrega
from django.contrib import messages

def pagamento_info(request):
    if request.POST:
        # Obtem o carrinho
        carrinho = Carrinho(request)
        carrinho_produtos = carrinho.get_produtos
        quantidades = carrinho.get_quantidades
        total = carrinho.total()

        # Verifica se o usuario está autenticado
        if request.user.is_authenticated:
            # Obtem o formuário de cobrança
            pagamento_form = PagamentoForm()
            return render(request, "pagamento/pagamento_info.html", {"carrinho_produtos":carrinho_produtos, "quantidades":quantidades, "total":total, "entrega_info":request.POST, "pagamento_form":pagamento_form })
        else:
            # Usuário não autenticado
            # Obtem o formuário de cobrança
            pagamento_form = PagamentoForm()
            return render(request, "pagamento/pagamento_info.html", {"carrinho_produtos":carrinho_produtos, "quantidades":quantidades, "total":total, "entrega_info":request.POST, "pagamento_form":pagamento_form })

        # parece que isso aqui tá sobrando... vou deixar por enquanto
        entrega_form = request.POST
        return render(request, "pagamento/pagamento_info.html", {"carrinho_produtos":carrinho_produtos, "quantidades":quantidades, "total":total, "entrega_form":entrega_form })
    else:
        messages.success(request, "Acesso negado")
        return redirect('home')



def checkout(request):

    # Obtem o carrinho
    carrinho = Carrinho(request)
    carrinho_produtos = carrinho.get_produtos
    quantidades = carrinho.get_quantidades
    total = carrinho.total()
       
    if request.user.is_authenticated:
        entrega_user = EnderecoEntrega.objects.get(usuario__id=request.user.id)
        entrega_form = EntregaForm(request.POST or None, instance=entrega_user)
        return render(request, "pagamento/checkout.html", {"carrinho_produtos":carrinho_produtos, "quantidades":quantidades, "total":total, "entrega_form":entrega_form })
    else:
        entrega_form = EntregaForm(request.POST or None)
        return render(request, "pagamento/checkout.html", {"carrinho_produtos":carrinho_produtos, "quantidades":quantidades, "total":total, "entrega_form":entrega_form })


def pagamento_sucesso(request):
    return render(request, "pagamento/pagamento_sucesso.html", {})

