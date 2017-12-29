# Infinity

Install psql (PostgreSQL) 10.1, `createdb infinity`

`git clone git@github.com:inxyz/infinity.git`

Then:

```
cd infinity
virtualenv -ppython3 .env
. .env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
_Note, that whatever user you create, the username is set to username_hash(self.email), e.g.:_

```python
>>> from oo.users.models import username_hash
>>> username_hash('admin@admin.com')
Admin@D3942DCE
```


Apply fixtures:

```
python manage.py loaddata languages currencies
python manage.py loaddata currency_price_snapshots
python manage.py loaddata hour_price_snapshots
```

Run tests:

`py.test`

