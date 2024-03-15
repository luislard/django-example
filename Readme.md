# Start the project using venv

```
python3 -m venv .venv
source .venv/bin/activate
cd src
pip install -r requirements.txt
python manage.py migrate
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

### Create superuser
```
python manage.py createsuperuser
```

### Dump dependencies
``` 
pip freeze > requirements.txt
```

### Revert all migrations
```
# python manage.py migrate <app> zero
python manage.py migrate pages zero
```