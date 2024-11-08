# Proyecto template 2024. 

**Desarrollado por Julian Andres Montoya Carvajal (julianmontoya3.1416@gmail.com)**

Esta es proyecto plantilla utilizando el framework FastAPI 💪 y el ORM SQLModel 💪💪

Para conocer la documentacion del framework visite https://fastapi.tiangolo.com/ y https://sqlmodel.tiangolo.com/

## Iniciar proyecto de desarrollo local desde cero

1) 

a) Instalar Ubuntu (particionando el disco):

    Preferiblemente tener instalado Ubuntu 22.04.3 LTS (Jammy) 
    (Falta documentación)

b) Instalar ubuntu en windows con wsl:
    
    (Falta documentación)

2) Instalar python (Superior a 3.10):

Preferiblemente tener instalado Python version 3.10.12
(Falta documentación)

3) Instalar pip (administrador de paquetes):

(Falta documentación)

4) Establecer entorno virtual:

(Falta documentación)

```bash
virtualenv env --python=python3
```

5) Activa el entorno virtual en linux:

```bash
source env/bin/activate
```

6) Instalar dependencias y asignarlas en requirements.txt

```bash
pip install fastapi
pip install sqlmodel
pip install psycopg2-binary (controlador para db postgresql)
pip install tenacity (para conexion con db)
pip install pydantic-settings (para variables de entorno)
pip install "passlib[bcrypt]" (para la seguridad)
pip install "python-jose[cryptography]" (para la seguridad)
pip install emails (para envio de emails)
pip install weasyprint (para generacion de pdfs)
pip install pytest (para pruebas unitarias)
pip install alembic (para migraciones)
```

```bash
python -m pip freeze > requirements.txt 
```

7) Crea archivo `.env` con variables de entorno necesarias (ver .env_example)

```bash
touch .env
```

8) Establecemos la estructura de carpetas del proyecto y el codigo

```bash
prueba
├── app
│   ├── config
│   │   ├── config.py
│   │   └── __init__.py
│   ├── crud
│   │   ├── hero.py
│   │   ├── __init__.py
│   │   ├── team.py
│   │   └── usuario.py
│   ├── database
│   │   ├── __init__.py
│   │   └── session.py
│   ├── dependencies.py
│   ├── __init__.py
│   ├── main.py
│   ├── models
│   │   ├── hero_model.py
│   │   ├── __init__.py
│   │   ├── prueba_hero_model.py
│   │   ├── team_model.py
│   │   └── usuario_model.py
│   ├── prestart_dev.sh
│   ├── prestart.sh
│   ├── routers
│   │   ├── hero.py
│   │   ├── __init__.py
│   │   ├── login.py
│   │   ├── prueba_hero.py
│   │   ├── team.py
│   │   ├── usuario.py
│   │   └── utils.py
│   ├── schemas
│   │   ├── hero.py
│   │   ├── __init__.py
│   │   ├── prueba_hero.py
│   │   ├── team.py
│   │   ├── token.py
│   │   └── usuario.py
│   ├── security
│   │   ├── __init__.py
│   │   └── security.py
│   ├── services
│   │   ├── _base.py
│   │   ├── hero.py
│   │   ├── __init__.py
│   │   ├── team.py
│   │   └── usuario.py
│   ├── static
│   │   ├── css
│   │   ├── external
│   │   ├── images
│   │   └── js
│   ├── templates
│   │   ├── emails
│   │   ├── pdf
│   │   └── views
│   ├── tests
│   │   ├── conftest.py
│   │   ├── __init__.py
│   │   ├── test_main.py
│   │   └── test_prueba_hero.py
│   └── utils
│       ├── email.py
│       ├── exceptions.py
│       ├── generar_verificar_token_email.py
│       ├── __init__.py
│       ├── pdfs.py
│       └── service_result.py
├── data_fake_desarrollo.sql
├── data_sqlite_env.db
├── docker-compose.override.yml
├── docker-compose.traefik.yml
├── docker-compose.yml
├── Dockerfile
├── .dockerignore
├── .env
├── env
│   ├── bin
│   ├── ...
├── .env_example
├── .git
│   ├── branches
│   ├── ...
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt

```

## Ejecutar la aplicacion localmente (sin base de datos SQLite)

Para ejecutar tu aplicacion ingresa los siguientes comandos para ejecutar el servidor de aplicaciones uvicorn

```bash
uvicorn app.main:app --reload 
```
o
```bash
fastapi dev app/main.py
```

## Ejecutar la aplicacion localmente (con base de datos SQLite y sin generar carpetas __pycache__)

```bash
export PYTHONDONTWRITEBYTECODE=1 && ./app/prestart_dev.sh && uvicorn app.main:app --reload
```
o

```bash
export PYTHONDONTWRITEBYTECODE=1 && ./app/prestart_dev.sh && fastapi dev app/main.py 
```

* Visita `http://localhost:8000/` en tu navegador para acceder a la aplicacion

* Visita `http://localhost:8000/docs` en tu navegador para acceder a la documentación interactiva de la API generada automáticamente por FastAPI

## Subir a github.

Deseamos subir nuestro proyecto a github para ello vamos a ejecutar los siguientes pasos

1) Creamos repositorio en github sin archivo readme.md ya que se encuentra en local.

2) Instalamos git en local

```bash
sudo apt install git
``` 

```bash
git --version
```

3) Debemos establecer  nombre de usuario y dirección de correo electrónico:

```bash
git config –global user.email correo_de_persona
```

```bash
git config –global user.name nombre_de_usuario
```

Para probar que se hizo bien ejecutamos lo siguiente:

```bash
git config --list
```

```bash
git config –global user.email 
```

```bash
git config –global user.name 
```

4) Configuramos proyecto localmente con los siguientes comandos

```bash
git init
```

```bash
git add *
```

añadimos tambien archivos ocultos como .git_ignore y muchos mas

```bash
git commit -m "mi primer commit"
```

5) Conectar repositorio local con repositorio remoto 

```bash
git remote add origin https://github.com/apoyoticsmedicina/prueba.git
```

```bash
git branch -M main
```

```bash
git push -u origin main
```

## Iniciar proyecto de desarrollo desde repositorio

1) 

a) Instalar Ubuntu (particionando el disco):

    Preferiblemente tener instalado Ubuntu 22.04.3 LTS (Jammy) 
    (Falta documentación)

b) Instalar ubuntu en windows con wsl:
    
    (Falta documentación)

2) Instalar python (Superior a 3.10):

Preferiblemente tener instalado Python version 3.10.12
(Falta documentación)

3) Instalar pip (administrador de paquetes):

(Falta documentación)

4) Clonar el repositorio (debe contar con git):

```bash
git clone https://github.com/apoyoticsmedicina/prueba.git
```

```bash
cd prueba
```

5) Establecer entorno virtual:

(Falta documentación)

```bash
virtualenv env --python=python3
```

6) Activa el entorno virtual en linux:

```bash
source env/bin/activate
```

7) Instalar dependendencias:

```bash
pip install -r requirements.txt
```

8) Crea archivo `.env` con variables de entorno necesarias

```bash
touch .env                                               
```

9) Crear base de datos sqlite. Para ello ejecute el script session.py o siga los pasos anteriores de ejecucion con base de datos sqlite

Nota: Tenga en cuenta que para probar scripts debe ejecutar los scripts.py como modulos, es decir, python -m PATH (https://sqlmodel.tiangolo.com/tutorial/code-structure/)

## Iniciar proyecto de desarrollo local con base de datos SQLite

1) Debemos instalar DB Browser for SQLite https://sqlitebrowser.org/

```bash
sudo add-apt-repository -y ppa:linuxgndu/sqlitebrowser
```

```bash
sudo apt-get update
```

```bash
sudo apt-get install sqlitebrowser
```

2) Ahora con la interfaz grafica de SQLite podemos crear un archivo que sera nuestra base de datos o podemos dejar que se cree cuando creamos la base de datos y tablas con SQLModel.

## Iniciar proyecto de desarrollo local con Docker y Docker Compose

* Asegurate de instalar Docker version 24.0.7 y ademas Docker Compose version 2.21.0.
El siguiente link te puede ayudar a obtener los dos https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04

### Etapa de desarrollo con docker  y sqlite

### Etapa de desarrollo con docker y postgresql

## Iniciar proyecto de desarrollo local y produccion con base de datos PostgreSQL

Motor (Engine) de bases de datos compatibles con sqlalchemy:
https://docs.sqlalchemy.org/en/14/core/engines.html
https://docs.sqlalchemy.org/en/14/tutorial/engine.html

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.




