from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..forms import CadastroForm, LoginForm
from ..models import BookRegister
from django.contrib import auth

class StatusViewsTestCase(TestCase):
    def setUp(self):
        if not User.objects.filter(username='lucas@gmail.com').exists():
            user = User.objects.create_superuser(
                username='lucas@gmail.com',
                password='meina1246'
        )
            user.save()

    def test_status_login_register_auth_inicio_200(self):
        response = self.client.get(reverse('login_auth'))
        self.assertEquals(response.status_code, 200)

        response2 = self.client.get(reverse('register_auth'))
        self.assertEquals(response2.status_code, 200)

        response3 = self.client.get(reverse('inicio'))
        self.assertEquals(response3.status_code, 200)


    def test_status_home_historico_302_quando_usuario_nao_esta_logado(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 302)

        response2 = self.client.get(reverse('historico'))
        self.assertEquals(response2.status_code, 302)


    def test_status_home_historico_200_quando_usuario_esta_logado(self):
        self.client.login(username='lucas@gmail.com', password='meina1246')

        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

        response2 = self.client.get(reverse('historico'))
        self.assertEquals(response2.status_code, 200)


class InicialViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_inicial_GET(self):
        response = self.client.get(reverse('inicio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'static/inicial.html')   


class RegisterAuthViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_auth_GET(self):
        response = self.client.get(reverse('register_auth'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'static/index.html')

    def test_register_auth_POST(self):
        form = CadastroForm(data={
            'email': 'lukf2007@hotmail.com',
            'senha_1': 'meina1246',
            'senha_2': 'meina1246',
        })
        if User.objects.filter(username=form.data['email']).exists():
            raise ValueError('Usuário já existe')
            
        formregister = User.objects.create_user(
            username=form.data['email'],
            password=form.data['senha_1'],
        )
        formregister.save()
        novo_user = User.objects.get(username='lukf2007@hotmail.com')
        self.assertIsNotNone(novo_user)

class LoginAuthViewsTest(TestCase):
    def setUp(self):
        if not User.objects.filter(username='lucas@gmail.com').exists():
            user = User.objects.create_superuser(
                username='lucas@gmail.com',
                password='meina1246'
        )
            user.save()

    def test_login_auth_GET(self):
        response = self.client.get(reverse('login_auth'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'static/index.html')


    def test_login_auth_POST(self):
        form = LoginForm(data={
            'email': 'lucas@gmail.com',
            'senha': 'meina1246'
        })
        usuario = auth.authenticate(username=form.data['email'], password=form.data['senha'])
        if usuario is not None:
            self.client.login(username=form.data['email'], password=form.data['senha'])

        self.assertTrue(usuario.is_authenticated)

    def test_login_auth_POST_not_login(self):
        form = LoginForm(data={
            'email': 'lucas@gmail.com',
            'senha': 'meina124'
        })
        usuario = auth.authenticate(username=form.data['email'], password=form.data['senha'])
        if usuario is not None:
            self.client.login(username=form.data['email'], password=form.data['senha'])
        self.assertTrue(usuario == None)


class HomeViewsTest(TestCase):
    def setUp(self):
        user = User.objects.create_superuser(
            username='lucas@gmail.com',
            password='meina1246'
        )
        user.save()

        form = LoginForm(data={
            'email': 'lucas@gmail.com',
            'senha': 'meina1246'
        })
        self.client.login(username=form.data['email'], password=form.data['senha'])


    def test_home_GET(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'static/home.html') 


class BookPageViewsTest(TestCase):
    def setUp(self):
        user = User.objects.create_superuser(
            username='lucas@gmail.com',
            password='meina1246'
        )
        user.save()

        form = LoginForm(data={
            'email': 'lucas@gmail.com',
            'senha': 'meina1246'
        })
        self.client.login(username=form.data['email'], password=form.data['senha'])


    def test_dados_livro_GET(self):
        response = self.client.get(reverse('livroview'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'static/dados_livro.html')

class DeleteBookViewsTest(TestCase):
    def setUp(self):
        user = User.objects.create_superuser(
            username='lucas@gmail.com',
            password='meina1246'
        )
        user.save()

        form = LoginForm(data={
            'email': 'lucas@gmail.com',
            'senha': 'meina1246'
        })
        self.client.login(username=form.data['email'], password=form.data['senha'])

        self.book = BookRegister.objects.create(
            nameBook='Livro a ser Excluído',
            authorBook='Autor de Exemplo',
            editoraBook='Editora de Exemplo',
            estado='Novo',
            descrição='Descrição de Exemplo',
            categoria='Categoria de Exemplo',
            disponivel=True,
        )

        self.book.save()

    def test_deletebook(self):
        response = self.client.post(reverse('deletebook', args=[self.book.pk]))
        self.assertRedirects(response, reverse('home'))
        self.assertFalse(BookRegister.objects.filter(pk=self.book.pk).exists())

class historicoViewsTest(TestCase):
    def setUp(self):
        user = User.objects.create_superuser(
            username='lucas@gmail.com',
            password='meina1246'
        )
        user.save()

        form = LoginForm(data={
            'email': 'lucas@gmail.com',
            'senha': 'meina1246'
        })
        self.client.login(username=form.data['email'], password=form.data['senha'])


    def test_historico_GET(self):
        response = self.client.get(reverse('historico'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'static/historico.html') 

class LogoutpTest(TestCase):
    def setUp(self):
        user = User.objects.create_superuser(
            username='lucas@gmail.com',
            password='meina1246'
        )
        user.save()

    def test_logout(self):
        form = LoginForm(data={
            'email': 'lucas@gmail.com',
            'senha': 'meina1246'
        })
        self.client.login(username=form.data['email'], password=form.data['senha'])

        response = self.client.get(reverse('logout'))

        self.assertRedirects(response, reverse('login_auth'))



