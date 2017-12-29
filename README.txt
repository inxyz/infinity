# Infinity

Install psql (PostgreSQL) 10.1

`git clone git@github.com:inxyz/infinity.git`

Then:

```
cd blogic
virtualenv -ppython3 .env
. .env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Apply fixtures:

```
python manage.py loaddata languages
python manage.py loaddata currencies
python manage.py loaddata currency_price_snapshots
python manage.py loaddata hour_price_snapshots
```
