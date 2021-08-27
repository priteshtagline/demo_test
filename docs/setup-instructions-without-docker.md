# python-drf

## Setup Project Without Docker

### Basic set up.

1. Create a virtual environments(macOS)

```sh
python3 -m venv env
```

2. Activate virtual environments

```sh
source env/bin/activate
```

3. Install require library.

```sh
pip3 install -r requirements.txt
```

4. The following DATABASES variable value replace in setting.py files.

```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

5. The following command throgh migrate database.

```sh
python3 manage.py migrate
```

6. Add demo data using fixtures.

```sh
python3 manage.py loaddata user_fixtures.json

python3 manage.py loaddata product_fixtures.json

python3 manage.py loaddata map_history_fixtures.json
```

7. The following command throgh server running.

```sh
python3 manage.py runserver 
```

You can go to the http://127.0.0.1:8000/ to view the application running.
