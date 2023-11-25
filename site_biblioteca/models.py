from django.db import models

class BookRegister(models.Model):
    id = models.AutoField(primary_key=True)
    nameBook = models.CharField(max_length=200)
    authorBook = models.CharField(max_length=100)
    descrição = models.CharField(max_length=255)
    estado = models.CharField(max_length=10)
    editoraBook = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True)
    categoria = models.CharField(max_length=50)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nameBook


class BorrowingData(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    book = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='borrowing_pdfs', default='emprestimos.pdf')
    email = models.EmailField(max_length=299)
