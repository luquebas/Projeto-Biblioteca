# Senai Library Project ∙ Araguaína - TO
🌍
*[Português](README.md) ∙ [English](README-en.md)*

A library system based on `python3.11` and `Django4.2`.

|||
| -- | -- |
|Back-end| [![Back_Technologies](https://skillicons.dev/icons?i=python&theme=dark)](https://skillicons.dev)|
|Front-end| [![Front_Technologies](https://skillicons.dev/icons?i=html,css,js,bootstrap&theme=dark)](https://skillicons.dev)|
|Frameworks| [![Front_Technologies](https://skillicons.dev/icons?i=django&theme=dark)](https://skillicons.dev)|
|Database| [![Technologies](https://skillicons.dev/icons?i=postgresql&theme=dark)](https://skillicons.dev)|
|Environments| [![Technologies](https://skillicons.dev/icons?i=vscode,github,googlecloud&theme=dark)](https://skillicons.dev)|
|Other Technologies Used| [![Technologies](https://skillicons.dev/icons?i=git,figma&theme=dark)](https://skillicons.dev)|

## Main Features
- Login OAuth supported - Google.
- API Open Library to request Images and JSONs.
- Unit Tests to have a better software construction and maintenance using Unittest Framework.
- SMTP protocol to transfer user password recovery emails and notifications.
- Sidebar, dark mode and responsive interface for a better user experience.
- System registered in a domain.
- Database Postgresql created on Google Cloud to store application, user, report and notification data.
- Google Cloud used to deploy the application.
- Python libraries to generate reports, tables and graphs.

---

## Running this project

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal linux or windows terminal, run the following command in the base directory of this project

```
virtualenv env
```

That will create a new folder `env` in your project directory. Next activate it with this command on linux:

```
source env/bin/active
```

Then install the project dependencies with

```
pip install -r requirements.txt
```

Now you can run the project with this command

```
python manage.py runserver
```

**Note** if you want Google OAuth to work you will need to enter your own Google API keys into the `.env` file in the settings files.

**Note** you have to create a PostgreSQL database and enter your own database data into the `.env`file in the settings filés.

---