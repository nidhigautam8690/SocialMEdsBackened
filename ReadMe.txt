//create virtual environment
pip install virtualnenvwrapper-win
mkvirtualenv Social_Meds
workon Social_Meds

//install django
pip install django

//create project on django
django-admin startproject SocialMeds
cd SocialMeds

//create and app inside the project
python manage.py startapp Facebook

// To create table inside database
python manage.py makemigrations
python manage.py migrate

//To cretae Superuser

python manage.py createsuperuser
then set Username & password

//To run server
python manage.py runserver

Run on Browser:
To run Project:
http://localhost:8000

To run admin panel:

http://localhost:8000/admin



//To upload the project on Git

git init
git add .
git commit -m "First COmmit"
git branch -m main
git remote add origin git@github.com:username/new_repo
git push -u main


//git clone

git clone url
