# Start the project using venv

```
python3 -m venv .venv
source .venv/bin/activate
cd src
python manage.py runserver
```

## Useful commands

### Apply migrations
```
python manage.py migrate
```

### Create migrations
```
python manage.py makemigrations
```

### Create an app
```
python manage.py startapp instruments
```