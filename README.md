# Django Template File Structure

This is just a initial django app with comments added to specify the templating structure clearly and how it should be configured and used. This is also meant to be just a git clone template that anyone can clone and start their django projects with
the templates already setup.

## Template Structure

If you want to use a template from the root template folder, you just give the name of the template like 'base.html' and if you want to use an app template, you use 'appname/base.html'

```
project/
  appname/
    templates/ 
      appname/  <-- another folder with app name so 'appname/base.html' is from here
        base.html
    views.py
    ...

  templates/    <-- root template folder so 'base.html' is from here
    base.html

  settings.py
  views.py
  ...
```

## How to install

```bash
$ cd todo_app
$ python -m venv env
$ source ./env/bin/activate
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

## Deployment

It is possible to deploy to services such as [render](https://render.com/) or to your own server.


## License

The MIT License (MIT)