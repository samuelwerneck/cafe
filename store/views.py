from django.shortcuts import render, redirect
from .models import Produto
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, AtualizarSenha
from django import forms


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
			return redirect('home')
		else:
			messages.success(request, ("Oops. Something went wrong."))
			return redirect('register')
	else:
		return render(request, 'register.html', {'form':form})