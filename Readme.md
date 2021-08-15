# Flask app with SQL ORM
https://flask-sqlorm.herokuapp.com

`flask`, `sqlite`, `sql orm`

## Docs
- `app.py` - main application
- `api.py` - API endpoints
- `models.py` - SQL ORM, database description
- `view_db.py` - will retreive data from DB and create Pandas dataframe 
- `test.py` - if you don't have **curl** 

## API endpoint 
**CRUD** -  Create (POST), Read (GET), Update (PUT), and Delete (DELETE)

`$ python api.py` 

Get the list

`$ curl http://localhost:5001/tasks`

GET a single task

`$ curl http://localhost:5001/tasks/<int:id>`

DELETE a task

`$ curl http://localhost:5001/tasks/<int:id> -X DELETE -v`

Add a new task

`$ curl http://localhost:5001/tasks -d "task=something new" -X POST -v`

Update a task

`$ curl http://localhost:5001/tasks/<int:id> -d "task=something different" -X PUT -v`


## Reference
- https://flask.palletsprojects.com/en/2.0.x/quickstart/
- https://flask-sqlalchemy.palletsprojects.com/en/2.x/
- https://flask-restful.readthedocs.io/en/latest/quickstart.html

## Heroku deployment
```shell
heroku login
pip freeze > requirements.txt
echo "web: gunicorn app:app" > Procfile
git init
git add .
git commit -m "init"
heroku create flask-sqlorm
git remote -v 
git push heroku master
```
