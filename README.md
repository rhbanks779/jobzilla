## Job Board Application

### Create and Activate Virtual Environment

python -m venv env
source env/bin/activate
source env/Scripts/activate #for Windows

### Install Dependencies

pip install -r requirements.txt

### Apply Migrations and Run Server

python manage.py migrate
python manage.py runserver
