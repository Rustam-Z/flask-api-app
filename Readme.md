# RESTful Flask CRUD API 

https://flask-sqlorm.herokuapp.com

Flask todo list project with RESTful API, and web UI. App is covered with unit, integration, Web UI, and Rest API tests.

`flask`, `sqlite`, `flask-sqlorm`, `pytest`, `selenium`

## Source files description
- `src/app.py` - application with wWb UI  
- `src/api.py` - API endpoints
- `src/models.py` - SQL ORM, database description
- `src/view_database.py` - will retrieve data from DB and create Pandas dataframe 

## API endpoints documentation
**CRUD** -  Create (POST), Read (GET), Update (PUT), and Delete (DELETE)

NOTE! When launching the server, be careful with the port number.

`$ python src/api.py` 

Get the list

`$ curl http://localhost:5001/tasks/`

GET a single task

`$ curl http://localhost:5001/tasks/<int:id>/`

DELETE a task

`$ curl http://localhost:5001/tasks/<int:id>/ -X DELETE -v`

Add a new task

`$ curl http://localhost:5001/tasks/ -d "task=something new" -X POST -v`

Update a task

`$ curl http://localhost:5001/tasks/<int:id>/ -d "task=something different" -X PUT -v`


## Testing requirement analysis
- `src/tests/test_app.py` - testing app.py
- `src/tests/test_api.py` - testing api.py


## Heroku deployment
```shell
heroku login
pip freeze > requirements.txt
echo "web: gunicorn src/app:app" > Procfile
git init
git add .
git commit -m "init"
heroku create flask-sqlorm
git remote -v 
git push heroku master
```

## Reference
- https://flask.palletsprojects.com/en/2.0.x/quickstart/
- https://flask-sqlalchemy.palletsprojects.com/en/2.x/
- https://flask-restful.readthedocs.io/en/latest/quickstart.html