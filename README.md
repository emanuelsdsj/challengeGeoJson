Primeiro queria agradecer por esse challenge =)

Nunca trabalhei com GeoJSON, mas nada que uma estudada na documentação do Django, GeoDjango e GeoJSON não resolvesse o problema.

Eu decidi apenas fazer a API como vocês pediram, logo não fiz a interface, testei com a interface padrão do Django Rest Framework e do Admin Django e também testei com o Postman.

Os maiores problemas que encontrei foram configurar o ambiente para usar a lib que me permitia salvar no banco o MultiPolygon e o Point, a lib que mais deu problema foi o GDAL como eu uso o ArchLinux precisei instalar o GDAL no sistema e suas dependências, por isso não precisei usar o pip install. 
Não sei como configurar no Windows, Ubuntu e Mac, mas acredito que seja mais simples.

# config básica

Usei pipenv como virtual machine:

- pip install pipenv

para iniciar:

- pipenv shell

instala os packages:

- pip install -r requirements.txt

eu usei o postgres, é necessário pelo menos uma dessas database:

- PostgreSQL, MySQL, Oracle, SQLite

É necessário mudar no settings.py a database, caso use o postgres só precisa mudar o name, user e password.

para rodar:

- python manage.py runserver


# Serviços principais:

Retorna todos os partners: 

- /partners/

Retorna partner por id: 

- /partners/<int:pk>/

Retorna o partner mais próximo dado uma localização específica: 

- /partners/closest/<str:lat>/<str:lon>/

Para criar um partner pode ser através de uma requisição POST para o url que retorna todos os partners: 

- /partners/

ou, utilizando o admin do django que é uma interface bem simples de entender.

- /admin/

# Serviços de testes - JSON direto da url:
https://raw.githubusercontent.com/ZXVentures/code-challenge/master/files/pdvs.json

Retorna todos os partners: 

- /gitjson/

Retorna partner por id: 

- /gitjson/<int:pk>/

Retorna o partner mais próximo dado uma localização específica: 

- /gitjson/closest/<str:lat>/<str:lon>/

Não fiz requisição POST nos testes.

