from django.test import TestCase
from ..forms import CadastroForm, LoginForm, EsqueciSenhaForm, NovaSenhaForm, RegistroLivrosForm, EmprestimoLivrosForm
from django.contrib.auth.models import User

class CadastroTestCase(TestCase):
    def test_estrutura_email_valida(self):
        form = CadastroForm(data= {
            'email': 'lukf2007@hotmail.com',
            'senha_1': 'meina1246',
            'senha_2': 'meina1246',
        })
        self.assertTrue(form.is_valid())

    def test_estrutura_email_vazia(self):
        form = CadastroForm(data= {
            'email': '',
            'senha_1': 'meina1246',
            'senha_2': 'meina1246',
        })
        self.assertFalse(form.is_valid())

    def test_estrutura_senha_diferente(self):
        form = CadastroForm(data={
            'email': 'lukf2007@hotmail.com',
            'senha_1':'meina1246',
            'senha_2': 'meina0127',
        })
        self.assertFalse(form.is_valid())

    def test_estrutura_email_invalido(self):
        form = CadastroForm(data={
            'email': 'abcdefg',
            'senha_1': 'meina1246',
            'senha_2': 'meina1246',
        })
        self.assertFalse(form.is_valid())

class EsqueciSenhaTestCase(TestCase):
    def setUp(self):
        if not User.objects.filter(username='lucas@gmail.com').exists():
            user = User.objects.create_superuser(
                username='lucas@gmail.com',
                password='meina1246'
        )
            user.save()

    def test_email_vazio(self):
        form = EsqueciSenhaForm(data={
            'email': ''
        })
        self.assertFalse(form.is_valid())
    
    def test_email_estrutura_invalida(self):
        form = EsqueciSenhaForm(data={
            'email': 'lukf2007@hotmail'
        })
        self.assertFalse(form.is_valid())

    def test_email_nao_vinculado_alguma_conta(self):
        form = EsqueciSenhaForm(data={
            'email': 'carlinhos@gmail.com'
        })
        self.assertFalse(form.is_valid())

    def test_email_funcionando(self):
        form = EsqueciSenhaForm(data={
            'email': 'lucas@gmail.com'
        })
        self.assertTrue(form.is_valid())

class NovaSenhaTestCase(TestCase):
    def test_estrutura_senha_diferente(self):
        form = NovaSenhaForm(data={
            'senha':'meina1246',
            'senha2': 'meina0127',
        })
        self.assertFalse(form.is_valid())

    def test_senha_vazia(self):
        form = NovaSenhaForm(data={
            'senha': '',
            'senha2': '',
        })
        self.assertFalse(form.is_valid())     

    def test_senha_valida(self):
        form = NovaSenhaForm(data={
            'senha': 'lucas123',
            'senha2': 'lucas123',
        })
        self.assertTrue(form.is_valid())  
        