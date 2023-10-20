# Projeto Família com Django

Este é um projeto simples criado para prática com o framework Django. O objetivo do projeto é gerenciar informações sobre membros da família, incluindo nome, idade, parentesco e status de falecido.

## Passos para Execução

1. Crie um ambiente virtual Python:
```python
 $ python -m venv dsweb
```

2. Ative o ambiente virtual no Windows: 
```python
$ dsweb\Scripts\activate
```

3. Instale o Django:
```python
$ pip install django
```

4. Crie um projeto Django:
```python
$ django-admin startproject pratica1
```

5. Crie uma aplicação chamada "familiares":
```python
$ python manage.py startapp familiares
```

6. Defina o modelo "Familiar" com os campos necessários (nome, idade, parentesco e falecido) na aplicação "familiares".

7. Adicione a aplicação "familiares" à lista de `INSTALLED_APPS` no arquivo `settings.py`.

8. Gere e aplique a migração para criar o banco de dados:
```python

$ python manage.py makemigrations
$ python manage.py migrate
```


9. Registre a classe de modelo "Familiar" para ser utilizada na interface de administração do Django:
```python
# Em familiares/admin.py
from django.contrib import admin
from .models import Familiar


admin.site.register(Familiar)
```
10. Crie um super usuário 
```python
$ python manage.py createsuperuser
```
11. Acesse a interface de administração do Django e cadastre 10 familiares seus.

12. Crie uma classe de visão e seu respectivo template para exibir a lista completa de familiares.

## 🚀 Tecnologias Necessárias

Para executar este projeto, você precisará das seguintes tecnologias:

- **Python:** 🐍 É a linguagem de programação utilizada para desenvolver a aplicação. Certifique-se de ter o Python instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).

- **Django:** 🌐 O framework web Django é usado para criar a aplicação. Você pode instalá-lo via pip, o gerenciador de pacotes do Python:

```python
$ pip install django
```

- **Ambiente Virtual:** 📦 Recomenda-se criar um ambiente virtual para isolar as dependências deste projeto de outros projetos Python. Você pode criar um ambiente virtual usando o módulo `venv` (Python 3.3+) ou `virtualenv`. Por exemplo:

```python
$ python -m venv dsweb
```

- **Navegador Web:** 🌐 Para acessar a interface de administração e visualizar a aplicação, você precisará de um navegador web, como Google Chrome, Mozilla Firefox, ou outro de sua escolha.

Essas são as principais tecnologias necessárias para realizar este projeto. Certifique-se de ter todas elas configuradas antes de seguir os passos descritos no arquivo `Readme.md`.
