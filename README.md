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



