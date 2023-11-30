from django.test import TestCase
from ..models import BookRegister, BorrowingData
from ..forms import CadastroForm
from django.contrib.auth.models import User


class BookRegisterTestCase(TestCase):

    def setUp(self):
        book = BookRegister.objects.create(
            nameBook="1984",
            authorBook="George Orwell",
            descrição="Os bichos endoidaram",
            estado="Conservado",
            editoraBook="Editora Lua",
            image="https://m.media-amazon.com/images/I/819js3EQwbL._AC_UF1000,1000_QL80_.jpg",
        )

        book.save()

    def test_registro_book(self):
        self.assertEqual(BookRegister.objects.count(), 1)

    def test_retorno_str(self):
        book1 = BookRegister.objects.get(nameBook="1984")
        self.assertEquals(book1.__str__(), "1984" )

class BorrowingRegisterTestCase(TestCase):

    def setUp(self):
        emprestimo = BorrowingData.objects.create(
            name = "Teste",
            book = "Aparecida",
            email = "teste@gmail.com"
        )

        emprestimo.save()

    def test_registro_emprestimo(self):
        self.assertEqual(BorrowingData.objects.count(), 1)