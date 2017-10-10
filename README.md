# Flask-Postgres Template
The basic template of a flask application with postgres database integration.

_Frequently desired for a Heroku deployment._

## Quickstart

0.  Clone the repo.

```
$ git clone git@github.com:sharonzhou/flask-postgres.git
```

1.  Enter the glorious directory!

```
$ cd flask-postgres/
```

2.  Install libraries.

	_Ideally, into a virtual environment, e.g. with virtualenv or conda, but that is not required._

```
$ pip install -r requirements.txt
```

3.  Create a postgres database. We will link it to the flask app in the subsequent steps.

	Here's how to do it on a Mac with [Homebrew](https://brew.sh/), with a database named **my_practical_db_name**, which you can replace with a more practical database name.

```
$ brew services restart postgresql
$ createdb my_practical_db_name
```

4.  Get your database username. Below, it's **my_cool_username**.

```
$ psql my_practical_db_name

my_practical_db_name=# select current_user;

 current_user 
--------------
 my_cool_username

my_practical_db_name=# \q

```

5. Link the postgres database to the Flask app. 
	
	_The link to your database includes the database type (postgres), your username (my_cool_username), the host (localhost, aka. 127.0.0.1), and your database name (my_practical_db_name)._

```
$ export DATABASE_URL="postgresql://my_cool_username@localhost/my_practical_db_name"
```

6.  Start the server.

```
$ python run.py
```

7.  Open http://0.0.0.0:5000 in your browser.

8.  Check if your postgres database is integrated correctly by clicking: **Add a "Thing" to your database**.

9.  Modify this template to your project. 

	You can begin by adding styles to the placeholder CSS file living at [app/static/css/app.css](https://github.com/sharonzhou/flask-postgres/blob/master/app/static/css/app.css), and adding scripts to the placeholder Javascript file living at [app/static/js/app.js](https://github.com/sharonzhou/flask-postgres/blob/master/app/static/js/app.js). 