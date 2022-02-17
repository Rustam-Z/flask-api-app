import requests
import json

BASE = "http://127.0.0.1:5000/"

get_the_list = requests.get(BASE + "tasks/")
get_single_task = requests.get(BASE + "tasks/2/")
delete_task = requests.delete(BASE + "tasks/1/")
post_task = requests.post(BASE + "tasks/", data=json.dumps({'task': 'test via post'}))
update_task = requests.put(BASE + "tasks/1/", data=json.dumps({'task': 'test via put'}))

print(get_single_task.json())
