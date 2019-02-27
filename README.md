{{ project_name|title }}
========================

### Before start
You should already have at least django installed, I recommend creating the environment first, then install django and pipenv `$ pip install django pipenv`, after that, proceed with the setup below.

### Setting up...
1. Create the new project using our template `django-admin.py startproject <YOUR_PROJECT_NAME> --template=https://github.com/codecraft63/django-base/archive/master.zip --extension=js,py,json,md,html,vue`
2. Change folder `$ cd <YOUR_PROJECT_NAME>`
3. Create your `.env` file, check `.env.example` for reference
4. Install pipenv `$ pip install pipenv` (if you haven't already)
5. Run `$ pipenv install --dev`
6. Run `$ yarn install`
7. Run `$ ./manage.py migrate`
8. Run `$ ./manage.py runserver`
9. Run (in another term) `$ yartstart`
10. Open `http://localhost:8000`
11. ...
12. Profit!
