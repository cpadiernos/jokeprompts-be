[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.0.4-brightgreen.svg)](https://djangoproject.com)
[![Django REST Framework Version](https://img.shields.io/badge/django--rest--framework-3.11.0-brightgreen)](https://www.django-rest-framework.org/)

# Joke Prompts - web application (backend)

## Table of Contents

* [General Info](#general-info)
* [Screenshot](#screenshot)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Project Status](#project-status)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General Info
This is the Django and Django REST Framework backend for the joke prompts site.

## Screenshot
N/A

## Technologies
* Python 3.6.4
* Django 3.0.4

## Setup
To run the project on your local machine:

1. Clone the repository:
```
git clone https://github.com/cpadiernos/jokeprompts-be.git
```

2. Create a virtual environment and activate it.

3. Install the requirments:
```
pip install -r jokeprompts-be/requirements.txt
```

4. Go into jokeprompts-be folder:
```
cd jokeprompts-be
```

5. Rename the ".env.example" file to ".env".

6. Create the database:
```
python manage.py migrate
```

7. Create the user for the admin site:
```
python manage.py createsuperuser
```

8. Run the development server:
```
python manage.py runserver
```

9. Navigate to http://127.0.0.1:8000/admin and enter the information of the superuser you created earlier. Add your own custom prompts.

Jokes: http://127.0.0.1:8000/api/jokes/
Random Prompt: http://127.0.0.1:8000/api/prompts/random/

Demo coming soon...

## Features
* Random joke prompt API
* Jokes API saves prompt and joke

To Do:
* Add accounts to keep track of your own jokes
* Add rating per joke.
* ...

## Project Status
Unit tests are included.

## Inspiration
As a former comedian, I had to write jokes daily. I thought it would be fun to write a little app to help with the process.

## Contact
Created by [@cpadiernos](https://www.linkedin.com/in/carolpadiernos/). Feel free to reach out!
