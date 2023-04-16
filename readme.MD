# Instalación

Primero instalamos los requirements:
```

pip install requirements.txt
```


Aplicamos las migraciones y ejecutamos el servidor, que ya estaría listo para funcionar:
```

python manage.py migrate

python manage.py runserver
```

# API endpoints

La API está ejecutandose en local, por lo que la url será 
http://127.0.0.1:8000/api/


Se puede acceder a las funcionalidades GET y POST del Rest framework con esta dirección:
http://127.0.0.1:8000/api/joke


Para acceder a un elemento en particular utilizamos un path parameter especificando el id. Este endpoint acepta GET, PUT, y DELETE:
http://127.0.0.1:8000/api/joke/1


## get_random
Se hace un get request al siguiente endpoint y devuelve un chiste aleatorio:

http://127.0.0.1:8000/api/get_random/
```
{"text": "Chuck Norris always hits the G-spot with mathematical precision.", "type": "chuck"}

```

Es posible añadir un path parameter al endpoint para especificar el tipo de chiste que se quiere recibir:
http://127.0.0.1:8000/api/get_random/dad

```
{"text": "Recent survey revealed 6 out of 7 dwarf's aren't happy.", "type": "dad"}
```


## get_plusone

Envía un numero al siguiente endpoint con un query parameter y devuelve el mismo número más uno:
http://127.0.0.1:8000/api/get_plusone/?number=3


## get_mcm

Envía una lista de números al endpoint con un query parameter y devuelve el mínimo común múltiplo:

http://127.0.0.1:8000/api/get_mcm/?numbers=2&numbers=4&numbers=6

```
{"list": [2, 4, 6], "mcm": 12}

```


# Que repositorio usar:


La API por defecto está usando sqlite para ejecutarse localmente. Pero la aproximación teórica sería la siguiente:

Para esta API usaría PostgreSQL. Para almacenar datos, realizar consultas de manera rápida siempre opto por una base de datos relacional. SQL server también podría ser una opción. Si quisieramos una base de datos no relacional, pensando en su escalabilidad y su capacidad para manejar datos no estructurados, elegiría mongodb.

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
