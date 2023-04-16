## Instalación

Primero instalamos los requirements:
````
pip install requirements.txt
```

Aplicamos las migraciones y ejecutamos el servidor, que ya estaría listo para funcionar:
```
python manage.py migrate

python manage.py runserver
```


## Que repositorio usar:
Para esta API usaremos PostgreSQL. Para almacenar datos, realizar consultas de manera rápida siempre opto por una base de datos relacional. SQL server también podría ser una opción. Si quisieramos una base de datos no relacional, pensando en su escalabilidad y su capacidad para manejar datos no estructurados, elegiría mongodb.

Para integrar las bases de datos en la API, con django es muy sencillo:

SQL:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'name_db',
        'HOST': 'localhost', #or any IP address
        'PORT': 'port_db',
        'USER': 'user_db',
        'PASSWORD': 'pass_db',
    }
}
```

NoSQL:

Django está pensado para ser usado con una base de datos relacional. Si queremos conectar una base de datos no relacional, la estructura sería algo más compleja, y tendríamos que usar una librería llamada djongo.


```
  DATABASES = {
       'default': {
           'ENGINE': 'djongo',
           'NAME': 'your-db-name',
       }
   }

```

Ejemplo de un modelo:
```
from djongo import models

class Entry(models.Model):
    blog = models.ArrayField(
        model_container=Blog
    )    
    headline = models.CharField(max_length=255)    

e = Entry()
e.blog = [
    {'name': 'Djongo'}, {'name': 'Django'}, {'name': 'MongoDB'}
]
e.headline = 'Headline example'
e.save()

```
