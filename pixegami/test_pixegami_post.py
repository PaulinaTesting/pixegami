import requests

ENDPOINT = "https://todo.pixegami.io"

def test_pixegami_post():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    task_id = create_task_response.json()["task"]["task_id"]

    new_payload = {
       "user_id": payload["user_id"],
       "task_id": task_id,
       "content": "my updated content",
       "is_done": True,
    }

    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200


    pass

def create_task(payload):
   return requests.put(ENDPOINT + "/create-task", json=payload)

def update_task(payload):
   return requests.put(ENDPOINT + "/update-task", json=payload)

def get_task(task_id):
   return requests.get(ENDPOINT + f"/get-task/{task_id}")

def new_task_payload():
   return {
         "content": "my_test_content",
         "user_id": "test_user",
         "is_done": False
    }