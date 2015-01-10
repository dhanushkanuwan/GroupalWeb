# Groupal

sudo apt-get install python-psycopg2
sudo apt-get install libpq-dev

cd requirements
pip install -r dev.txt

cd settings
ln -s dev.py local.py

python manage.py makemigrations
python manage.py migrate

sudo apt-get install libjpeg-dev
sudo apt-get install zlib1g-dev
sudo apt-get install libpng12-dev


