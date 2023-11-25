from django.test import TestCase
from ..models import BookRegister
from ..forms import CadastroForm
from django.contrib.auth.models import User

class CadastroFormTestCase(TestCase):

    def test_registrar_usuario_no_bd(self):
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


class BookRegisterTestCase(TestCase):

    def setUp(self):
        BookRegister.objects.create(
            nameBook="1984",
            authorBook="George Orwell",
            descrição="Os bichos endoidaram",
            estado="Conservado",
            editoraBook="Editora Lua",
            image="https://m.media-amazon.com/images/I/819js3EQwbL._AC_UF1000,1000_QL80_.jpg",
        )

    def test_retorno_str(self):
        book1 = BookRegister.objects.get(nameBook="1984")
        self.assertEquals(book1.__str__(), "1984" )