import json
from django.urls import reverse

def test_create_task(client):
    response = client.post(
        reverse('api_create_task'),
        data=json.dumps({"title": "Test Task"}),
        content_type="application/json"
    )
    assert response.status_code == 201


def test_get_tasks(client):
    response = client.get(reverse('api_get_tasks'))
    assert response.status_code == 200
    assert isinstance(json.loads(response.content), list)


def test_update_task(client):
    # Create a task first
    response = client.post(
        reverse('api_create_task'),
        data=json.dumps({"title": "Old Title"}),
        content_type="application/json"
    )
    assert response.status_code == 201

    task_id = 1  # Since DB is simple, assume ID = 1 for test app

    response = client.put(
        reverse('api_update_task', args=[task_id]),
        data=json.dumps({"title": "Updated Title"}),
        content_type="application/json"
    )
    assert response.status_code == 200


def test_delete_task(client):
    task_id = 1
    response = client.delete(reverse('api_delete_task', args=[task_id]))
    assert response.status_code == 200
