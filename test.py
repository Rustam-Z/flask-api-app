import requests
import json

BASE = "http://127.0.0.1:5001/"

get_the_list = requests.get(BASE + "tasks")
get_sigle_task = requests.get(BASE + "tasks/1")
delete_task = requests.delete(BASE + "tasks/1")
post_task = requests.post(BASE + "tasks", data=json.dumps({'task': 'test via post'}))
update_task = requests.put(BASE + "tasks/1", data=json.dumps({'task': 'test via put'}))

print(post_task.text)
