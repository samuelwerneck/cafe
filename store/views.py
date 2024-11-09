from django.shortcuts import render, redirect
from .models import Produto, Perfil
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignUpForm, UpdateUserForm, AtualizarSenha, InfoUsuario_Form
from pagamento.forms import EntregaForm
from pagamento.models import EnderecoEntrega
from django.db.models import Q
import json
from carrinho.carrinho import Carrinho


def busca(request):
	# Verifica se o formulario foi preenchido
	if request.method == "POST":
		buscado = request.POST['buscado']
		# Buscar produtos na base de dados
		buscado = Produto.objects.filter(Q(nome__icontains=buscado) | Q(descricao__icontains=buscado))
		# Testa se não encontrou nada
		if not buscado:
			messages.success(request, "Este produto não existe. Tente novamente")
			return render(request, "busca.html", {})
		else:
			return render(request, "busca.html", {'buscado':buscado})
	else:
		return render(request, "busca.html", {})


def atualiza_info(request):
	if request.user.is_authenticated:
		# Obtem o usuario atual
		current_user = Perfil.objects.get(usuario__id=request.user.id)
		# Obtem o endereço de entrega do usuário atual
		entrega_user = EnderecoEntrega.objects.get(usuario__id=request.user.id)
		
		# Obtem o formuário do usuário
		form = InfoUsuario_Form(request.POST or None, instance=current_user)
		# Obtem o formulario de endereço de entrega
		entrega_form = EntregaForm(request.POST or None, instance=entrega_user)

		if form.is_valid() or entrega_form.is_valid():
			form.save()
			entrega_form.save()
			messages.success(request, "Suas informações foram salvas")
			return redirect('home')		
		return render(request, "atualiza_info.html", {'form':form, 'entrega_form':entrega_form})
	else:
		messages.success(request, "Você precisa estar logado para acessar essa página")
		return redirect('home')


def atualiza_senha(request):
	if request.user.is_authenticated:
		current_user = request.user
		# Preencheu o formulario
		if request.method == 'POST':
			form = AtualizarSenha(current_user, request.POST)
			# O formulario é valido?
			if form.is_valid():
				form.save()
				messages.success(request, "Sua nova senha foi salva. Por favor, faça login novamente")
				#login(request, current_user)
				return redirect('login')
			else:
				for error in list(form.errors.values()):
					messages.error(request, error)
					return redirect('atualiza_senha')

		else:
			form = AtualizarSenha(current_user)
			return render(request, "atualiza_senha.html", {'form':form})
	else:
		messages.success(request, "Você precisa estar logado pra acessar esta página")
		return redirect('home')


def atualiza_usuario(request):
	if request.user.is_authenticated:
		current_user = User.objects.get(id=request.user.id)
		user_form = UpdateUserForm(request.POST or None, instance=current_user)

		if user_form.is_valid():
			user_form.save()

			login(request, current_user)
			messages.success(request, "Informações atualizadas")
			return redirect('home')		
		return render(request, "atualiza_usuario.html", {'user_form':user_form})
	else:
		messages.success(request, "Você precisa estar logado para acessar essa página")
		return redirect('home')
	

def produto(request,pk):
	produto = Produto.objects.get(id=pk)
	return render(request, 'produtos.html', {'produto':produto})


def home(request):
	produtos = Produto.objects.all()
	return render(request, 'home.html', {'produtos':produtos})


def about(request):
	return render(request, 'about.html', {})


def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST.get('password', False)
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)

			# Recuperar um carrinho existente, se houver
			current_user = Perfil.objects.get(usuario__id=request.user.id)
			carrinho_existente = current_user.carrinho_salvo
			# Converte o carrinho salvo num dicionario Python
			if carrinho_existente:
				# Converte usando JSON
				carrinho_convertido = json.loads(carrinho_existente)
				# Adicionar a sessão
				carrinho = Carrinho(request)
				for key,value in carrinho_convertido.items():
					carrinho.db_add(produto=key, quantidade=value)




			messages.success(request, ("You have been logged in"))
			return redirect('home')
		else:
			messages.success(request, ("There was an error"))
			return redirect('login')

	else:
		return render(request, 'login.html', {})


def logout_user(request):
	logout(request)
	messages.success(request, ("You have been logged out!"))
	return redirect('home')


def register_user(request):
	form = SignUpForm()
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			# Log in user
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("You have registered successfully"))
			return redirect('atualiza_info')
		else:
			messages.success(request, ("Oops. Something went wrong."))
			return redirect('register')
	else:
		return render(request, 'register.html', {'form':form})