# ParaPhraser

ParaPhraser is a web-based compiler for Python, C, C++ and Java.

## Prerequisites

Be sure you have the following installed on your development machine:

```
1. git
2. python >= 3.10.x
3. pip >= 22.2.x
4. virtualenv >= 20.16.3
```

## Setup

Clone the repository:

```bash
git clone https://github.com/adityanithariya/ParaPhraser.git
cd ParaPhraser
```

Create a virtual environment and activate it:

```bash
virtualenv env
.\env\Scripts\activate
```

Then install the dependencies:

```bash
pip install -r requirements.txt
```

Once `pip` has finished installing dependencies, you're ready to go!

### Initialising and Starting the Development Server

Run `makemigrations` and `migrate` for making all the required tables in the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

Run the django development server using `manage.py`:

```bash
python manage.py runserver
```

Congrats, you have successfully run the development server! \
Now navigate [here](http://127.0.0.1:8000/ "localhost:8000") for the website.

### Admin Panel

Create a superuser:

```bash
python manage.py createsuperuser
```

Enter `username` and `password` of created superuser [here](http:127.0.0.1:8000/admin "Admin Panel") to log into admin panel, where you can manage the database.
