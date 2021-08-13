# Flask app with SQL ORM
`flask`, `sqlite`, `orm`

## Docs
`app.py` - logic of application
`view_db.py` - will retreive data from DB and create Pandas dataframe 

## API endpoint
`http://127.0.0.1:5000/api/tasks` - returns all tasks from DB into JSON format

## Reference
- https://flask.palletsprojects.com/en/2.0.x/quickstart/
- https://flask-sqlalchemy.palletsprojects.com/en/2.x/

## Heroku deployment
```shell
heroku login
git init
git add .
git commit -m "init"
heroku create flask-sqlorm
git remote -v 
git push heroku master
```