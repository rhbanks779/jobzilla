# JobZilla

JobZilla is a job listing and application platform built with Django.

## Project Overview

JobZilla allows users to create, update, and delete job postings, as well as search for jobs based on location or application deadlines. Users can also apply for jobs and receive email confirmations.

## Installation and Setup

###Clone the Repository

git clone https://github.com/yourusername/jobzilla.git
cd jobzilla

###Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

###Install Dependencies

pip install -r requirements.txt

###Setup Database

python manage.py makemigrations
python manage.py migrate

###Create a Superuser

python manage.py createsuperuser

###Run the Server

python manage.py runserver

###Access the Application
Open a web browser and go to http://127.0.0.1:8000/
