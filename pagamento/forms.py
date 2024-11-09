from django import forms
from .models import EnderecoEntrega

class EntregaForm(forms.ModelForm):
    ent_nome = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome'}), required=True)
    ent_email = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'E-mail'}), required=True)
    ent_endereco = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Endereço'}), required=True)
    ent_complemento = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Complemento'}), required=False)
    ent_cidade = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cidade'}), required=True)
    ent_estado = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Estado'}), required=False)
    ent_cep = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'CEP'}), required=False)

    class Meta:
        model = EnderecoEntrega
        fields = ['ent_nome', 'ent_email', 'ent_endereco', 'ent_complemento', 'ent_cidade', 'ent_estado', 'ent_cep', ]

        exclude = ['usuario', ]


class PagamentoForm(forms.Form):
    cartao_nome = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome no Cartão'}), required=True)
    cartao_numero = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Número do Cartão'}), required=True)
    cartao_venc = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Vencimento'}), required=True)
    cartao_cvv = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Código de Segurança'}), required=True)
    cartao_endereco = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Endereço de Cobrança'}), required=True)
    cartao_cidade = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cidade'}), required=True)
    cartao_estado = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Estado'}), required=True)
    cartao_cep = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'CEP'}), required=True)