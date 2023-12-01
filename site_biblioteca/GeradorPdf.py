from fpdf import FPDF
import datetime

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
        
        self.cell(15, 60, f'Usuário: {name}', border=False, align='R')

        self.cell(-22, 80, f'Livro: {book}', border=False, align='R')

        
        self.cell(28, 100, f'Data de empréstimo: {datetime.date.today().strftime("%d/%m/%Y")}', border=False, align='R')

        self.cell(-4, 120, f'Data de devolução: {(datetime.date.today() + datetime.timedelta(days=15)).strftime("%d/%m/%Y")}', border=False, align='R')

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