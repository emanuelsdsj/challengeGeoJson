Primeiro queria agradecer por esse challenge, aprendi muita coisa =)

Nunca trabalhei com GeoJSON, mas nada que uma estudada na documentação do Django, GeoDjango e GeoJSON não resolvesse o problema.

Eu decidi apenas fazer a API como vocês pediram, logo não fiz a interface, testei com a interface padrão do Django Rest Framework e do Admin Django e também testei com o Postman.

Os maiores problemas que encontrei foram configurar o ambiente para usar a lib que me permitia salvar no banco o MultiPolygon e o Point, essa lib foi o GDAL e como eu uso o ArchLinux, precisei instalar o GDAL e suas dependências, por isso não precisei usar o pip install. 
Não sei como configurar no Windows, Ubuntu e Mac, mas acredito que seja mais simples.


# config básica

Usei pipenv como virtual machine:

- pip install pipenv

para iniciar:

- pipenv shell

instala os packages:

- pip install -r requirements.txt

eu usei o postgreSQL, não testei outras databases.
É necessário mudar no settings.py, caso use o postgres só precisa mudar o name, user e password.
```
 DATABASES = {
     'default': {
         'ENGINE': 'django.contrib.gis.db.backends.postgis',
         'NAME': 'postgrestest',
         'USER': 'postgres',
         'PASSWORD': 'teste159753',
     }
 }
```
Iniciar:

- python manage.py runserver


# Serviços principais:

Retorna todos os partners: 

- /partners/

Retorna partner por id: 
<int:pk> = id = integer

- /partners/<int:pk>/

Retorna o partner mais próximo dado uma localização específica: 
<str:lat> = latitude = string
<str:lon> = longitude = string

- /partners/closest/<str:lat>/<str:lon>/

Para criar um partner pode ser através de uma requisição POST para o url que retorna todos os partners: 

- /partners/

Não precisa do id.
Exemplo:
```
 {
    "tradingName": "Adega Pinheiros",
    "ownerName": "Joao Maradona",
    "document": "18.293.334/0001-66",
    "coverageArea": {
        "type": "MultiPolygon",
        "coordinates": [
        [
            [
                [
                    -43.17633,
                    -22.91514
                ],
                [
                    -43.18113,
                    -22.92035
                ],
                [
                    -43.18508,
                    -22.93063
                ],
                [
                    -43.20723,
                    -22.9334
                ],
                [
                    -43.21032,
                    -22.95324
                ],
                [
                    -43.23332,
                    -22.96541
                ],
                [
                    -43.23555,
                    -22.97805
                ],
                [
                    -43.23981,
                    -22.9871
                ],
                [
                    -43.2475,
                    -22.99535
                ],
                [
                    -43.24984,
                    -23.00175
                ],
                [
                    -43.24233,
                    -23.00207
                ],
                [
                    -43.22838,
                    -22.99314
                ],
                [
                    -43.18939,
                    -22.99287
                ],
                    -22.96343
                ],
                [
                    -43.14839,
                    -22.94877
                ],
                [
                    -43.14991,
                    -22.93747
                ],
                [
                    -22.9336
                ],
                [
                    -43.16615,
                    -22.9208
                ],
                [
                    -43.16914,
                    -22.91575
                ],
                [
                    -43.17633,
                    -22.91514
                ]
            ]
        ]
        ]
    },
    "address": {
        "type": "Point",
        "coordinates": [
        -43.193417,
        -22.958384
        ]
    }
 }
```
ou, utilizando o admin do django que é uma interface bem simples de entender.

- /admin/

Para criar um super user para logar no admin:

- python manage.py createsuperuser

# Serviços de testes - JSON direto da url:
https://raw.githubusercontent.com/ZXVentures/code-challenge/master/files/pdvs.json

Retorna todos os partners: 

- /gitjson/

Retorna partner por id:
<int:pk> = id = integer

- /gitjson/<int:pk>/

Retorna o partner mais próximo dado uma localização específica: 
<str:lat> = latitude
<str:lon> = longitude

- /gitjson/closest/<str:lat>/<str:lon>/

Não fiz requisição POST nos testes.


Subi para o heroku, mas a free database não suporta GDAL, então só funcionam os serviços de teste, pois eles não precisam

https://challengegeojson.herokuapp.com/gitjson/
