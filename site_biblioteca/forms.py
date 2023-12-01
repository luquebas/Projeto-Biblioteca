from django import forms
from django.core.exceptions import ValidationError
from django.contrib import auth
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import BookRegister
import re

class LoginForm(forms.Form):
    email=forms.EmailField(
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-input",
                "placeholder": "Email"
            }
        )    
    )

    senha=forms.CharField(
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-input",
                "placeholder": "Senha"
            }
        )
    )

    def clean(self):
        super(LoginForm, self).clean()
        senha= self.cleaned_data.get('senha')
        email = self.cleaned_data.get('email')

        if senha == '':
            raise ValidationError("A senha não pode estar vazia") 
        if not auth.authenticate(username=email, password=senha):
            raise ValidationError("Credenciais Inválidas, verifique seu E-mail e Senha!")   

        return self.cleaned_data
    

    def clean_email(self):
        email= self.cleaned_data.get('email')
        email_regex = r"^\S+@\S+\.\S+$"
        if email == '':
            raise ValidationError("O Email não pode estar vazio")
        if re.match(email_regex, email) == False:
            raise ValidationError("Email inserido é Inválido")
        return email

class CadastroForm(forms.Form):
    email=forms.EmailField(
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-input",
                "placeholder": "Email"
            }
        )    
    )
    
    senha_1=forms.CharField(
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "strongPassword form-input",
                "placeholder": "Senha"
            }
        )
    )

    senha_2=forms.CharField(
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "strongPassword form-input",
                "placeholder": "Confirmar Senha"
            }
        )
    )
    
    def clean(self):
        super(CadastroForm, self).clean()
        senha1 = self.cleaned_data['senha_1']
        senha2 = self.cleaned_data['senha_2']

        if senha1 != senha2:
            raise ValidationError("As Senhas diferem!")
        if senha1 == '' or senha2 == '':
            raise ValidationError("As senhas não podem estar vazias")
        return self.cleaned_data
    
    def clean_email(self):
        email= self.cleaned_data['email']
        email_regex = r"^\S+@\S+\.\S+$"
        if email == '':
            raise ValidationError("O Email não pode estar vazio")
        if re.match(email_regex, email) == False:
            raise ValidationError("Email inserido é Inválido")
        return email
    
class EsqueciSenhaForm(forms.Form):
    email=forms.EmailField(
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "id": "main-input",
                "placeholder": "Email"
            }
        )    
    )
    
    def clean_email(self):
        email= self.cleaned_data.get('email')
        email_regex = r"^\S+@\S+\.\S+$"
        if email == '':
            raise ValidationError("O Email não pode estar vazio")
        if re.match(email_regex, email) == False:
            raise ValidationError("Email inserido é Inválido")
        if email is None or not User.objects.filter(username=email).exists():
            raise ValidationError("Credenciais Inválidas, verifique se esse Email está vinculado a sua conta!")
        return email
    
class NovaSenhaForm(forms.Form):
    senha=forms.CharField(
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "id": "main-input",
                "placeholder": "Senha"
            }
        )    
    )

    senha2=forms.CharField(
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "id": "main-input",
                "placeholder": "Digite Novamente sua Senha"
            }
        )    
    )
    
    def clean(self):
        super(NovaSenhaForm, self).clean()
        senha = self.cleaned_data.get('senha')
        senha2 = self.cleaned_data.get('senha2')

        if senha != senha2:
            raise ValidationError("As Senhas diferem!")
        if senha == '' or senha2 == '':
            raise ValidationError("As senhas não podem estar vazias")
        return self.cleaned_data


class RegistroLivrosForm(forms.ModelForm):

    class Meta:
        model = BookRegister
        fields = '__all__'

    nameBook=forms.CharField(
        required=True,
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome"
            }
        )    
    )

    CHOICES=[
        ('Livro', 'livro'),
        ('Periódico', 'Periódico'),
        ('Folheto Técnico', 'Folheto Técnico')
            ]
    categoria=forms.ChoiceField(
        required=True,
        widget=forms.Select(
            attrs={
                "id": "subject_input"
            }
        ), choices=CHOICES
    )


    CHOICES=[
        (True, 'Disponível'),
        (False, 'Indisponível')
            ]
    disponivel=forms.ChoiceField(
        required=True,
        widget=forms.Select(
            attrs={
                "id": "subject_input"
            }
        ), choices=CHOICES
    )

    authorBook=forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Autor"
            }
        )    
    )
    editoraBook=forms.CharField(
        required=False,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Editora"
            }
        )    
    )

    CHOICES=[
        ('Novo', 'Novo'),
        ('Seminovo', 'Seminovo'),
        ('Usado', 'Usado'),
            ]
    estado=forms.ChoiceField(
        required=True,
        widget=forms.Select(
            attrs={
                "id": "subject_input"
            }
        ), choices=CHOICES
    )

    descrição=forms.CharField(
        required=False,
        max_length=255,
        widget=forms.Textarea(
            attrs={
                'id': 'message-input',
                'cols': 30,
                'rows': 5
            }
        )
    )

    def clean_name(self):
        name = self.cleaned_data.get('name')
        
        if name == '':
            raise ValidationError("O campo Nome não pode estar vazio!")
        

class EmprestimoLivrosForm(forms.Form):
    name=forms.CharField(
        required=True,
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome"
            }
        )    
    )
    
    email=forms.EmailField(
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email"
            }
        )    
    )

    CHOICES=[(book, book) for book in BookRegister.objects.all() if book.disponivel == True]
    livro=forms.ChoiceField(
        required=True,
        widget=forms.Select(
            attrs={
                "id": "subjectinput"
            }
         ), 
         choices=CHOICES
    )

    def clean_name(self):
        name = self.cleaned_data.get('name')
        
        if name == '':
            raise ValidationError("O campo Nome não pode estar vazio!")
    
    def clean_email(self):
        email= self.cleaned_data.get('email')
        email_regex = r"^\S+@\S+\.\S+$"
        if email == '':
            raise ValidationError("O Email não pode estar vazio")
        if re.match(email_regex, email) == False:
            raise ValidationError("Email inserido é Inválido")
        return email