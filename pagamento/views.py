from django.shortcuts import render
from carrinho.carrinho import Carrinho
from pagamento.forms import EntregaForm
from pagamento.models import EnderecoEntrega

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

