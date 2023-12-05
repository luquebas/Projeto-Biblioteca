import requests
from requests.exceptions import RequestException
from django.templatetags.static import static
from .models import BookRegister
import random
import pandas as pd
from xhtml2pdf import pisa
import plotly.express as px
from io import BytesIO

def return_image(name):
    try:
        response = requests.get(f'https://openlibrary.org/search.json?q={name}')
        data = response.json()
        isbn = data['docs'][0]['isbn'][0]
    
        img_url = f"https://covers.openlibrary.org/b/isbn/{isbn}-M.jpg?default=false"

        return img_url 
    
    except:
        static_img = static('autenticar/img/nao-encontrado.jpeg')
        return static_img

def gerar_codigo():
    nums = []
    for i in range(0,6):
        nums.append(str(random.randint(0,9)))
        codigo = ''.join(nums)
    return codigo


def relatorio_estoque():
    query = BookRegister.objects.values('nameBook')

    dataframe = pd.DataFrame.from_records(query)
    dataframe.loc['Total'] = f"{len(BookRegister.objects.all())} Livros"
    
    html = dataframe.to_html()
    html = f"""
            <html>
    <head>
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@100;300;400;500&family=Poppins:wght@100;300&display=swap');
        body {{
            font-family: Poppins;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        main {{
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            overflow-x: auto; /* criar uma rolagem horizontal (dentro da table) caso a table ultrapasse a tela */
            margin: 5% auto;
            max-width: 80%;
        }}
        table {{
            border-collapse: collapse;
            text-align: center;
            color: black;
            font-size: 1rem;
            border: 2px solid black;
        }}
        th {{
            background-color: rgba(30, 143, 255, 0.600);
        }}
        td {{
            background-color: dodgerblue;
            color: #fff;
        }}
        th, td {{
            border: 1px solid black;
            padding: 12px;  
        }}
        svg {{
            padding: 0 4px 0 4px;
            width: 16px;
            height: 16px;
        }}
    </style>
    </head>
    <body>
        <main>
        <table>
            <h1>Relatório da Quantidade de Livros</h1>
            {html}
        </table>    
        </main>
    </body>
    </html>
"""
    pdf_data = BytesIO()

    pisa.CreatePDF(html, dest=pdf_data)

    return pdf_data

def graph_categories():
    livros = BookRegister.objects.filter(categoria="Livro")
    periodicos = BookRegister.objects.filter(categoria="Periódico")
    folheto_tecnico = BookRegister.objects.filter(categoria="Folheto Técnico")

    random_x =[len(livros), len(periodicos), len(folheto_tecnico)]
    names = ['Livro', 'Periódico', 'Folheto Técnico']


    fig = px.pie(values=random_x, color_discrete_sequence=px.colors.sequential.Turbo, names=names, title='Quantidade de Livros por Gênero')

    fig.update_layout(
    paper_bgcolor='rgba(0, 0, 0, 0)',  
    autosize=True 
    )

    return fig

def graph_disponibility():
    disponivel = BookRegister.objects.filter(disponivel=True)
    indisponivel = BookRegister.objects.filter(disponivel=False)

    random_x =[len(disponivel), len(indisponivel)]
    names = ['Disponível', 'Indisponível']

    fig = px.pie(values=random_x, color_discrete_sequence=px.colors.sequential.Agsunset, names=names, title='Quantidade de Livros por Disponibilidade')

    fig.update_layout(
    paper_bgcolor='rgba(0, 0, 0, 0)',  
    autosize=True,
)

    return fig

def graph_estado():
    novo = BookRegister.objects.filter(estado="Novo")
    seminovo = BookRegister.objects.filter(estado="Seminovo")
    usado = BookRegister.objects.filter(estado="Usado")

    random_x =[len(novo), len(seminovo), len(usado)]
    names = ['Novo', 'Seminovo', 'Usado']

    fig = px.pie(values=random_x, color_discrete_sequence=px.colors.sequential.Cividis, names=names, title='Quantidade de Livros por Estado de Conservação')

    fig.update_layout(
    paper_bgcolor='rgba(0, 0, 0, 0)',
    autosize=True,
    )
    

    return fig