# Projeto 1b Tecnologias Web - Ricardo Ribeiro Rodrigues.
## [Deploy do site](https://aqueous-hamlet-29504.herokuapp.com).
## Features propostas
- [x] Reimplementar o CRUD da parte A em Django, ou seja, implementar as funcionalidades de criação, listagem, edição e remoção de anotações aplicando o mesmo estilo (css).

- [x] Utilizar o PostgreSQL (em um container Docker) ao invés do SQLite.

- [x] Implementar o sistema de tags para as anotações.

- [x] Publicar a página.

## Features adicionais (Conceito A+)
- [x] Paginas de erro (404 e 500) personalizadas.

- [x] Possibilidade de uma nota ter múltiplas tags (ManyToMany).

- [x] Update e delete na página de todas as notas de uma tag.

## Para rodar local
Rode uma imagem docker do postgres na porta **5432**, e rode o servidor com o seguinte comando:
```cmd
python manage.py runserver
```
Se der algum erro, altere no arquivo getit/settings.py as configurações de database:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'getit',
        'USER': 'getituser',
        'PASSWORD': 'getitsenha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
