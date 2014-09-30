sudo apt-get install python-psycopg2
sudo apt-get install libpq-dev
pip install -r requirements.txt
python manage.py migrate
python manage.py syncdb
dhanushka/dhanushka1977

python manage.py sqlmigrate web 0001
python manage.py migrate
python manage.py runserver