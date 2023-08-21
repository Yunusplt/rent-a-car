## Template (PostgreSQL, Swagger, Redoc, Debugtoolbar)

### Steps
- python -m venv env
- ./env/script/activate
- pip install djangorestframework
- python.exe -m pip install --upgrade pip
- pip install python-decouple
- create .env file
- create .gitignore
- pip freeze > requirements.txt

### PostgreSQL
- pip install psycopg2 (ERROR) (for postgresql)
- error verdikten sonra.
-- env folder delete
-- python -m venv env
-- ./env/script/activate
-- pip install -r .\requirements.txt
-- again $ pip install psycopg2 (successfully)

### Install Swagger and Redoc  (for API documantion)
- https://drf-yasg.readthedocs.io/en/stable/readme.html?highlight=installation#installation
- pip install -U drf-yasg   add installed app 'drf_yasg',
- in urls.py add... mevcut urls.py icerigini sil burdan gelen codeblogunu yapistir. 
- migrate and look at Browser swagger

### Install Debug Toolbar
- https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
- pip install django-debug-toolbar
- installed app  "debug_toolbar",
- "debug_toolbar.middleware.DebugToolbarMiddleware",       !! add to the Top !!
- INTERNAL_IPS = [          in base.py add to the bottom.
    # ...
    "127.0.0.1",
    # ...
]


### 
- delete settings.py and create settings folder.
- create files dev.py and prod.py 
- we want to see debugtoolbar only in devolopment process. therefore all codes about debugtoolbar are in dev.py
- descripe your Postgresql information in prod.py 

### PostgreSQL (pgAdmin 4)
- go to App
- create a database
- write ENV_NAME=prod in .env file.
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
- look at the pgadmin app (PostgreSQL)
- 
