# Flask REST demo

## Development

install requirements

```
$ pip install -r requirements.txt
```

set database url and app

```
$ export DATABASE_URL=mysql+pymysql://root:root@localhost:3306/demo
$ export FLASK_APP="restdemo:create_app()"
```

inital database tables

```
$ flask db init
$ flask db migrate
$ flask db upgrade
```

run the application

```
$ flask run
 * Tip: There are .env files present. Do "pip install python-dotenv" to use them.
 * Serving Flask app "restdemo:create_app()"
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```

## Testing

```
$ pip install -r requirements.txt
$ python -m unittest discover
```

## Production

install requirements

```
$ pip install -r requirements.txt
```

set database url and app

```
$ export DATABASE_URL=mysql+pymysql://root:root@localhost:3306/demo
$ export FLASK_APP="restdemo:create_app()"
```

inital database tables

```
$ flask db init
$ flask db migrate
$ flask db upgrade
```

run the application

```
$ pip install gunicorn
$ gunicorn -w 4 --bind=0.0.0.0:8000 restdemo.wsgi:application
```
