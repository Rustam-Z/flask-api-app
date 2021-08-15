import requests
import json

BASE = "http://127.0.0.1:5001/"

get_the_list = requests.get(BASE + "todos")
get_sigle_task = requests.get(BASE + "todos/todo1")
delete_task = requests.delete(BASE + "todos/todo1")
post_task = requests.post(BASE + "todos", data=json.dumps({'task': 'test via post'}))
update_task = requests.put(BASE + "todos/todo1", data=json.dumps({'task': 'test via put'}))

print(get_the_list.text)