from django.shortcuts import render, redirect
from carrinho.carrinho import Carrinho
from pagamento.forms import EntregaForm, PagamentoForm
from pagamento.models import EnderecoEntrega, Pedido, ItensPedido
from django.contrib.auth.models import User
from django.contrib import messages
from store.models import Produto


def pedidos(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        # Obtém o número do pedido
        pedido = Pedido.objects.get(id=pk)
        itens = ItensPedido.objects.filter(pedido=pk)
        return render(request, 'pagamento/pedidos.html', {"pedido":pedido, "itens":itens})


def painel_nao_enviados(request):
    if request.user.is_authenticated and request.user.is_superuser:
        pedidos = Pedido.objects.filter(enviado=False)
        return render(request, "pagamento/painel_nao_enviados.html", {"pedidos":pedidos})
    else:
        messages.success(request, "Acesso negado")
        return redirect('home')


def painel_enviados(request):
    if request.user.is_authenticated and request.user.is_superuser:
        pedidos = Pedido.objects.filter(enviado=True)
        return render(request, "pagamento/painel_enviados.html", {"pedidos":pedidos})
    else:
        messages.success(request, "Acesso negado")
        return redirect('home')


def processa_pedido(request):
    if request.POST:
        # Obtém o carrinho
        carrinho = Carrinho(request)
        carrinho_produtos = carrinho.get_produtos
        quantidades = carrinho.get_quantidades
        total = carrinho.total()

        # Obtém as informações de pagamento da página anterior
        pagamento_form = PagamentoForm(request.POST or None)
        
        # Obtém as dados da sessão do envio
        minha_entrega = request.session.get('minha_entrega')
        
        # Obtém informações do pedido
        nome = minha_entrega['ent_nome']
        email = minha_entrega['ent_email']
        endereco_entrega = f"{minha_entrega['ent_endereco']}\n{minha_entrega['ent_complemento']}\n{minha_entrega['ent_cidade']}\n{minha_entrega['ent_estado']}\n{minha_entrega['ent_cep']}"
        valor_pago = total

        # Criando o pedido
        if request.user.is_authenticated:
            user = request.user
            pedido = Pedido(usuario=user, nome=nome, email=email, endereco_entrega=endereco_entrega, valor_pago=valor_pago)
            pedido.save()

            # Adicionando itens ao pedido
            
            # Obtém o ID do pedido
            pedido_id = pedido.pk

            # Obtém os produtos do carrinho
            for produto in carrinho_produtos():
                produto_id = produto.id
                # Obtém o preço
                preco = produto.preco

                # Obtém a quantidade
                for key, value in quantidades().items():
                    if int(key) == produto.id:
                        itens_pedido = ItensPedido(pedido_id=pedido_id, produtos_id=produto_id, usuario=user, quantidade=value, preco=preco)
                        itens_pedido.save()

            # Deleta o carrinho após o pedido ser enviado
            for key in list(request.session.keys()):
                if key == "session_key":
                    # Deleta a chave
                    del request.session[key]


            messages.success(request, "Pedido enviado")
            return redirect('home')

        # Usuário não logado - Convidado
        else:
            pedido = Pedido(nome=nome, email=email, endereco_entrega=endereco_entrega, valor_pago=valor_pago)
            pedido.save()


            # Adicionando itens ao pedido
            
            # Obtém o ID do pedido
            pedido_id = pedido.pk

            # Obtém os produtos do carrinho
            for produto in carrinho_produtos():
                produto_id = produto.id
                # Obtém o preço
                preco = produto.preco

                # Obtém a quantidade
                for key, value in quantidades().items():
                    if int(key) == produto.id:
                        itens_pedido = ItensPedido(pedido_id=pedido_id, produtos_id=produto_id, quantidade=value, preco=preco)
                        itens_pedido.save()

             # Deleta o carrinho após o pedido ser enviado
            for key in list(request.session.keys()):
                if key == "session_key":
                    # Deleta a chave
                    del request.session[key]


            
            messages.success(request, "Pedido enviado")
            return redirect('home')

    else:
        messages.success(request, "Acesso Negado")
        return redirect('home')


def pagamento_info(request):
    if request.POST:
        # Obtém o carrinho
        carrinho = Carrinho(request)
        carrinho_produtos = carrinho.get_produtos
        quantidades = carrinho.get_quantidades
        total = carrinho.total()

        # Cria uma sessão com as informações de envio
        minha_entrega = request.POST
        request.session['minha_entrega'] = minha_entrega

        # Verifica se o usuario está autenticado
        if request.user.is_authenticated:
            # Obtém o formuário de cobrança
            pagamento_form = PagamentoForm()
            return render(request, "pagamento/pagamento_info.html", {"carrinho_produtos":carrinho_produtos, "quantidades":quantidades, "total":total, "entrega_info":request.POST, "pagamento_form":pagamento_form })
        else:
            # Usuário não autenticado
            # Obtém o formuário de cobrança
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

