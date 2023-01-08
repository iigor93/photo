# Website for photographer

Python 3.10, Django 4.1, Postgres (Docker)
Free HTML template (Bootstrap, jQuery)

__Proxy server:__ Nginx (also manage all static and media files)

__WSGI server:__ Gunicorn

## Architecture
**: photo**

Main Django app (with settings.py file)

**:: core**

Main app

**:: blog**

Blog app. Blog item, images and tags

**:: price**

Price and FAQ app.

## Static and Media

All static files collected in _static_ folder. All user files collected in _media_ folder.

## Templates

Every app has its own template folder. And there is also main _templates_ folder.

## ADDITIONS:

To run this projects you also need:
>_.env_ file in _photo_ directory, included:
>> DJANGO_SECRET_KEY
>> ALLOWED_HOST: _list of allowed host_
>> DEBUG: "True" or "False"
>> CSRF_TRUSTED_ORIGINS: _your host name_
>> DB_NAME: _database name_
>> DB_USER: _database user_
>> DB_PASSWORD: _database password_
>> DB_HOST: _database host_
>> DB_PORT: _database port_

> Postgres database 
