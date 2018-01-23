# Infinity

[![Build Status](https://travis-ci.org/aezik/infinity.svg?branch=master)](https://travis-ci.org/aezik/infinity)

Install psql (PostgreSQL) 10.1, `createdb infinity`

`git clone git@github.com:inxyz/infinity.git`

Then:

```
cd infinity
pipenv shell
pipenv install
python manage.py migrate
python manage.py runserver
```

Apply fixtures:

```
python manage.py loaddata languages currencies
python manage.py loaddata currency_price_snapshots
python manage.py loaddata hour_price_snapshots
```

Create superuser:
```
$ python manage.py createsuperuser
Username: admin
Email address: admin@admin.com
Password:
Password (again):
Superuser created successfully.
```

_Note, that whatever user you create, the username is set to username_hash(self.email), e.g.:_

```python
>>> from src.users.models import username_hash
>>> username_hash('admin@admin.com')
Admin@D3942DCE
```

Run tests:

`py.test`

