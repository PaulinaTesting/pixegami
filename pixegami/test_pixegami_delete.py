import requests

ENDPOINT = "https://todo.pixegami.io"

def test_pixegami_delete():

    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]

    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 200

    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 404


    pass

def create_task(payload):
   return requests.put(ENDPOINT + "/create-task", json=payload)

def update_task(payload):
   return requests.put(ENDPOINT + "/update-task", json=payload)

def get_task(task_id):
   return requests.get(ENDPOINT + f"/get-task/{task_id}")

def delete_task(task_id):
   return requests.get(ENDPOINT + f"/delete-task/{task_id}")

def new_task_payload():
   return {
         "content": "my_test_content",
         "user_id": "test_user",
         "is_done": False
    }