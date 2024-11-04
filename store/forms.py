from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import Perfil

class InfoUsuario_Form(forms.ModelForm):
	fone = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Telefone'}), required=False)
	endereco = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Endereço'}), required=False)
	complemento = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Complemento'}), required=False)
	cidade = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cidade'}), required=False)
	estado = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Estado'}), required=False)
	cep = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'CEP'}), required=False)
	#pais = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'País'}), required=False)

	class Meta:
		model = Perfil
		fields = ('fone', 'endereco', 'complemento', 'cidade', 'estado', 'cep', )


class AtualizarSenha(SetPasswordForm):
	class Meta:
		model = User
		fields = ['new_password1', 'new_password2']

	def __init__(self, *args, **kwargs):
		super(AtualizarSenha, self).__init__(*args, **kwargs)

		self.fields['new_password1'].widget.attrs['class'] = 'form-control'
		self.fields['new_password1'].widget.attrs['placeholder'] = 'Senha'
		self.fields['new_password1'].label = ''
		self.fields['new_password1'].help_text = '<ul class="form-text text-muted small"><li>Sua senha não pode ser parecida com outros dados pessoais.</li><li>Sua senha deve possuir pelo menos 8 caracteres.</li><li>Não pode ser uma senha usada com freqência</li><li>Não pode ter apenas números.</li></ul>'

		self.fields['new_password2'].widget.attrs['class'] = 'form-control'
		self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirme a Senha'
		self.fields['new_password2'].label = ''
		self.fields['new_password2'].help_text = '<span class="form-text text-muted"><small>Digite a mesma senha</small></span>'


class UpdateUserForm(UserChangeForm):
	# Esconder informações de senha nesse formulario de atualização
	password = None
	# Outras informações
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'E-Mail'}),required=False)
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome Completo'}),required=False)
	#last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),required=False)

	class Meta:
		model = User
		#fields = ('username', 'first_name', 'last_name', 'email')
		fields = ('username', 'first_name', 'email')

	def __init__(self, *args, **kwargs):
		super(UpdateUserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Nome de Usuário'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Necessário. No máximo 50 caracteres. Apenas letras, números e @ . + - _</small></span>'



class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'E-Mail'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome Completo'}))
	#last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

	class Meta:
		model = User
		#fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
		fields = ('username', 'first_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Nome de Usuário'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Necessário. No máximo 50 caracteres. Apenas letras, números e @ . + - _</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Sua senha não pode ser parecida com outros dados pessoais.</li><li>Sua senha deve possuir pelo menos 8 caracteres.</li><li>Não pode ser uma senha usada com freqência</li><li>Não pode ter apenas números.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirme a Senha'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Digite a mesma senha</small></span>'