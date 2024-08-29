from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description','url']

    def __init__(self, *args, **kwargs):
        super(MovieForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Filme"
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Digite o nome do filme'})

        self.fields['url'].label = "Imagem"
        self.fields['url'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Digite o endereço da imagem'})

        self.fields['description'].label = "descrição"
        self.fields['description'].widget = forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Digite uma descrição para o filme',
            'rows': 10,
            'style': 'min-width: 400px; max-width: 400px;border-radius:5px ' 
        })