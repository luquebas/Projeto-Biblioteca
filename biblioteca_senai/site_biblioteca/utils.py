import requests
from django.templatetags.static import static
from .models import BookRegister
from fpdf import FPDF
import random
import pandas as pd
from xhtml2pdf import pisa
from io import BytesIO

class GeradorPdf(FPDF):
    
    def header(self):
        #logo
        self.image('templates/static/autenticar/img/senai-logo.png', 10, 8, 40)
        #fonte
        self.set_font('Times', 'B', 18)
        #Margem
        self.cell(80)
        #Título
        self.cell(50,10,'Comprovante do Empréstimo de Livro', border=False, align='C')
        #Quebra de Linha
        self.ln(20)
    
    def footer(self):
        #Posição do rodapé
        self.set_y(-15)
        #Fonte
        self.set_font('Times', 'I', 10)
        #Page Number
        self.cell(0,10, f'{self.page_no()} / {{nb}}', align='C')

    def chapter_body(self, name, book):
        self.add_page()
        self.set_auto_page_break(auto=True,margin=20)

        #Total de Páginas
        self.alias_nb_pages()

        #Especificando Fonte ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats'), ('B'(Bold), 'I'(Italico), ''(Regular) 'U'(Underline), Tamanho)
        self.set_font('Times', '', 16)

        #Adicionar Texto: Width('w'), Height('h') ln=True border=True
        self.cell(40, 20, 'Araguaína - Centro de Educação e Tecnologia - CETEC' )

        self.set_text_color(79,79,79)
        self.set_font('Times', '', 15)

        self.cell(10, 40, 'Recibo de empréstimo',  border=False, align='R')
        
        self.cell(33, 60, f'Usuário: {name}', border=False, align='R')

        self.cell(69, 80, f'ID:id - {book}', border=False, align='R')

        
        self.cell(-81.5, 100, f'Data de empréstimo: data', border=False, align='R')

        self.cell(-3, 120, f'Data de devolução: 00/00/0000', border=False, align='R')

        self.set_text_color(0,0,0)

        self.cell(50, 160, 'Segue as orientações para facilitar a organização da biblioteca: ', border=False, align='C')

        self.set_text_color(79,79,79)
        self.set_font('Times', '', 15)

        self.cell(-45, 185, 'A devolução dos livros deve ser feita na recepção da biblioteca do SENAI-TO. Isso porque,', border=False, align='C')
        self.ln(20)
        self.cell(0, 155, 'caso o aluno devolva diretamente às estantes, não será possível dar baixa no sistema.', border=False, align='C')
        self.ln(20)
        self.cell(0, 140, 'Ao realizar os empréstimos dos livros, não deve devolve-los rasgados, sujos ou com ', border=False, align='C')
        self.ln(20)
        self.cell(0, 110, 'escritas e deve cumprir com o prazo de entrega (15 dias).', border=False, align='C')
        self.ln(20)



def return_image(name):
    response = requests.get(f'https://openlibrary.org/search.json?q={name}')
    data = response.json()
    static_img = static('autenticar/img/nao-encontrado.jpeg')

    if 'docs' in data and 'isbn' in data['docs'][0]:
        isbn = data['docs'][0]['isbn'][0]
        img_response = requests.get(f"https://covers.openlibrary.org/b/isbn/{isbn}-M.jpg?default=false")

        if img_response.status_code != 404:
            return f"https://covers.openlibrary.org/b/isbn/{isbn}-M.jpg?default=false"
        else:
            return static_img
    return static_img

def gerar_codigo():
    nums = []
    for i in range(0,6):
        nums.append(str(random.randint(0,9)))
        codigo = ''.join(nums)
    return codigo


def relatorio_estoque():
    query = BookRegister.objects.values('nameBook', 'estoqueBook')

    dataframe = pd.DataFrame.from_records(query)
    dataframe.loc['Total'] = pd.Series(dataframe['estoqueBook'].sum(), index=['estoqueBook'])
    
    html = dataframe.to_html()
    html = f"""
            <html>
            <head>
                <style>
                    table {{
                        border-collapse: collapse;
                        width: 100%;
                    }}
                    th, td {{
                        padding: 8px;
                        border-bottom: 1px solid #ddd;
                    }}
                    th {{
                        background-color: #f2f2f2;
                    }}
                    h1 {{
                        display: flex;
                        justify-content: center;
                        align-items: center;
                    }}
                </style>
            </head>
            <body>
                <h1>Relatório da Quantidade de Livros</h1>
                {html}
            </body>
            </html>
        """
    pdf_data = BytesIO()

    pisa.CreatePDF(html, dest=pdf_data)

    with open('relatorio.pdf', 'wb') as pdf_file:
        pdf_file.write(pdf_data.getvalue())

    pdf_file = open('relatorio.pdf', 'rb')
    pdf_bytes = pdf_file.read()
    pdf_file.close()

    return pdf_bytes