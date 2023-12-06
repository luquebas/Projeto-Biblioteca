# Projeto Biblioteca Senai ∙ Araguaína - TO
🌍
*[Português]( README.md ) ∙ [Inglês](README-en.md)*

Um sistema biblioteca construído utilizando `python3.11` e `Django4.2`.

|||
| -- | -- |
|Back-end|  [![Back_Technologies](https://skillicons.dev/icons?i=python&theme=dark)]( https://skillicons.dev ) |
|Front-end|  [![ Front_Technologies]( https://skillicons.dev/icons?i=html,css,js,bootstrap&theme=dark )]( https://skillicons.dev ) |
|Estruturas|  [![ Front_Technologies ]( https://skillicons.dev/icons?i=django&theme=dark )]( https://skillicons.dev ) |
|Banco de Dados| [![ Tecnologias ]( https://skillicons.dev/icons?i=postgresql&theme=dark )]( https://skillicons.dev ) |
|Ambientes|  [![ Tecnologias ](https://skillicons.dev/icons?i=vscode,github,googlecloud&theme=dark )]( https://skillicons.dev ) |
|Outras tecnologias utilizadas| [![Tecnologias](https://skillicons.dev/icons?i=git,figma&theme=dark)](https://skillicons.dev) |

---

## Principais características
- Login OAuth suportado - Google.
- Utilização da API Open Library para requisição de imagens e JSONs.
- Testes Unitários envolvem a melhor construção e manutenção do código com a utilização do Framework Unittest.
- Protocolo SMTP para envio de e-mails de recuperação de senhas de usuário e notificações.
- Menu Lateral, modo escuro e interface responsiva para melhoria da experiência do usuário.
- Sistema registrado em um domínio.
- Banco de Dados Postgresql criado no Google Cloud para armazenamento de dados da aplicação, usuários, relatórios e notificações.
- Deploy da aplicação feita através do Google Cloud.
- Bibliotecas python para gerar gráficos, tabelas e relatórios.

---

## Executando este projeto

Para colocar este projeto em funcionamento você deve começar instalando o Python em seu computador. É aconselhável criar um ambiente virtual para armazenar as dependências dos seus projetos separadamente. Você pode instalar o virtualenv com

```
pip install virtualenv
```

Clone ou baixe este repositório e abra-o no editor de sua preferência. Em um terminal linux ou windows, execute o seguinte comando no diretório base deste projeto

```
virtualenv env
```

Isso criará uma nova pasta `env` no diretório do seu projeto. Em seguida, ative-o com este comando no Linux:

```
source env/bin/activate
```

Em seguida, instale as dependências do projeto com

```
pip install -r requirements.txt
```

Agora você pode executar o projeto com este comando

```
python manage.py runserver
```

**Observação** se quiser que o Google OAuth funcione, você precisará inserir suas próprias chaves de API do Google no arquivo `.env` nos arquivos de configurações.

**Nota** você deve criar um banco de dados PostgreSQL e inserir seus próprios dados do banco de dados no arquivo `.env` nos arquivos de configurações.

---