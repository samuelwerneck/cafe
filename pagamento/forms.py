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
    ent_pais = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'País'}), required=True)

    class Meta:
        model = EnderecoEntrega
        fields = ['ent_nome', 'ent_email', 'ent_endereco', 'ent_complemento', 'ent_cidade', 'ent_estado', 'ent_cep', 'ent_pais', ]

        exclude = ['usuario', ]